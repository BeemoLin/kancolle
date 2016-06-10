# encoding: utf-8
import sys
import time
import datetime
import os
import glob
import json
import random
import subprocess
from pprint import pprint

# three party
from colorama import init
from termcolor import colored
#colored init
init()

#config import
import config

#auto combat
_sikuli_auto = False

#auto check fatigue
_fatigue_check = False

#auto combat check ndock
_ndock_check = False

_flag = True
# current place
_place = "port"

#check ndock type
_check_type = "all"

#click LAG
_LAG = config._LAG

#expedition_task
_task_list = config._task_list

#sleep
_sleep = config._sleep

#delay task default(150sec)
min_delay = config.min_delay
delay_task = config.delay_task
# don't need set this, is radom
_delay_task = config._delay_task

#screen offset
_offset = config._offset

#self model import
import Utility
import _command

u = Utility
c = _command

def main():
    # init something
    # ...
	while _flag:
		global data
		global body
		body = read_port('../poi/app_compiled/cache/START2.json')
		data = read_port('../poi/app_compiled/cache/PORT.json')
		_user_input = raw_input(colored("電：ご命令を", "green") + ">")
		if is_handled_by_predefined_func(_user_input) is True:
			continue

		check_command(_user_input)

def expedition_cmd(team, (area, no), come_back_team):
	u.focus_screen()
	u._sleep(3.0)
	
	print colored(team, "yellow") + colored("艦隊戻りました", "green")

	# wellcome back
	auto_cmd("place p")
	auto_cmd("poi")
	auto_cmd("go")
	auto_cmd("home")
	auto_cmd("poi")
	for r in range(come_back_team, 0, -1):
		for j in range(3, 0, -1):
			auto_cmd("poi")
		auto_cmd("place p")
		auto_cmd("poi")
		auto_cmd("go")
		auto_cmd("home")
		auto_cmd("poi")
	
	#refill
	if get_flag_ship_fuel(team) == False:
		auto_cmd("place p")
		auto_cmd("home")
		auto_cmd("poi")
		u._sleep(2.0)
		auto_cmd("go")
		auto_cmd("place r")
		auto_cmd("enter")
		auto_cmd('f' + str(team + 1))
		auto_cmd("all")
		auto_cmd("place p")
		auto_cmd("home")
		auto_cmd("poi")
		u._sleep(2.0)
	
	#expedition
	if get_flag_ship_fuel(team):
		auto_cmd("place p")
		auto_cmd("go")
		auto_cmd("place e")
		auto_cmd("enter")
		auto_cmd("e" + str(area))
		auto_cmd(str(no))
		auto_cmd("ok")
		auto_cmd("f" + str(team + 1))
		auto_cmd("start")

	#back home
	u._sleep(1.0)
	auto_cmd("place p")
	auto_cmd("home")
	auto_cmd("poi")
	auto_cmd("go")
	u._sleep(1.0)
	auto_cmd("home")
	auto_cmd("poi")


def is_handled_by_predefined_func(input_cmd):
	global _place
	global _flag
	global _sikuli_auto
	global _ndock_check
	global _fatigue_check
	global _check_type
	if input_cmd == "exit":
		_flag = False
		print colored("電：お疲れさまでした", "green")
		return True
	elif input_cmd == 'oil':
		get_flag_ship_fuel(1)
		get_flag_ship_fuel(2)
		get_flag_ship_fuel(3)
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
		return True

	elif input_cmd == 'dock all':
		_check_type = "all"
		print colored("明石 : あまり得意じゃないんだけど！", "green") 
		return True

	elif input_cmd == 'dock one':
		_check_type = "one"
		print colored("明石 : これは……はかどります！", "green") 
		return True

	#switch submarine
	elif input_cmd == 'ss':
		subprocess.call(['./submarine.sh'], shell=True)
		print colored(" 潜水艦 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == 'ssv':
		subprocess.call(['./submarine_air.sh'], shell=True)
		print colored(" 潜水空母 ", "yellow") + colored("出撃します！！", "green")
		return True

	#event spring 2016
	elif input_cmd == 'ee1':
		subprocess.call(['./E1.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" E1 I ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == 'ee3':
		subprocess.call(['./E3.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" E3 ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == 'ere3':
		subprocess.call(['./rE3.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" rE3 ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == 'ee5':
		subprocess.call(['./E5.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" E5 ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True

	elif input_cmd == 'pvp':
		subprocess.call(['./pvp.sh'], shell=True)
		print colored("伊401", "green") + colored(" pvp ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '11':
		subprocess.call(['./1-1.sh'], shell=True)
		print colored("伊401", "green") + colored(" 1-1 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '15':
		subprocess.call(['./1-5.sh'], shell=True)
		print colored("伊401", "green") + colored(" 1-5 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '22':
		subprocess.call(['./2-2.sh'], shell=True)
		print colored("伊401", "green") + colored(" 2-2 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '23':
		subprocess.call(['./2-3.sh'], shell=True)
		print colored("伊401", "green") + colored(" 2-3 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '24':
		subprocess.call(['./2-4.sh'], shell=True)
		print colored("伊401", "green") + colored(" 2-4 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '25':
		subprocess.call(['./2-5.sh'], shell=True)
		print colored("伊401", "green") + colored(" 2-5 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '321':
		subprocess.call(['./3-2.sh'], shell=True)
		print colored("伊401", "green") + colored(" 3-2-A ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '33':
		subprocess.call(['./3-3.sh'], shell=True)
		print colored("伊401", "green") + colored(" 3-3 ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '52rb':
		subprocess.call(['./5-2-b.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" 5-2 Boss ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == '54':
		subprocess.call(['./5-4.sh'], shell=True)
		print colored("伊401", "green") + colored(" 5-4-A ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '54ss':
		subprocess.call(['./5-4-b-ss.sh'], shell=True)
		print colored("伊401", "green") + colored(" 5-4 Boss(ss) ", "yellow") + colored("出撃します！！", "green")
		return True
	elif input_cmd == '321r':
		subprocess.call(['./r3-2.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" 3-2-A ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == '54r':
		subprocess.call(['./r5-4.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" 5-4-A ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == '54rb':
		subprocess.call(['./5-4-b.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" 5-4 Boss ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == '54rss':
		subprocess.call(['./5-4-b-rss.sh'], shell=True)
		print colored("伊401 : ふふーん♪", "green") + colored(" 5-4 Boss(ss) ", "yellow") + colored("伊400型の追撃はしつこいんだから！", "green")
		return True
	elif input_cmd == 'auto e':
		_sikuli_auto = False
		_ndock_check = False
		_fatigue_check = False
		auto_e()
		return True
	elif input_cmd == 'auto c':
		_ndock_check = False
		_fatigue_check = False
		auto_c()
		return True
	elif input_cmd == 'auto cf':
		_ndock_check = False
		_fatigue_check = True
		auto_c()
		return True
	elif input_cmd == 'auto cd':
		_ndock_check = True
		_fatigue_check = False
		auto_c()
		return True
	elif input_cmd == 'auto cfd':
		_ndock_check = True
		_fatigue_check = True
		auto_c()
		return True
	elif input_cmd == 'auto ec':
		_sikuli_auto = True
		_ndock_check = False
		_fatigue_check = False
		auto_e()
		return True
	elif input_cmd == 'auto ecf':
		_sikuli_auto = True
		_ndock_check = False
		_fatigue_check = True
		auto_e()
		return True
	elif input_cmd == 'auto ecd':
		_sikuli_auto = True
		_ndock_check = True
		_fatigue_check = False
		auto_e()
		return True
	elif input_cmd == 'auto':# full command
		_sikuli_auto = True
		_ndock_check = True
		_fatigue_check = True
		auto_e()
		return True
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

def auto_c():
	e_flag = True
	while(e_flag):
		try:
			combat()
		except KeyboardInterrupt:
			print colored("\n自動出撃が中断されました", "red")
			e_flag = False

def combat():
	kantai_status = True
	fatigue_status = True
	
	if _ndock_check:
		kantai_status = ndocks_status(data)

	if _fatigue_check:
		fatigue_status = get_kantai_cond(0)


	if kantai_status and fatigue_status:
		show_msg = colored("電：伊401出撃します！", "green")
		subprocess.call(['./kancolle-auto/run.sh'], shell=True)
	time.sleep(1)

def auto_e():
	e_flag = True
	while(e_flag):
		try:
			now_time = time.strftime("(%a)%X", time.localtime())
			now_hour = datetime.datetime.now().hour
			
			if(now_hour > _sleep[0] and now_hour < _sleep[1]):
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
	file_path = '../poi/app_compiled/cache/PORT.json'

	show_msg = colored("電：任務中 ", "green")
	
	update_time = time.strftime("(%a)%H:%M ", time.localtime(os.path.getmtime(file_path)))

	data = read_port(file_path)
	show_msg += expedition_msg(data, 1)
	show_msg += expedition_msg(data, 2)
	show_msg += expedition_msg(data, 3)
	show_msg += colored("更新:" , "green") + colored(update_time, "yellow")
	
	now_time = time.strftime("(%a)%X", time.localtime())
	show_msg += colored("今:", "green") + colored(now_time, "yellow")

	print_oneline(show_msg)
	
	come_back_team = 0
	come_back_team_id = -1

	if _task_list[0] != "":
		if expedition_status(data, 1) is False:
			come_back_team += 1
			come_back_team_id = 1
	if _task_list[1] != "":
		if expedition_status(data, 2) is False:
			come_back_team += 1
			come_back_team_id = 2
	if _task_list[2] != "":
		if expedition_status(data, 3) is False:
			come_back_team += 1
			come_back_team_id = 3

	if come_back_team > 0 and come_back_team_id != -1:
		expedition_cmd(come_back_team_id, _task_list[come_back_team_id - 1], come_back_team)
	else:
		if _sikuli_auto:
			combat()

def print_oneline(print_msg):
	sys.stdout.write("\r{}".format(print_msg))
	sys.stdout.flush()

def read_port(file_path):
	read_data = {}
	is_json = False

	while is_json == False:
		with open(file_path)as data_file:
			try: 
				read_data = json.load(data_file)
				is_json = True
			except:
				print colored("[error] read_port ", "red")
	return read_data

def get_flag_ship_fuel(team):
	data = read_port('../poi/app_compiled/cache/PORT.json')
	flag_ship_id = str(data["api_deck_port"][team]["api_ship"][0])
	ships = data["api_ship"]
	ship_api_id = -1
	ship_current_fuel = -1
	for ship in ships:
		if str(ship["api_id"]) == str(flag_ship_id):
			ship_api_id = ship["api_ship_id"]
			ship_current_fuel = ship["api_fuel"]

	max_fuel = -1
	ship_name = "nil"
	ship_info_list = body["api_mst_ship"]
	for ship_info in ship_info_list:
		if str(ship_info["api_id"]) == str(ship_api_id):
			max_fuel = ship_info["api_fuel_max"]
			ship_name = ship_info["api_name"].encode('utf-8')

	if ship_current_fuel / float(max_fuel) > 0.99:
		print str(team) + "番隊:" + ship_name + colored(" Refill done.", "green")
		return True
	else:
		print str(team) + "番隊:" + ship_name + colored(" Not refill yet.", "red")
		return False
	
def get_kantai_cond(team):
	file_path = "../poi/app_compiled/cache/PORT.json"
	data = read_port(file_path)
	update_time = os.path.getmtime(file_path)
	knatai = data["api_deck_port"][team]["api_ship"]
	ships = data["api_ship"]
	ship_current_cond = -1
	for knatai_ship in knatai:
		for ship in ships:
			if str(ship["api_id"]) == str(knatai_ship):
				temp_cond = 41 - ship["api_cond"]
				if temp_cond > ship_current_cond:
					ship_current_cond = temp_cond

	refill_cond_time = update_time + ship_current_cond * 1 * 60

	if ship_current_cond <= 0 or time.time() > refill_cond_time:
		print str(team) + "番隊:"  + colored(" cond good.", "green")
		return True
	else:
		print str(team) + "番隊:" + colored(" cond refill time : " + time.strftime("(%a)%H:%M", time.localtime(refill_cond_time)), "yellow")
		return False

def ndock_unused(data, dock):

	show_msg = colored("舞鶴の温泉 ", "green")
	for i in range(1, 5):
		repair_timeout = time.localtime(float(str(data["api_ndock"][i - 1]["api_complete_time"])[0:10]))
		if repair_timeout < time.localtime():
			show_msg += "第" + colored(str(i), "yellow") + "風呂:"
			show_msg += colored(" 使える ", "green")
		else:
			show_msg += "第" + colored(str(i), "yellow") + "風呂:"
			show_msg += time.strftime("(%a)%H:%M", repair_timeout)
			show_msg += colored(" 前使えない ", "red")

	print_oneline(show_msg)

	repair_timeout = time.localtime(float(str(data["api_ndock"][dock - 1]["api_complete_time"])[0:10]))

	if repair_timeout < time.localtime():
		return True
	else:
		return False

def ndocks_status(data):
	if _check_type == "one":
		if ndock_unused(data, 1) and ndock_unused(data, 2) and ndock_unused(data, 3) and ndock_unused(data, 4):
			return True
		else:
			return False
	if _check_type == "all":
		if ndock_unused(data, 1) or ndock_unused(data, 2) or ndock_unused(data, 3) or ndock_unused(data, 4):
			return True
		else:
			return False

def expedition_status(data, team):
	global _delay_task
	team_data = str(data["api_deck_port"][team]["api_mission"][2])[0:10]
	
	if _delay_task[team - 1] <= 1:
		_delay_task[team - 1] = min_delay + random.randint(0, delay_task[team - 1])

	if time.localtime(float(team_data) + _delay_task[team - 1]) > time.localtime():
		return True	
	else:
		_delay_task[team - 1] = min_delay + random.randint(0, delay_task[team - 1])
		return False

def expedition_msg(data, team):
	show_msg = ""
	if len(data["api_deck_port"]) > team:
		team_data = str(data["api_deck_port"][team]["api_mission"][2])[0:10]
		team_delay = "-" + str(_delay_task[team - 1]) + "s "
		team_time = time.strftime("(%a)%H:%M", time.localtime(float(team_data) + _delay_task[team - 1]))
		show_msg += colored(str(team + 1) + "番隊:", "green")
		
		if time.localtime(float(team_data) - 300) > (time.localtime()):
			show_msg += colored(team_time, "cyan") + team_delay
		elif time.localtime(float(team_data)) > (time.localtime(time.time())):
			show_msg += colored(team_time, "magenta") + team_delay
		else:
			show_msg += colored(team_time, "red") + team_delay
	else:
		show_msg += colored(str(team + 1) + "番隊:", "green")
		show_msg += colored("使えられない", "red")

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
