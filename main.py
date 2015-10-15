# encoding: utf-8
from colorama import init
from termcolor import colored
init()

def main():
    # init something
    # ...
    while True:
        _user_input = raw_input(colored('電：ご命令を', 'green') + ">")
        if is_handled_by_predefined_func(_user_input) is True:
            continue
        check_command(_user_input)

def is_handled_by_predefined_func(input_cmd):
    if input_cmd == 'cmd':
        return False
    else:
        print input_cmd + ' is not defined'
        return True

def check_command(input_cmd):
    print input_cmd

main()
