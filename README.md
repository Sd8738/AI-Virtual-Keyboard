# ⌨️ AI Virtual Touchless Keyboard

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange.svg)](https://google.github.io/mediapipe/)

A fully functional **AI Virtual Keyboard** built using Python and Computer Vision. This project allows users to type on a virtual interface using hand gestures captured by a webcam, eliminating the need for physical hardware.

---

## 🚀 Features
- **Real-Time Hand Tracking:** Utilizes `cvzone` and `mediapipe` for high-speed landmark detection.
- **Touchless Typing:** Simulates key presses by calculating the Euclidean distance between the Index and Middle finger tips.
- **Visual Feedback:** - **Purple:** Default state.
  - **Dark Purple:** Hover state (Finger over key).
  - **Green:** Click state (Key pressed).
- **QWERTY Layout:** Standard keyboard arrangement for intuitive usage.
- **Live Output:** Displays the typed text in real-time on the screen.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:**
  - `opencv-python` (Image processing)
  - `cvzone` (Hand tracking module wrapper)
  - `mediapipe` (Underlying ML framework for hand landmarks)
  - `pynput` (To simulate physical keyboard events)

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone [[https://github.com/Sd8738/AI-Virtual-Keyboard.git](https://github.com/Sd8738/AI-Virtual-Keyboard.git)]
   cd AI-Virtual-Keyboard


 Install Dependencies Run the following command to install the required libraries:
 pip install opencv-python cvzone mediapipe pynput

 Run the Script
 python AI-Virtual-Keyboard.py

 🧠 How It Works
The system captures video frames and processes them through the HandDetector module.

It identifies 21 hand landmarks.

It tracks the position of the Index Finger tip (Landmark 8).

It checks if the finger is within the coordinates of any virtual button.

It calculates the distance between Landmark 8 (Index Tip) and Landmark 12 (Middle Tip). If the distance is below the threshold, it triggers a keystroke using pynput.

👨‍💻 Author
Sumant Deshmukh LinkedIn | GitHub
