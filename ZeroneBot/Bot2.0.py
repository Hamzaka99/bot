import cv2
import time
import keyboard
import pyautogui
import win32api
import win32con

time.sleep(5)

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)

while not keyboard.is_pressed('q'):
    uparrow = pyautogui.locateCenterOnScreen('uparrow.png', grayscale=True, confidence=0.70)
    if uparrow is not None:
        pyautogui.moveTo(uparrow)  # Moves the mouse to the coordinates of the image
        click()
