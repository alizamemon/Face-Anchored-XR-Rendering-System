import cv2
import mediapipe as mp
import numpy as np
import math
import time
from collections import deque

# Initialize MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Smoothing buffer
smooth_pts = deque(maxlen=5)

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0,0))

def overlay_image(background, foreground, x, y, w, h, angle):
    foreground = cv2.resize(foreground, (w, h))
    if angle != 0:
        foreground = rotate_image(foreground, angle)
    alpha_mask = foreground[:, :, 3] / 255.0
    for c in range(0, 3):
        if 0 <= y < background.shape[0]-h and 0 <= x < background.shape[1]-w:
            background[y:y+h, x:x+w, c] = (1.0 - alpha_mask) * background[y:y+h, x:x+w, c] + alpha_mask * foreground[:, :, c]

filters = {
    '1': {'img': cv2.imread('glasses.png', cv2.IMREAD_UNCHANGED), 'name': 'Glasses'},
    '2': {'img': cv2.imread('mustache.png', cv2.IMREAD_UNCHANGED), 'name': 'Mustache'},
    '3': {'img': cv2.imread('hat.png', cv2.IMREAD_UNCHANGED), 'name': 'Hat'},
    '4': {'img': cv2.imread('crown.png', cv2.IMREAD_UNCHANGED), 'name': 'Crown'}
}
current_filter = '1'
p_time = 0

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    # --- LAYER 5: Performance Metrics ---
    c_time = time.time()
    fps = 1 / (c_time - p_time)
    p_time = c_time
    cv2.putText(frame, f"FPS: {int(fps)}", (w-100, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    if results.multi_face_landmarks:
        lm = results.multi_face_landmarks[0].landmark
        
        # --- LAYER 2: Depth-Aware Scaling ---
        # MediaPipe Z value ranges approx from -0.1 to 0.1
        z_depth = lm[6].z 
        depth_scale = np.interp(z_depth, [-0.15, 0.15], [1.2, 0.8])

        # Alignment Logic (Aapki purani values)
        if current_filter == '1': 
            idx1, idx2, idx_anc, scale, off_y = 130, 359, 6, 1.4, 0.6
        elif current_filter == '2': 
            idx1, idx2, idx_anc, scale, off_y = 205, 425, 164, 0.8, 0.5
        else: 
            idx1, idx2, idx_anc, scale, off_y = 130, 359, 10, 2.0, 1.0

        curr_pts = np.array([[lm[idx1].x*w, lm[idx1].y*h], [lm[idx2].x*w, lm[idx2].y*h], [lm[idx_anc].x*w, lm[idx_anc].y*h]])
        smooth_pts.append(curr_pts)
        avg_pts = np.mean(smooth_pts, axis=0)
        p1, p2, anc = avg_pts[0], avg_pts[1], avg_pts[2]

        angle = -math.degrees(math.atan2(p2[1]-p1[1], p2[0]-p1[0]))
        # Multiplying width by depth_scale for 3D effect
        g_w = int(np.linalg.norm(p2 - p1) * scale * depth_scale)
        f_img = filters[current_filter]['img']
        g_h = int(g_w * (f_img.shape[0] / f_img.shape[1]))

        tx, ty = int(anc[0] - (g_w / 2)), int(anc[1] - (g_h * off_y))

        if 0 < tx < w-g_w and 0 < ty < h-g_h:
            overlay_image(frame, f_img, tx, ty, g_w, g_h, angle)

        # --- LAYER 4: HUD ---
        cv2.putText(frame, f"SYS_ACTIVE: {filters[current_filter]['name']}", (30, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f"POSE_TILT: {int(angle)} deg", (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    cv2.imshow('Face-Anchored XR Rendering System', frame)
    key = cv2.waitKey(1) & 0xFF
    if chr(key) in filters: 
        current_filter = chr(key)
        smooth_pts.clear()
    elif key == ord('q'): break

cap.release()
cv2.destroyAllWindows()