import pyautogui
import time

def click(): 
    time.sleep(0.1)     
    pyautogui.click()

def place():
	pyautogui.moveTo(350, 200)
	click()
	pyautogui.dragTo(550, 200)
	click()


while True:
	#place()
	"""
	if pyautogui.press('esc') == True:
		break"""
	print(pyautogui.press('esc'))