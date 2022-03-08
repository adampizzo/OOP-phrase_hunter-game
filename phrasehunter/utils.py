import os
import sys
import time


def s_sleep():
    time.sleep(.25)
    
def m_sleep():
    time.sleep(1)
    
def l_sleep():
    time.sleep(3)
    
def s_clear():
    ''' The purpose of the clear function is to determine what the
        operating system and then clear the screen.'''
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
