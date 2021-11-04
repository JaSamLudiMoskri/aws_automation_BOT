#!/usr/bin/env python
from subprocess import call
import os
import logging
import subprocess
import cowsay
from colorama import Fore


try:
    cowsay.cow('Welcome user.')
    print(Fore.BLUE , 'THIS SOFTWARE WILL ENABLE YOU TO CONTROL YOUR AWS SERVICES WHILE NOT LEAVING YOUR TERMINAL.\n\n')
    print(Fore.RED , '-----------------------------------------ATTENTION!-----------------------------------------')
    print(Fore.MAGENTA,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    pick = input(' TO RUN PROGRAM ENTER run,IF YOU WANT TO SEE LIST OF ALL COMMANDS YOU CAN RUN ENTER help: ')
    
    
    cwd = (os.path.dirname(os.path.realpath(__file__)))
    os.chdir(cwd + '/Services')

    if pick == 'run':
        print(Fore.RED,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('IF YOU ENTER COMMAND THAT DOES NOT EXISTS PROGRAM WILL AUTOMATICLY EXIT !!!')
        command = input("Please enter full, and correct name of command you want to run : ")
        print(Fore.WHITE ,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        call(["python" , "main.py" , "find_and_run_plugins" , command])

    elif pick == 'help':
        call(["python" , "main.py" , "cheat_sheat"])

except subprocess.CalledProcessError:
    logging.exception("Python can't open file. No such file or directory.")