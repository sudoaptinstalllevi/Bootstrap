import ctypes
import time
import win32api
import win32con
import threading
want_to_fucking_jitter = 0x0001
import os
def scream():
 import time
 os.system("curl -L -o fred.mp3 https://github.com/sudoaptinstalllevi/Bootstrap/raw/refs/heads/main/fred.mp3 >nul 2>&1")
 time.sleep(10)
 while True:
  import pygame
  os.system("cls")
  pygame.mixer.init()
  pygame.mixer.music.load("fred.mp3")
  pygame.mixer.music.play()
  time.sleep(0.8)
print(fr"""
  _           _          
 | |__ _  _  | |_____ __ 
 | '_ \ || | | / -_) V / 
 |_.__/\_, | |_\___|\_/  
       |__/                                                                            
""")
def fucking_shake():
    ctypes.windll.user32.mouse_event(want_to_fucking_jitter, 20, 21)
    time.sleep(0.0033)
    ctypes.windll.user32.mouse_event(want_to_fucking_jitter, -20, -20)
def thread_it():
 while True:
  r6_mouse = win32api.GetAsyncKeyState(win32con.VK_RBUTTON)
  r7_mouse = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
  if r6_mouse and r7_mouse:
     fucking_shake()
     time.sleep(0.0035)
threading.Thread(target=scream, daemon=True).start()
thread_it()


 
