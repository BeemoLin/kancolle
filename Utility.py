from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random

_m = PyMouse()
_k = PyKeyboard()
#x_dim, y_dim = m.screen_size()
#m.click(x_dim/2, y_dim/2, 1)
#k.type_string('Hello, World!')

def click_and_wait(position, blur, sleep_sec):
	click_no_wait(position, blur)
	_sleep(sleep_sec)

def click_no_wait(position, blur):
	click_x = position[0] + _rand(blur)
	click_y = position[1] + _rand(blur)
	_m.click(click_x, click_y)
	_m.click(click_x, click_y)

def change_window():
	_k.press_key('command')
	_k.tap_key('tab', interval=0.1)
	_k.release_key('command')

def _sleep(sleep_sec):
	time.sleep(sleep_sec)

def _rand(rand_range):
	rand = random.randint(-rand_range, rand_range)
	return rand
