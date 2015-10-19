# encoding: utf-8
import time
import sys
import os
import glob
import json
from pprint import pprint

# three party
from colorama import init
from termcolor import colored
#colored init
init()

_flag = True
#click LAG
_LAG = 2.0
# current place
_place = "port"
#screen offset
_offset = (0, 50)

#self model import
import utility
import _command

u = utility
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
	elif input_cmd == 'game':
		u.focus_screen()
		return True
	elif _place != "":
		return False
	else:
		print input_cmd + " poi?"
		return True

def auto_cmd(_cmd):
	if is_handled_by_predefined_func(_cmd) is False:
		check_task_command(_cmd)

def auto_e():
	e_flag = True
	while(e_flag):
		try:
			e_task()
			time.sleep(1)
		except KeyboardInterrupt:
			print colored("自動遠征が中断されました", "red")
			e_flag = False

def e_task():
	g = glob
	files = sorted(g.glob('../logbook/json/*PORT.json'), key=os.path.getmtime, reverse = True)
	
	show_msg = colored("電：任務中 ", "green")
	
	if files:
		update_time = time.strftime("(%a)%X ", time.localtime(os.path.getmtime(files[0])))

		data = read_port(files[0])
		show_msg += expedition_msg(data, 1)
		show_msg += expedition_msg(data, 2)
		show_msg += expedition_msg(data, 3)
		show_msg += colored("更新:" , "green") + colored(update_time, "yellow")
	
	now_time = time.strftime("(%a)%X", time.localtime())
	show_msg += colored("今:", "green") + colored(now_time, "yellow")
	
	sys.stdout.write("\r{}".format(show_msg))
	sys.stdout.flush()
	
	if expedition_status(data, 1) is False:
		expedition_cmd(1, (1, 5))
	
	if expedition_status(data, 2) is False:
		expedition_cmd(2, (3, 4))
	
	if expedition_status(data, 3) is False:
		expedition_cmd(3, (5, 5))

def read_port(file_path):
	with open(file_path)as data_file:
		data = json.load(data_file)
	return data


def expedition_status(data, team):
	team_data = str(data["api_data"]["api_deck_port"][team]["api_mission"][2])[0:10]
		
	if time.localtime(float(team_data)) > time.localtime():
		return True	
	else:
		return False

def expedition_msg(data, team):
	team_data = str(data["api_data"]["api_deck_port"][team]["api_mission"][2])[0:10]
	team_time = time.strftime("(%a)%X ", time.localtime(float(team_data)))
	show_msg = colored(str(team + 1) + "番隊:", "green")
		
	if time.localtime(float(team_data)) > time.localtime():
		show_msg += colored(team_time, "yellow")
	else:
		show_msg += colored(team_time, "red")
	return show_msg

def expedition_cmd(team, (area, no)):

	# wellcome back
	auto_cmd("place p")
	auto_cmd("poi")
	auto_cmd("go")
	auto_cmd("home")
	auto_cmd("go")
	auto_cmd("home")
	auto_cmd("poi")
	time.sleep(8.0)
	auto_cmd("poi")
	auto_cmd("poi")
	auto_cmd("poi")
	time.sleep(8.0)
	auto_cmd("poi")
	auto_cmd("poi")
	auto_cmd("poi")
	time.sleep(8.0)
	auto_cmd("poi")
	auto_cmd("poi")

	#refill
	time.sleep(4.0)
	auto_cmd("go")
	auto_cmd("place r")
	auto_cmd("enter")
	auto_cmd("f" + str(team + 1))
	auto_cmd("all")

	#expedition
	time.sleep(4.0)
	auto_cmd("place p")
	auto_cmd("home")
	auto_cmd("go")
	auto_cmd("place e")
	auto_cmd("enter")
	auto_cmd("e" + str(area))
	auto_cmd(str(no))
	auto_cmd("ok")
	auto_cmd("f" + str(team + 1))
	auto_cmd("start")

	#back home
	time.sleep(5.0)
	auto_cmd("place p")
	auto_cmd("home")
	auto_cmd("go")
	auto_cmd("home")
	auto_cmd("poi")

def check_task_command(input_cmd):
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
			u.change_window()
			run_command(cmd[_place][input_cmd])
			u.change_window()
		else:
			if input_cmd == "?":
				print cmd[_place].keys()
			else:
				print input_cmd + " poi?"

def run_command(cmd):
	print cmd[0]
	click_point = (cmd[1][0] + _offset[0], cmd[1][1] + _offset[1])
	u.click_and_wait(click_point, cmd[2], _LAG)

def current_status():
	current_status = "電："
	current_status += " Place = " + colored(_place, "yellow")
	current_status += " Lag = " + colored(str(_LAG), "yellow")
	return current_status

main()
