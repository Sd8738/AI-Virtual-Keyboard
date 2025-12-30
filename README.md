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
   git clone [https://github.com/your-username/AI-Virtual-Keyboard.git](https://github.com/your-username/AI-Virtual-Keyboard.git)
   cd AI-Virtual-Keyboard
