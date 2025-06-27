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
import time #line:31
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:32
import pygame #line:33
os .system ("cls")#line:37

def reload():
   os.system("cls")

def load_settings ():#line:91
    os .system ("cls")#line:92
    print (f"{LIGHT_BLUE}[1] Default Jitter")#line:93
    print (f"{LIGHT_GREEN}[2] Make Your Own Jitter")#line:94
    print (f"{LIGHT_PURPLE}[3] Use Your jitter.txt")#line:95
    print (f"{LIGHT_CYAN}[4] Example How To Make Your Own Jitter")#line:96
    print(f"{LIGHT_WHITE}Quick tip, pressing {LIGHT_GREEN}ctrl+c{LIGHT_WHITE} in the jitter screen will bring you back here.")
    O0O0O0OO0O0O0O0O0 =input (f"\n{LIGHT_PURPLE}Enter Your Choice Of Jitter{YELLOW}__>__ {LIGHT_CYAN} ")#line:97
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
def banner():#line:133
  print (fr"""  {LIGHT_BLUE}                                                            
                                         ___    __                          
                                        /   |  / /______  ______  ____  ___ 
                                       / /| | / / ___/ / / / __ \/ __ \/ _ \
                                      / ___ |/ / /__/ /_/ / /_/ / / / /  __/
                                     /_/  |_/_/\___/\__, /\____/_/ /_/\___/ 
                                                   /____/ """) 
def controller_call ():#line:141
    OO0O0000O0OO0OO00 =0x0001 #line:142
    ctypes.windll.user32.mouse_event(OO0O0000O0OO0OO00 ,int (move_left ),int (move_down ),24 ,24 )#line:143
    time .sleep (0.0037 )#line:144
    ctypes.windll.user32.mouse_event(OO0O0000O0OO0OO00 ,int (-move_right ),int (-move_up ),-24 ,-24 )#line:145
def monitor_settings (O000OO00OOOO00OOO ):#line:147
    return O000OO00OOOO00OOO #line:148
def wait_for_controller ():#line:149
    while pygame .joystick .get_count ()==0 :#line:150
        time .sleep (0.7 )#line:153
        pygame .joystick .quit ()#line:154
        pygame .joystick .init ()#line:155
    OOO0OOOO0OOO0OOOO =pygame .joystick .Joystick (0 )#line:156
    OOO0OOOO0OOO0OOOO .init ()#line:157
    os.system("cls")
    banner()
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             {LIGHT_CYAN}LT + LR{LIGHT_WHITE} or {LIGHT_PURPLE}L1 + L2\033[0m")#line:160
    print (f"\n{LIGHT_WHITE}                                                 Project By \033[1;32m@yyLevi\033[0m")#line:161
    print (f"                                                ['{YELLOW}Jitter Activated'\033[0m]")#line:162
    print(f"\n{LIGHT_WHITE} Reminder {LIGHT_PURPLE}ctrl+c {LIGHT_WHITE}will bring you back to main menu")
    return OOO0OOOO0OOO0OOOO #line:163
while True:
    try:
        move_right, move_left, move_up, move_down, time_sleep = load_settings() # i fucking hate indents in python
        current_settings = (move_right, move_left, move_up, move_down)
        pygame.init()
        pygame.joystick.init()
        controller = wait_for_controller()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            if pygame.joystick.get_count() == 0:
                pygame.quit()
                exit()
            aim = controller.get_axis(4)
            shoot = controller.get_axis(4)
            if aim > 0.0 and shoot > 0.0:
                controller_call()
            if int(time.time()) % 2 == 0:
                updated_settings = monitor_settings(current_settings)
                if updated_settings != current_settings:
                    move_right, move_left, move_up, move_down = updated_settings
                    current_settings = updated_settings
            time.sleep(time_sleep)
    except KeyboardInterrupt:
       print("\n")
