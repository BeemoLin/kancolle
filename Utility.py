# encoding: utf-8
import time
import random
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from termcolor import colored

_m = PyMouse()
_k = PyKeyboard()
#x_dim, y_dim = m.screen_size()
#m.click(x_dim/2, y_dim/2, 1)
#k.type_string('Hello, World!')

def click_and_wait(position, blur, sleep_sec):
	click_no_wait(position, blur)
	_sleep(sleep_sec)


def click_no_wait(position, blur):
	click_x = position[0] + _rand(blur[0])
	click_y = position[1] + _rand(blur[1])
	print colored('がるるー: (' + str(click_x) + ', ' + str(click_y) + ')', 'grey')
	_m.click(click_x, click_y)

def change_window():
	#_k.press_key('command')
	#_k.tap_key('tab', interval=0.2)
	#_k.release_key('command')
	_sleep(0.5)

def focus_screen():
	#click_and_wait(position, blur, lag)
	click_and_wait((0, 150), (0, 0), 0.5)
	click_and_wait((0, 150), (0, 0), 0.5)
	click_and_wait((200, 40), (0, 0), 0.5)

def _sleep(sleep_sec):
	rand_lag = float(random.randint(0, 3000) / 1000)
	print colored('ちょっと待って:' + str(sleep_sec + rand_lag), 'grey')
	time.sleep(sleep_sec + rand_lag)

def _rand(rand_range):
	rand = random.randint(-rand_range, rand_range)
	return rand
