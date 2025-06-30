import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import ctypes
import time
import win32api
import win32con

os.system('cls')
want_to_fucking_jitter = 0x0001

pygame.init()
pygame.joystick.init()

need = pygame.joystick.Joystick(0)

print("""
 _______  ___  ___      ___       _______  ___      ___  __     
|   _  "\|"  \/"  |    |"  |     /"     "||"  \    /"  ||" \    
(. |_)  :)\   \  /     ||  |    (: ______) \   \  //  / ||  |   
|:     \/  \\  \/      |:  |     \/    |    \\  \/. ./  |:  |   
(|  _  \\  /   /        \  |___  // ___)_    \.    //   |.  |   
|: |_)  :)/   /        ( \_|:  \(:      "|    \\   /    /\  |\  
(_______/|___/          \_______)\_______)     \__/    (__\_|_) 
                                                                
""")

def fucking_shake():
    ctypes.windll.user32.mouse_event(want_to_fucking_jitter, 20, 20)
    time.sleep(0.0037)
    ctypes.windll.user32.mouse_event(want_to_fucking_jitter, -20, -20)
while True:
 pygame.event.pump()
 r6_mouse = win32api.GetAsyncKeyState(win32con.VK_RBUTTON)
 set_on_aim = need.get_axis(4)
 if set_on_aim > 0.0 or (r6_mouse):
    fucking_shake()
    time.sleep(0.0037)
