# encoding: utf-8
import sys
import time
import datetime
import os
import glob
import json
import random
from pprint import pprint

# three party
from colorama import init
from termcolor import colored
#colored init
init()

_flag = True
#click LAG
_LAG = 2.0
#_task_list = ((海域, 任務), (海域, 任務), (海域, 任務))
# 20~40MIN:[3]LV3 3SS [6鋁]LV4 4SS or DD
# 1~2HR:[5]LV3 1輕 2DD 1SS [21]LV15+30 1輕 5DD 4罐 [37]LV50+200 1輕 5DD 5罐
# 1~2HR:[38]LV65+240 1輕 5DD 10罐 [20 開發]LV1 1SS 1輕
# 6~9HR:[36]LV30 2水母 1輕 1DD 2SS [19]LV20 2航戰 2DD 2SS
#常態任務
#_task_list = ((5, 4), (3, 4), (5, 5))
#高速任務
#_task_list = ((1, 6), (3, 5), (5, 6))
_task_list = ((1, 6), (1, 2), (5, 6))
#_task_list = ((1, 5), (3, 5), (5, 5))

#sleep
_sleep = (3, 7)

#delay task default(150sec)
min_delay = 30
delay_task = (120, 120, 120)
# don't need set this, is radom
_delay_task = [0, 0, 0]
# current place
_place = "port"
#screen offset
_offset = (7, 35)

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

def expedition_cmd(team, (area, no)):
	u.focus_screen()
	u._sleep(3.0)
	# wellcome back
	auto_cmd("place p")
	auto_cmd("poi")
	auto_cmd("go")
	auto_cmd("home")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")
	u._sleep(4.0)
	auto_cmd("poi")
	auto_cmd("poi")

	#refill
	u._sleep(2.0)
	auto_cmd("go")
	auto_cmd("place r")
	auto_cmd("enter")
	auto_cmd("f1")
	auto_cmd("all")
	auto_cmd("f2")
	auto_cmd("all")
	auto_cmd("f3")
	auto_cmd("all")
	auto_cmd("f4")
	auto_cmd("all")
	auto_cmd('f' + str(team + 1))
	auto_cmd("all")
	u._sleep(2.0)
	auto_cmd("place p")
	auto_cmd("home")
	auto_cmd("go")
	auto_cmd("place r")
	auto_cmd("enter")
	auto_cmd("f1")
	auto_cmd("all")
	auto_cmd("f2")
	auto_cmd("all")
	auto_cmd("f3")
	auto_cmd("all")
	auto_cmd("f4")
	auto_cmd("all")
	auto_cmd('f' + str(team + 1))
	auto_cmd("all")

	#expedition
	u._sleep(4.0)
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
	u._sleep(5.0)
	auto_cmd("place p")
	auto_cmd("home")
	auto_cmd("go")
	auto_cmd("home")
	auto_cmd("poi")

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
			now_time = time.strftime("(%a)%X", time.localtime())
			now_hour = datetime.datetime.now().hour
			
			if(now_hour > _sleep[0] and now_hour <= _sleep[1]):
				show_msg = colored("電：自動遠征は休憩中です ", "green")
				show_msg += colored(_sleep[1], "yellow") + colored("時に続きます ", "green")
				show_msg += colored("今:", "green") + colored(now_time, "yellow")
				print_oneline(show_msg)	
			else:
				e_task()
			
			time.sleep(1)
		except KeyboardInterrupt:
			print colored("\n自動遠征が中断されました", "red")
			e_flag = False

def e_task():
	files = getJsonList()

	show_msg = colored("電：任務中 ", "green")
	
	if files:
		update_time = time.strftime("(%a)%H:%M ", time.localtime(os.path.getmtime(files[0])))

		data = read_port(files[0])
		show_msg += expedition_msg(data, 1)
		show_msg += expedition_msg(data, 2)
		show_msg += expedition_msg(data, 3)
		show_msg += colored("更新:" , "green") + colored(update_time, "yellow")
	
	now_time = time.strftime("(%a)%X", time.localtime())
	show_msg += colored("今:", "green") + colored(now_time, "yellow")

	print_oneline(show_msg)
	
	if expedition_status(data, 1) is False:
		expedition_cmd(1, _task_list[0])
	
	if expedition_status(data, 2) is False:
		expedition_cmd(2, _task_list[1])
	
	if expedition_status(data, 3) is False:
		expedition_cmd(3, _task_list[2])

def getJsonList():
	g = glob
	files = sorted(g.glob('../logbook/json/*PORT.json'), key=os.path.getmtime, reverse = True)
	return files

def print_oneline(print_msg):
	sys.stdout.write("\r{}".format(print_msg))
	sys.stdout.flush()

def read_port(file_path):
	with open(file_path)as data_file:
		data = json.load(data_file)
	return data


def expedition_status(data, team):
	global _delay_task
	team_data = str(data["api_data"]["api_deck_port"][team]["api_mission"][2])[0:10]
	
	if _delay_task[team - 1] <= 1:
		_delay_task[team - 1] = min_delay + random.randint(0, delay_task[team - 1])

	if time.localtime(float(team_data) + _delay_task[team - 1]) > time.localtime():
		return True	
	else:
		_delay_task[team - 1] = min_delay + random.randint(0, delay_task[team - 1])
		return False

def expedition_msg(data, team):
	team_data = str(data["api_data"]["api_deck_port"][team]["api_mission"][2])[0:10]
	team_delay = "-" + str(_delay_task[team - 1]) + "s "
	team_time = time.strftime("(%a)%H:%M", time.localtime(float(team_data) + _delay_task[team - 1]))
	show_msg = colored(str(team + 1) + "番隊:", "green")
	
	if time.localtime(float(team_data) - 300) > (time.localtime()):
		show_msg += colored(team_time, "cyan") + team_delay
	elif time.localtime(float(team_data)) > (time.localtime(time.time())):
		show_msg += colored(team_time, "magenta") + team_delay
	else:
		show_msg += colored(team_time, "red") + team_delay

	return show_msg

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
	print colored("電：", "green") + cmd[0]
	click_point = (cmd[1][0] + _offset[0], cmd[1][1] + _offset[1])
	u.click_and_wait(click_point, cmd[2], _LAG)

def current_status():
	current_status = "電："
	current_status += " Place = " + colored(_place, "yellow")
	current_status += " Lag = " + colored(str(_LAG), "yellow")
	return current_status

main()
