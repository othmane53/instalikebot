import pyautogui as v
from time import sleep
import keyboard

hashtag = input(str('what hashtag are you searching for ? :\n'))

def work():
	v.click(224,753)
	sleep(1)
	v.write('firefox')
	sleep(1)
	v.press('enter')
	sleep(3)
	v.click(533,53)
	sleep(1)
	v.write('instagram.com')
	sleep(1)
	v.press('enter')
	sleep(3)
	v.click(680,131)
	sleep(4)
	keyboard.write(hashtag)
	sleep(4)
	v.click(688,201)
	sleep(4)
	v.click(345,451)
	sleep(4)
	while True:
		v.doubleClick(345,451)
		sleep(3)
		v.press('right')
		sleep(3)
		v.doubleClick(345,451)


work()
