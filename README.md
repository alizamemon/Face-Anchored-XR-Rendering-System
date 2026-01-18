# Face-Anchored XR Rendering System  
A Human-Centric Augmented Reality Prototype for Extended Reality (XR)

---

## Project Overview

This project is a **real-time Face-Anchored Extended Reality (XR) system** that overlays virtual objects (glasses, hats, crowns, etc.) onto a human face using **3D facial landmark geometry**.

Unlike basic AR filters, this system is designed with **human perception, visual stability, and XR principles** in mind.  
It focuses on **pose-correct rendering, depth-aware scaling, and temporal smoothing** to ensure a realistic and comfortable user experience.

The project directly aligns with **Extended Reality (XR)** concepts such as **Human Sensation & Perception**, **3D Vision Computation**, and **Human-Centered System Design**.

---

## Key Features

### 1️⃣ Face-Anchored Object Placement  
Virtual assets are anchored using **MediaPipe Face Mesh (468 3D landmarks)**, ensuring accurate positioning relative to facial anatomy.

---

### 2️⃣ Pose-Correct Rendering (Head Tilt Awareness)  
The system computes facial orientation using geometric relations between landmarks and rotates virtual objects accordingly.

```text
Result: Glasses and hats rotate naturally with head movement
```
## 3️⃣ Depth-Aware Scaling (3D Perception)

Using the **Z-coordinate of facial landmarks**, the system dynamically scales virtual objects when the user moves closer or farther from the camera.

- **Closer face → larger virtual object**  
- **Farther face → smaller virtual object**

This behavior simulates **depth perception**, a core concept in Extended Reality (XR).

---

## 4️⃣ Temporal Smoothing (Perceptual Stability)

A **rolling average buffer** smooths landmark positions across consecutive frames, significantly reducing jitter and visual noise.

**Benefit:**  
- Increased visual comfort  
- Reduced motion sickness  
- More stable XR experience  

---

## 5️⃣ Multi-Asset XR Filters

The system supports multiple virtual assets:

- Glasses  
- Mustache  
- Hat  
- Crown  

Users can switch between filters **in real time** using keyboard input.

---

## 6️⃣ Real-Time Performance Monitoring

Frames Per Second (**FPS**) is calculated and displayed continuously to ensure real-time constraints are met.

This demonstrates:
- System awareness  
- Performance evaluation  
- Real-time processing capability  

---

## 7️⃣ XR Debug HUD (Explainable System)

A minimal **Heads-Up Display (HUD)** provides real-time system insights:

- Active XR module  
- Head tilt angle  
- System FPS  

This makes the system:
- Interpretable  
- Testable  
- Research-friendly  

---

## System Workflow

1. Webcam captures real-time video frames  
2. MediaPipe Face Mesh extracts **3D facial landmarks**  
3. Facial pose and depth are computed  
4. Temporal smoothing stabilizes landmark movement  
5. Virtual assets are scaled, rotated, and rendered  
6. Final XR output is displayed with performance metrics  

---

## Technical Stack

- **Language:** Python 3.x  
- **Computer Vision:** OpenCV  
- **Facial Landmark Detection:** MediaPipe Face Mesh  
- **Mathematics & Geometry:** NumPy, Math  
- **Real-Time Processing:** OpenCV Video Capture  

---

## Project Structure

```plaintext
XR_Face_Anchoring_Project/
├── assets/
│   ├── glasses.png
│   ├── mustache.png
│   ├── hat.png
│   └── crown.png
├── AR.py
└── README.md
```

## 🛠️ How to Run

### 1️⃣ Install dependencies

```bash
pip install opencv-python mediapipe numpy

```

### 2️⃣ Add Assets

Put images in assets folder:

* `glasses.png`
* `mustache.png`
* `hat.png`
* `crown.png`

### 3️⃣ Run the application

```bash
python AR.py

```
### 4️⃣ System Output

<img width="637" height="510" alt="Screenshot 2026-01-19 033355" src="https://github.com/user-attachments/assets/91297068-8731-44a0-8367-9ce913f0b95f" />
<img width="639" height="511" alt="Screenshot 2026-01-19 033437" src="https://github.com/user-attachments/assets/11bb244b-a632-4b54-9e67-8fc42f0db438" />

---

## Controls

| Key | Action |
| --- | --- |
| **1 – 4** | Switch between different XR assets |
| **Q** | Quit the application |

---

## Academic & XR Relevance

This project demonstrates a practical understanding of core XR principles required for research-level applications:

* **Human-Centered XR Design:** Mapping virtual assets to biological landmarks.
* **3D Vision & Depth Estimation:** Using Z-depth for perspective-correct scaling.
* **Pose-Aware Rendering:** Real-time trigonometry for head-tilt alignment.
* **Perceptual Stability:** Implementation of temporal smoothing to enhance user comfort.
* **Performance-Aware CV:** Optimizing CPU-based inference for real-time FPS.


---

## Future Enhancements

* **Kalman Filtering:** Transitioning from moving averages to predictive state estimation.
* **True 3D Rendering:** Integrating OpenGL or Unity for depth-buffered 3D models.
* **Multi-Face Support:** Extending spatial anchors for multiple users in the frame.
* **Gaze-Aware Interaction:** Linking the eye-tracking project with this AR system for intent-based filtering.

---

## 👤 Author

**Aliza Memon** *Computer Engineer*

📧 **Email:** [alizanisar11@gmail.com](mailto:alizanisar11@gmail.com)

🌐 **Portfolio:** [portfolioaliza.netlify.app](https://portfolioaliza.netlify.app)
