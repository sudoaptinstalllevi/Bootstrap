import os #line:1
import time #line:2
import pyautogui #line:4
import ctypes #line:5
"""Colors For Ui"""#line:6
BLACK ="\033[0;30m"#line:7
RED ="\033[0;31m"#line:8
GREEN ="\033[0;32m"#line:9
BROWN ="\033[0;33m"#line:10
BLUE ="\033[0;34m"#line:11
PURPLE ="\033[0;35m"#line:12
CYAN ="\033[0;36m"#line:13
LIGHT_GRAY ="\033[0;37m"#line:14
DARK_GRAY ="\033[1;30m"#line:15
LIGHT_RED ="\033[1;31m"#line:16
LIGHT_GREEN ="\033[1;32m"#line:17
YELLOW ="\033[1;33m"#line:18
LIGHT_BLUE ="\033[1;34m"#line:19
LIGHT_PURPLE ="\033[1;35m"#line:20
LIGHT_CYAN ="\033[1;36m"#line:21
LIGHT_WHITE ="\033[1;37m"#line:22
"""Colors For Ui"""#line:23
os .system ("cls")#line:24
print (f"{LIGHT_WHITE}By {LIGHT_BLUE}@yyLevi\033[0m")#line:25
time .sleep (2.8 )#line:26
os .system ("cls")#line:27
time .sleep (0.001 )#line:28
import os #line:29
import shutil #line:30
import time #line:31
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:32
import pygame #line:33
from colorama import Fore ,Style #line:34
os .system ('cls')#line:35
time .sleep (0.01 )#line:36
os .system ("cls")#line:37
os .system ('cls')#line:46
def main2 ():#line:47
 for OOOO0O00O000O000O in range (2 ):#line:48
  print (fr"""  {LIGHT_BLUE}                                                            
    ___    __                          
   /   |  / /______  ______  ____  ___ 
  / /| | / / ___/ / / / __ \/ __ \/ _ \
 / ___ |/ / /__/ /_/ / /_/ / / / /  __/
/_/  |_/_/\___/\__, /\____/_/ /_/\___/ 
              /____/""")#line:55
  O00O000OOO0OOOO00 =input (f"""\n{LIGHT_CYAN}['\033[0m{LIGHT_PURPLE}Enter Password To {LIGHT_CYAN}Access{LIGHT_PURPLE}:{YELLOW} """)#line:56
  if O00O000OOO0OOOO00 =="squ":#line:57
    print ("")#line:58
    break #line:59
  else :#line:60
    os .system ("cls")#line:61
    print (f"{LIGHT_CYAN}Wrong Password, \033[0m{LIGHT_WHITE}['{LIGHT_PURPLE}{1 - OOOO0O00O000O000O}{LIGHT_WHITE}'] \033[0m{LIGHT_PURPLE}Attempts Left Untill Exiting, Cracked Ascend")#line:62
 else :#line:63
    os .system ("cls")#line:64
    print (f"""{LIGHT_PURPLE}                     
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
| . | | | . | -_| | | -_|
|___|___|___|___|_  |___|
                |___|    

{LIGHT_BLUE}Used All Password Attempts...\n\033[0m""")#line:72
    time .sleep (2.1 )#line:73
    O00O000OOO0OOOO00 =quit (pyautogui .write ("exit"),pyautogui .press ("enter"))#line:74
main2 ()#line:76
def clear_screen ():#line:77
    O0OO00O00OOO0O00O ='cls'if os .name =='nt'else 'clear'#line:78
    os .system (O0OO00O00OOO0O00O )#line:79
def get_terminal_width ():#line:80
    return shutil .get_terminal_size ().columns #line:81
def color_text (O00O0000000O0O0OO ,color =Fore .WHITE ):#line:82
    O00O0000000OO0OOO =O00O0000000O0O0OO .split ('\n')#line:83
    OO0O0000OOOO00OOO =get_terminal_width ()#line:84
    OO00000O0OOO0O000 =[color +O0O0O0O0OO0000O00 .center (OO0O0000OOOO00OOO )+Style .RESET_ALL for O0O0O0O0OO0000O00 in O00O0000000OO0OOO ]#line:85
    return '\n'.join (OO00000O0OOO0O000 )#line:86
def center_text (OOOOO0O00OOOO0OOO ):#line:87
    OOO000OO00OO0OOOO =shutil .get_terminal_size ().columns #line:88
    OO00OO0O0O0OOO0O0 =[OO0OOO0000OO00OOO .center (OOO000OO00OO0OOOO )for OO0OOO0000OO00OOO in OOOOO0O00OOOO0OOO .split ('\n')]#line:89
    return '\n'.join (OO00OO0O0O0OOO0O0 )#line:90
def load_settings ():#line:91
    os .system ("cls")#line:92
    print (f"{LIGHT_BLUE}[1] Default Jitter")#line:93
    print (f"{LIGHT_GREEN}[2] Make Your Own Jitter")#line:94
    print (f"{LIGHT_PURPLE}[3] Use Your jitter.txt")#line:95
    print (f"{LIGHT_CYAN}[4] Example How To Make Your Own Jitter")#line:96
    O0O0O0OO0O0O0O0O0 =input (f"\n{PURPLE}Enter Your Choice Of Jitter_. ")#line:97
    os .system ("cls")#line:98
    if O0O0O0OO0O0O0O0O0 =="1":#line:99
     return (20 ,20 ,20 ,20 ,0.0034 )#line:100
    elif O0O0O0OO0O0O0O0O0 =="3":#line:101
     try :#line:102
      with open ("jitter.txt","r")as O000O0000OOOOO000 :#line:103
        O00OO0OO0000OOO0O =O000O0000OOOOO000 .read ().split (",")#line:104
        return tuple (map (float ,O00OO0OO0000OOO0O ))#line:105
     except :#line:106
      pass #line:107
      return load_settings ()#line:108
    elif O0O0O0OO0O0O0O0O0 =="4":#line:109
     pyautogui .press ("win")#line:110
     pyautogui .write ("notepad")#line:111
     time .sleep (0.6 )#line:112
     pyautogui .press ("enter")#line:113
     time .sleep (2.4 )#line:114
     pyautogui .write ("20,20,20,24,0.0034")#line:115
     time .sleep (0.55 )#line:116
     ctypes .windll .user32 .MessageBoxW (0 ,"Name Of .TXT Must Be, jitter.txt To Be Able To Run","jitter.txt",0 )#line:117
     return load_settings ()#line:118
    elif O0O0O0OO0O0O0O0O0 =="2":#line:119
     while True :#line:120
      try :#line:121
       OOOO0O0O00O0O00O0 =float (input (f"{LIGHT_BLUE}enter any number to move the mouse up etc. 20: You're Choice "))#line:122
       OO0O00O0OOO00OOO0 =float (input (f"{LIGHT_GREEN}enter any number to move the mouse left etc. 20: You're Choice "))#line:123
       OO0O0O0OOOOOOO0OO =float (input (f"{LIGHT_PURPLE}enter any number to move the mouse right etc. 20: You're Choice "))#line:124
       O0OO0OOO0OO000O00 =float (input (f"{LIGHT_CYAN}enter any number to move the mouse down etc. 24: You're Choice "))#line:125
       O0000OOO00O00OO0O =float (input (f"{YELLOW}enter the speed of how fast the jitter goes, etc. 0.004: You're Choice "))#line:126
       return OOOO0O0O00O0O00O0 ,OO0O00O0OOO00OOO0 ,OO0O0O0OOOOOOO0OO ,O0OO0OOO0OO000O00 ,O0000OOO00O00OO0O #line:127
      except ValueError :#line:128
         print ("restarting wrong input.")#line:129
         time .sleep (1.2 )#line:130
         os .system ("cls")#line:131
def display_banner (O0OO00O000O000O00 ,OOO00OOOOO00OOOO0 ,OOO0OO0OOO00O0OO0 ,O0O00O0000000OO0O ):#line:133
  print (fr"""  {LIGHT_BLUE}                                                            
                                         ___    __                          
                                        /   |  / /______  ______  ____  ___ 
                                       / /| | / / ___/ / / / __ \/ __ \/ _ \
                                      / ___ |/ / /__/ /_/ / /_/ / / / /  __/
                                     /_/  |_/_/\___/\__, /\____/_/ /_/\___/ 
                                                   /____/ """)#line:140
def controller_call ():#line:141
    OO0O0000O0OO0OO00 =0x0001 #line:142
    ctypes .windll .user32 .mouse_event (OO0O0000O0OO0OO00 ,int (move_left ),int (move_down ),24 ,24 )#line:143
    time .sleep (0.0037 )#line:144
    ctypes .windll .user32 .mouse_event (OO0O0000O0OO0OO00 ,int (-move_right ),int (-move_up ),-24 ,-24 )#line:145
def monitor_settings (O000OO00OOOO00OOO ):#line:147
    return O000OO00OOOO00OOO #line:148
def wait_for_controller ():#line:149
    while pygame .joystick .get_count ()==0 :#line:150
        clear_screen ()#line:151
        display_banner (move_right ,move_left ,move_up ,move_down )#line:152
        time .sleep (1 )#line:153
        pygame .joystick .quit ()#line:154
        pygame .joystick .init ()#line:155
    OOO0OOOO0OOO0OOOO =pygame .joystick .Joystick (0 )#line:156
    OOO0OOOO0OOO0OOOO .init ()#line:157
    clear_screen ()#line:158
    display_banner (move_right ,move_left ,move_up ,move_down )#line:159
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             {LIGHT_CYAN}LT + LR{LIGHT_WHITE} or {LIGHT_PURPLE}L1 + L2\033[0m")#line:160
    print (f"\n{LIGHT_WHITE}                                                 Project By \033[1;32m@yyLevi\033[0m")#line:161
    print (f"                                                ['{YELLOW}Jitter Activated'\033[0m]")#line:162
    return OOO0OOOO0OOO0OOOO #line:163
try :#line:164
 move_right ,move_left ,move_up ,move_down ,time_sleep =load_settings ()#line:165
 current_settings =(move_right ,move_left ,move_up ,move_down )#line:166
 pygame .init ()#line:167
 pygame .joystick .init ()#line:168
 controller =wait_for_controller ()#line:169
 while True :#line:170
    for event in pygame .event .get ():#line:171
      if pygame .joystick .get_count () > 0 :#line:175
       aim =controller .get_axis (4 )#line:178
       shoot =controller .get_axis (4 )#line:179
       if aim >0.0 and shoot >0.0 :#line:180
        controller_call ()#line:181
       if int (time .time ())%0.1 ==0 :#line:182
        updated_settings =monitor_settings (current_settings )#line:183
       if updated_settings !=current_settings :#line:184
            move_right ,move_left ,move_up ,move_down =updated_settings #line:185
            current_settings =updated_settings #line:186
            display_banner (move_right ,move_left ,move_up ,move_down )#line:187
      time .sleep (time_sleep )#line:188
except KeyboardInterrupt :#line:189
 os .system ("cls")
