import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# --- CONFIGURATION ---
cam_width, cam_height = 1280, 720 # Higher resolution is better for keyboards
cap = cv2.VideoCapture(0)
cap.set(3, cam_width)
cap.set(4, cam_height)

# Setup Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)
keyboard = Controller()

# Define Key Layout
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

finalText = ""

# --- BUTTON CLASS ---
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

# Create Button Objects
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        # Position buttons nicely in a grid
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# --- DRAWING FUNCTION ---
def drawAll(img, buttonList):
    # Draw transparent rectangles
    # Note: cvzone makes this easier, but we draw manually for style
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        
        # Draw the button background
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), cv2.FILLED)
        # Draw the text
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.plain_old_compatible_cv_enum_flags.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

print("AI Keyboard Started! Press 'q' to exit.")

while True:
    success, img = cap.read()
    if not success:
        break
    
    img = cv2.flip(img, 1) # Mirror the image
    
    # Detect Hands
    hands, img = detector.findHands(img, flipType=False) # flipType=False because we already flipped
    
    # Draw all buttons with some transparency
    # (To make it look "Sci-Fi", we draw on a copy and blend it)
    imgNew = img.copy()
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(imgNew, (x, y), (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgNew, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    
    # Blend the button image with original image (Transparency)
    alpha = 0.5
    cv2.addWeighted(imgNew, alpha, img, 1 - alpha, 0, img)

    # --- LOGIC ---
    if hands:
        hand = hands[0] # Get the first hand
        lmList = hand["lmList"] # Get list of landmarks
        
        # Index finger tip (8) and Middle finger tip (12)
        # Note: cvzone lmList has [x, y, z] structure
        x8, y8 = lmList[8][0], lmList[8][1]
        x12, y12 = lmList[12][0], lmList[12][1]

        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            # Check if Index Finger is inside the button box
            if x < x8 < x + w and y < y8 < y + h:
                
                # Highlight the button (Make it darker/solid)
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                
                # Check for "Click" (Distance between Index and Middle finger)
                # length, info, img = detector.findDistance(8, 12, img) # Old cvzone syntax
                
                # Calculate distance manually or use detector (simpler manual here)
                length = ((x8 - x12) ** 2 + (y8 - y12) ** 2) ** 0.5
                
                # If fingers are close (Click)
                if length < 30:
                    # Visual Feedback (Green Color)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    
                    # Press the key
                    keyboard.press(button.text)
                    keyboard.release(button.text)
                    finalText += button.text
                    sleep(0.15) # Delay to prevent double typing

    # Show the text you have typed so far
    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("AI Virtual Keyboard", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()