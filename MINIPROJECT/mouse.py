import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands and drawing utility
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Detect a single hand for simplicity
mp_drawing = mp.solutions.drawing_utils

# Get screen dimensions for mouse movement scaling
screen_width, screen_height = pyautogui.size()

# Start capturing video from the webcam
camera = cv2.VideoCapture(0)

# Variables to track clicking and dragging state
clicking = False
dragging = False
right_clicking = False
click_start_time = 0
drag_threshold_time = 0.3  # Time in seconds to distinguish drag from click
last_click_time = 0
click_delay = 0.5  # Minimum delay between clicks to avoid double clicks

try:
    while True:
        # Capture frame from webcam
        ret, image = camera.read()
        if not ret:
            print("Failed to grab frame.")
            break
        image = cv2.flip(image, 1)  # Flip the image horizontally
        image_height, image_width, _ = image.shape

        # Convert the frame to RGB for MediaPipe
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_image)
        landmarks = result.multi_hand_landmarks

        if landmarks:
            for hand_landmarks in landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get landmark coordinates for fingers
                index_finger_tip = hand_landmarks.landmark[8]
                thumb_tip = hand_landmarks.landmark[4]
                middle_finger_tip = hand_landmarks.landmark[12]
                pinky_finger_tip = hand_landmarks.landmark[20]

                # Move mouse cursor
                mouse_x = int(index_finger_tip.x * screen_width)
                mouse_y = int(index_finger_tip.y * screen_height)
                pyautogui.moveTo(mouse_x, mouse_y)

                # Calculate distance between index and middle fingers for scrolling
                index_middle_dist = abs(int(middle_finger_tip.y * image_height) - int(index_finger_tip.y * image_height))

                # Task: Scrolling (Up/Down)
                if index_middle_dist < 30:
                    pyautogui.scroll(-20)  # Scroll down
                elif index_middle_dist > 50:
                    pyautogui.scroll(20)  # Scroll up

                # Task: Click or Drag - Detect pinch between thumb and index finger
                thumb_index_dist = abs(int(thumb_tip.y * image_height) - int(index_finger_tip.y * image_height))

                # Start pinch detection for click/drag
                if thumb_index_dist < 40:  # Thumb and index are close enough
                    if not clicking:
                        clicking = True
                        click_start_time = time.time()  # Start timing the pinch

                    # Check if the pinch gesture has lasted long enough to be a drag
                    if time.time() - click_start_time > drag_threshold_time:
                        if not dragging:
                            dragging = True
                            pyautogui.mouseDown()  # Start dragging

                else:
                    # If thumb and index are no longer close, stop click or drag
                    if clicking:
                        # If it was a short pinch, treat it as a click
                        if not dragging and (time.time() - click_start_time < drag_threshold_time):
                            current_time = time.time()
                            if current_time - last_click_time > click_delay:
                                pyautogui.click()  # Perform left-click
                                last_click_time = current_time
                        clicking = False
                        dragging = False
                        pyautogui.mouseUp()  # Stop dragging if it was active

                # Task: Right-click - Detect pinch between thumb and pinky finger
                thumb_pinky_dist = abs(int(thumb_tip.y * image_height) - int(pinky_finger_tip.y * image_height))

                if thumb_pinky_dist < 40:
                    current_time = time.time()
                    if not right_clicking and (current_time - last_click_time > click_delay):
                        pyautogui.rightClick()  # Perform right-click
                        right_clicking = True
                        last_click_time = current_time
                else:
                    right_clicking = False  # Reset right-click state when fingers are apart

        # Display the video feed with annotations
        cv2.imshow("Hand Gesture Scrolling, Clicking, and Right-Click Control", image)

        # Exit when ESC key is pressed
        if cv2.waitKey(1) & 0xFF == 27:
            break

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Release the camera and close OpenCV windows
    camera.release()
    cv2.destroyAllWindows()
