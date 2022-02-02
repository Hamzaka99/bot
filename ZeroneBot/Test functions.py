import pyautogui


uparrow = pyautogui.locateCenterOnScreen('uparrow.png', grayscale=True, confidence=0.70)

if uparrow is not None:
        pyautogui.moveTo(uparrow)  # Moves the mouse to the coordinates of the image
    
