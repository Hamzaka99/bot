import pyautogui


uparrow = pyautogui.locateCenterOnScreen('C:\Users\yousef\Desktop\ZeroneBot-20220202T101148Z-001\ZeroneBot\ZeroneBot\test functions\uparrow.png', grayscale=True, confidence=0.70)

if uparrow is not None:
        pyautogui.moveTo(uparrow)  # Moves the mouse to the coordinates of the image
    
