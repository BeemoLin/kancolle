# encoding: utf-8
import time
import sys

# three party
from colorama import init
from termcolor import colored
#colored init
init()

_flag = True
#click LAG
_LAG = 0.5
# current place
_place = "port"
#screen offset
_offset = (0, 50)

#self model import
import Utility
import _command

u = Utility
c = _command


def main():
    # init something
    # ...
	while _flag:
		_user_input = raw_input(colored("電：ご命令を", "green") + ">")
		if is_handled_by_predefined_func(_user_input) is True:
			continue
		
		check_command(_user_input)
		

def is_handled_by_predefined_func(input_cmd):
	global _place
	global _flag
	if input_cmd == "exit":
		_flag = False
		print colored("電：お疲れさまでした", "green")
		return True
	elif input_cmd == 'place p':
		_place = "port"
		print current_status()
		return True
	elif input_cmd == "place e":
		_place = "expedition"
		print current_status()
		return True
	elif input_cmd == "place r":
		_place = "refill"
		print current_status()
		return True
	elif input_cmd == '?':
		print current_status()
		return False
	elif input_cmd == 'auto e':
		auto_e()
		return False
	elif _place != "":
		return False
	else:
		print input_cmd + " poi?"
		return True

def auto_e():
	e_flag = True
	while(e_flag):
		try:
			print_now()
			time.sleep(1)
		except KeyboardInterrupt:
			print colored("自動遠征が中断されました", "red")
			e_flag = False

def print_now():
	sys.stdout.write("\r{}".format(time.strftime('%Y-%m-%d %X',time.localtime())))
	sys.stdout.flush()

def check_command(input_cmd):
	cmd = {}
	if _place == "port":
		cmd = c.get_port()
	elif _place == "expedition":
		cmd = c.get_expedition()
	elif _place == "refill":
		cmd = c.get_refill()

	if cmd.has_key(_place):
		if cmd[_place].has_key(input_cmd):
			run_command(cmd[_place][input_cmd])
		else:
			if input_cmd == "?":
				print cmd[_place].keys()
			else:
				print input_cmd + " poi?"

def run_command(cmd):
	print cmd[0]
	click_point = (cmd[1][0] + _offset[0], cmd[1][1] + _offset[1])
	u.change_window()
	u.click_and_wait(click_point, cmd[2], _LAG)
	u.change_window()

def current_status():
	current_status = "電："
	current_status += " Place = " + colored(_place, "yellow")
	current_status += " Lag = " + colored(str(_LAG), "yellow")
	return current_status

main()
