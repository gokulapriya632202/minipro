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

## OUTPUT

Mouse cursor

![Screenshot 2024-11-13 122834](https://github.com/user-attachments/assets/76cf996c-8d89-461f-8661-58e3b24e7ce5)

Scroll Up

![Screenshot 2024-11-13 122934](https://github.com/user-attachments/assets/279a3b55-b2b3-4514-8c3e-62ad5d4a54b3)

Scroll down

![Screenshot 2024-11-13 122909](https://github.com/user-attachments/assets/9f772fca-7b89-4811-912a-d3ff5f08e546)

Right click

![Screenshot 2024-11-13 123330](https://github.com/user-attachments/assets/f88caeae-1f63-4395-a733-03d4558b38aa)

Left click

![Screenshot 2024-11-13 123350](https://github.com/user-attachments/assets/bdc82f1e-66f1-4c70-9001-de17688aa069)

## RESULTS AND IMPACTS

The real-time hand gesture recognition system for mouse control showed excellent accuracy and dependability in identifying a variety of hand gestures while effectively converting them into mouse commands, such as clicking, scrolling, and moving the pointer. The user's hand was precisely isolated against various backdrops and live video feeds were successfully processed by the system, enabling responsive and fluid handling that closely mimics the feel of a conventional mouse. The system's resilience was confirmed by testing, which revealed constant performance across a range of backdrops and lighting circumstances. Additionally, the CNN model accurately classified gestures, allowing for smooth, organic real-time interaction.

With its revolutionary approach to human-computer interaction, this system improves accessibility and ergonomics of technology, especially in settings where it is beneficial to operate hands-free. It facilitates touchless, sterile control in healthcare, assisting medical personnel throughout treatments without sacrificing hygienic standards. By offering a different method of computer control, the device also helps those with physical limitations, encouraging inclusivity in digital settings. With an easy-to-use interface that improves user experience, it may also find usage in smart home systems, public presentations, and industrial environments. Its usefulness and accessibility may be further increased across other use cases with future advancements in gesture complexity and environmental factor adaptation.

## Articles published / References

*(2022). Deep learning based Hand gesture recognition system and design of a Human-Machine Interface. doi: 10.48550/arxiv.2207.03112
*M.Dhyanesh., R., Vijay, Kumar., MD., Ameena., M., Surya, Teja., R., Vijay, Krishna., Dr., G., Krishna, Kishore. (2024). Virtual Mouse using Hand Gesture Recognition. International Journal For Multidisciplinary Research, doi: 10.36948/ijfmr.2024.v06i02.14594
*Ramachandrudu, Chowdam, C. Ajith, and T. Murali. "Human Computer Interaction Using Hand Gesture.“
*K. Roy and M. A. H. Akif, "Real Time Hand Gesture Based User Friendly Human Computer Interaction System," 2022 International Conference on Innovations in Science, Engineering and Technology (ICISET), Chittagong, Bangladesh, 2022, pp. 260-265, doi: 10.1109/ICISET54810.2022.9775918.
*Shaikh, Sahil, Gaurav Narode, Kalyani Thorat, Achal Pardeshi, and D. P. Jain. "GESTURE RECOGNITION BASED VIRTUAL MOUSE AND KEYBOARD."








