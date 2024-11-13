# MINIPROJECT

## TITLE OF THE PROJECT
Real-Time Hand Gesture Recognition for Mouse Control

## ABOUT
Gesture recognition has become a hands-free substitute for conventional input devices like the mouse as the need for natural and intuitive human-computer interaction (HCI) grows. A real-time hand gesture detection system for mouse control is shown in this study, which uses basic hand gestures to carry out standard mouse operations. The system records live footage of the user's hand using a conventional camera. It then uses computer vision algorithms to recognize motions and translate them into actions like scrolling, clicking, and moving the cursor. Fundamentally, the system separates the hand from the background using a combination of image processing techniques, including contour analysis, skin color segmentation, and background subtraction, and accurately classifies hand postures using a convolutional neural network (CNN) trained on gesture datasets. 
In situations like healthcare or for people with physical limitations, where typical input devices are unfeasible, this touchless control method provides an ergonomic and user-friendly interaction model. The system, which is intended for real-time performance, offers responsive, low-latency control that is on par with a traditional mouse, making it a useful and affordable substitute. High accuracy and reliable real-time performance are demonstrated during testing; further enhancements could include multi-gesture detection for intricate commands and improved accuracy in a variety of environments and lighting conditions.

## FEATURES

  - Real-Time Gesture Recognition: Captures and processes hand gestures from a live video feed, enabling responsive and interactive mouse control.
  -  Multiple Mouse Controls: Supports cursor movement, left-click, right-click, scrolling, and drag-and-drop, allowing a wide range of mouse functions via hand gestures.
  -  Hand Tracking and Detection: Utilizes computer vision libraries (e.g., MediaPipe, OpenCV) for precise hand and finger detection.
  -  Gesture-Based Commands: Maps specific gestures to different mouse actions (e.g., pinching for click, separating fingers for scroll), making the interface intuitive.
  -  User-Friendly Interface: Designed for smooth interaction, with gestures corresponding naturally to mouse actions, minimizing the need for physical device contact.
    
## REQUIREMENTS

* Hardware Requirements:
  *Camera or Webcam for capturing real-time hand gestures.
  *Computer with moderate processing power to handle real-time video processing.
  *Minimum 8 GB RAM for efficient performance.
*Software Requirements:
  *Python 3.x as the programming language.
*Libraries:
  *OpenCV for image and video processing.
  *MediaPipe for hand tracking and gesture recognition.
  *NumPy for numerical computations.
  *PyAutoGUI for mouse control actions.
  *TensorFlow/Keras (optional) for deep learning-based gesture recognition.
  *Compatible with Windows, macOS, or Linux.

## SYSTEM ARCHITECTURE

![MINIPROJECT AD](https://github.com/user-attachments/assets/cbcb3ea8-8983-4734-9191-13d90c0860de)


