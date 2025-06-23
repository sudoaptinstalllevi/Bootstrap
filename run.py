import os #line:1
import time #line:2
import sys #line:3
import pyautogui
import ctypes
"""Colors For Ui"""#line:4
BLACK ="\033[0;30m"#line:5
RED ="\033[0;31m"#line:6
GREEN ="\033[0;32m"#line:7
BROWN ="\033[0;33m"#line:8
BLUE ="\033[0;34m"#line:9
PURPLE ="\033[0;35m"#line:10
CYAN ="\033[0;36m"#line:11
LIGHT_GRAY ="\033[0;37m"#line:12
DARK_GRAY ="\033[1;30m"#line:13
LIGHT_RED ="\033[1;31m"#line:14
LIGHT_GREEN ="\033[1;32m"#line:15
YELLOW ="\033[1;33m"#line:16
LIGHT_BLUE ="\033[1;34m"#line:17
LIGHT_PURPLE ="\033[1;35m"#line:18
LIGHT_CYAN ="\033[1;36m"#line:19
LIGHT_WHITE ="\033[1;37m"#line:20
"""Colors For Ui"""#line:21
os .system ("cls")#line:22
print (f"{LIGHT_PURPLE}By {LIGHT_WHITE}@yyLevi\033[0m")#line:23
time .sleep (3.7 )#line:24
os .system ("cls")#line:25
time .sleep (0.001 )#line:42
import os #line:43
import shutil #line:44
import time #line:45
import win32api #line:46
import win32con #line:47
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:48
import pygame #line:49
from colorama import Fore ,Style #line:50
os .system ('cls')#line:51
time .sleep (0.01 )#line:70
os .system ("cls")#line:71
def loading ():#line:72
 OO0OOO0O0OOOO0O0O =['/','-','\\','|']#line:73
 for O0OO0OO00O00OO00O in range (3 ):#line:74
  for O0000OO0O000O000O in OO0OOO0O0OOOO0O0O :#line:75
     sys .stdout .write (f'\r{LIGHT_CYAN}Loading{LIGHT_WHITE} Please Wait{LIGHT_CYAN}...  {LIGHT_PURPLE}{O0000OO0O000O000O}')#line:76
     sys .stdout .flush ()#line:77
     time .sleep (0.01 )#line:78
loading ()#line:79
os .system ('cls')#line:85
def main2 ():#line:86
 for O0OOO00O00O00OO0O in range (2 ):#line:87
  print (fr"""  {LIGHT_BLUE}                                                            
    ___    __                          
   /   |  / /______  ______  ____  ___ 
  / /| | / / ___/ / / / __ \/ __ \/ _ \
 / ___ |/ / /__/ /_/ / /_/ / / / /  __/
/_/  |_/_/\___/\__, /\____/_/ /_/\___/ 
              /____/""")#line:92
  O000O0O0000OO0OOO =input (f"""\n{LIGHT_CYAN}['\033[0m{LIGHT_PURPLE}Enter Password To {LIGHT_CYAN}Access{LIGHT_PURPLE}:{YELLOW} """)#line:94
  if O000O0O0000OO0OOO =="1":#line:95
    print ("")#line:96
    break #line:97
  else :#line:98
    os .system ("cls")#line:99
    print (f"{LIGHT_CYAN}Wrong Password, \033[0m{LIGHT_WHITE}['{LIGHT_PURPLE}{1 - O0OOO00O00O00OO0O}{LIGHT_WHITE}'] \033[0m{LIGHT_PURPLE}Attempts Left Untill Exiting, Cracked Ascend")#line:100
 else :#line:101
    os .system ("cls")#line:102
    print (f"""{LIGHT_GREEN}                     
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
{LIGHT_CYAN}| . | | | . | -_| | | -_|
{LIGHT_PURPLE}|___|___|___|___|_  |___|
                |___|    

{LIGHT_WHITE}Used All Password Attempts...\n""")#line:110
    time .sleep (2.1 )#line:111
    O000O0O0000OO0OOO =quit ()#line:112
main2 ()#line:113
def clear_screen ():#line:114
    OO0O00O000O00O000 ='cls'if os .name =='nt'else 'clear'#line:115
    os .system (OO0O00O000O00O000 )#line:116
def get_terminal_width ():#line:117
    return shutil .get_terminal_size ().columns #line:118
def color_text (OO00OO0OOOOOO0O0O ,color =Fore .WHITE ):#line:119
    OO00000O00OOO0O00 =OO00OO0OOOOOO0O0O .split ('\n')#line:120
    O000O000O0O0O0000 =get_terminal_width ()#line:121
    O00OO00OOO0O00OOO =[color +OO0OO0OOO00O0OO00 .center (O000O000O0O0O0000 )+Style .RESET_ALL for OO0OO0OOO00O0OO00 in OO00000O00OOO0O00 ]#line:122
    return '\n'.join (O00OO00OOO0O00OOO )#line:123
def center_text (O00O00O0O0000O00O ):#line:124
    OOOO0OOO0O0OOOOOO =shutil .get_terminal_size ().columns #line:125
    OO0O000O0O0O000OO =[OO0OOO000O00OOO0O .center (OOOO0OOO0O0OOOOOO )for OO0OOO000O00OOO0O in O00O00O0O0000O00O .split ('\n')]#line:126
    return '\n'.join (OO0O000O0O0O000OO )#line:127
def load_settings ():#line:128
    os .system ("cls")#line:129
    print(f"{LIGHT_BLUE}[1] Use Zero Recoil Jitter")
    print(f"{LIGHT_GREEN}[2] Enter You're Own Jitter With No .TXT")
    print(f"{LIGHT_PURPLE}[3] Put You're Jitter File Here To Use")
    print(f"{LIGHT_CYAN}[4] Example How To Make You're Own Jitter")
    choice = input(f"\n{PURPLE}Enter Your Choice Of Jitter_. ")
    os.system("cls")
    if choice == "1":
     return(20,20,20,24,0.004)     
    elif choice == "3":
     try:
      with open("jitter.txt", "r") as file:
        read = file.read().split(",")
        return tuple(map(float, read))
     except:
      pass
      return load_settings()
    elif choice == "4":
     pyautogui.press("win")
     pyautogui.write("notepad")
     time.sleep(0.6)
     pyautogui.press("enter")
     time.sleep(2.4)
     pyautogui.write("20,20,20,24,0.004")
     time.sleep(0.55)
     ctypes.windll.user32.MessageBoxW(0, "Name Of .TXT Must Be, jitter.txt To Be Able To Run", "jitter.txt", 0)
     return load_settings()
    elif choice == "2":
     while True:
      try:
       move_up = float(input(f"{LIGHT_BLUE}enter any number to move the mouse up etc. 20: You're Choice "))
       move_left = float(input(f"{LIGHT_GREEN}enter any number to move the mouse left etc. 20: You're Choice ")) 
       move_right = float(input(f"{LIGHT_PURPLE}enter any number to move the mouse right etc. 20: You're Choice "))
       move_down = float(input(f"{LIGHT_CYAN}enter any number to move the mouse down etc. 24: You're Choice "))
       time_sleep = float(input(f"{YELLOW}enter the speed of how fast the jitter goes, etc. 0.004: You're Choice "))
       return move_up, move_left, move_right, move_down, time_sleep
      except ValueError:
         print("restarting wrong input.")
         time.sleep(1.2)
         os.system("cls")

def display_banner (O0OOOOOOO00O00OOO ,O0O00OOO0OOOO00OO ,O00O00000O0O00000 ,O0OO000OOO0000000 ):#line:137
  print (fr"""  {LIGHT_BLUE}                                                            
                                         ___    __                          
                                        /   |  / /______  ______  ____  ___ 
                                       / /| | / / ___/ / / / __ \/ __ \/ _ \
                                      / ___ |/ / /__/ /_/ / /_/ / / / /  __/
                                     /_/  |_/_/\___/\__, /\____/_/ /_/\___/ 
                                                   /____/ """)#line:142
def mouse_motion ():#line:144
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE, int(move_right) ,int(move_down), 29 ,29 )#line:145
    time .sleep (0.0037 )#line:146
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE, int(-move_left), int(-move_up) ,-29 ,-29 )#line:147
def monitor_settings (O0O0OO00O0OO00OOO ):#line:148
    return O0O0OO00O0OO00OOO #line:149
def wait_for_controller ():#line:150
    while pygame .joystick .get_count ()==0 :#line:151
        clear_screen ()#line:152
        display_banner (move_right ,move_left ,move_up ,move_down )#line:153
        time .sleep (1 )#line:154
        pygame .joystick .quit ()#line:155
        pygame .joystick .init ()#line:156
    O00OOO00OOO00OO00 =pygame .joystick .Joystick (0 )#line:157
    O00OOO00OOO00OO00 .init ()#line:158
    clear_screen ()#line:159
    display_banner (move_right ,move_left ,move_up ,move_down )#line:160
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             {LIGHT_CYAN}LT + LR{LIGHT_WHITE} or {LIGHT_PURPLE}L1 + L2\033[0m")#line:161
    print (f"\n{LIGHT_WHITE}                                                 Project By \033[1;32m@yyLevi\033[0m")#line:162
    print (f"                                                ['{YELLOW}Jitter Activated'\033[0m]")#line:163
    return O00OOO00OOO00OO00 #line:164
try :#line:165
 move_right ,move_left ,move_up ,move_down ,time_sleep =load_settings ()#line:166
 current_settings =(move_right ,move_left ,move_up ,move_down )#line:167
 pygame .init ()#line:168
 pygame .joystick .init ()#line:169
 controller =wait_for_controller ()#line:170
 while True :#line:171
    for event in pygame .event .get ():#line:172
        if event .type ==pygame .QUIT :#line:173
            pygame .quit ()#line:174
            exit ()#line:175
    if pygame .joystick .get_count ()==0 :#line:176
        pygame .quit ()#line:177
        exit ()#line:178
    aim =controller .get_axis (4 )#line:179
    shoot =controller .get_axis (4 )#line:180
    if aim >0.0 and shoot >0.0 :#line:181
        mouse_motion ()#line:182
    if int (time .time ())%2 ==0 :#line:183
        updated_settings =monitor_settings (current_settings )#line:184
        if updated_settings !=current_settings :#line:185
            move_right ,move_left ,move_up ,move_down =updated_settings #line:186
            current_settings =updated_settings #line:187
            display_banner (move_right ,move_left ,move_up ,move_down )#line:188
    time .sleep (time_sleep )#line:189
except KeyboardInterrupt :#line:190
 print ()
