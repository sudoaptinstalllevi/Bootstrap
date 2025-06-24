import customtkinter
import win32api
import win32con
import time
import threading
import pyautogui
import pygame
import ctypes
import os 

os.system("pip install customtkinter >nul 2>&1")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("800x465")
app.title("Bootstrap")
move_up_var = customtkinter.StringVar(value="20")
move_left_var = customtkinter.StringVar(value="20")
move_right_var = customtkinter.StringVar(value="20")
move_down_var = customtkinter.StringVar(value="24")
time_sleep_var = customtkinter.StringVar(value="0.0034")

controller = None
jitter_active = False

def mouse_motion():
    try:
        move_up = float(move_up_var.get())
        move_left = float(move_left_var.get())
        move_right = float(move_right_var.get())
        move_down = float(move_down_var.get())

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(move_right), int(move_down), 0, 0)
        time.sleep(0.0037)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(-move_left), int(-move_up), 0, 0)
    except:
        pass

def wait_for_controller():
    global controller
    while pygame.joystick.get_count() == 0:
        pygame.joystick.quit()
        pygame.joystick.init()
        time.sleep(1)
    controller = pygame.joystick.Joystick(0)
    controller.init()
    return controller

def start_jitter_logic():
    global controller, jitter_active
    try:
        pygame.init()
        pygame.joystick.init()
        controller = wait_for_controller()

        current_settings = (move_right_var.get(), move_left_var.get(), move_up_var.get(), move_down_var.get())
        
        while jitter_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if pygame.joystick.get_count() == 0:
                pygame.quit()
                return

            aim = controller.get_axis(4)
            shoot = controller.get_axis(4)

            if aim > 0.0 and shoot > 0.0:
                mouse_motion()

            updated_settings = (
                move_right_var.get(),
                move_left_var.get(),
                move_up_var.get(),
                move_down_var.get()
            )

            if updated_settings != current_settings:
                current_settings = updated_settings

            time.sleep(float(time_sleep_var.get()))
    except Exception as e:
        pass

def start_jitter():
    global jitter_active
    jitter_active = True
    threading.Thread(target=start_jitter_logic, daemon=True).start()

def stop_jitter():
    global jitter_active
    jitter_active = False

def load_from_file():
    try:
        with open("jitter.txt", "r") as file:
            read = file.read().split(",")
            values = tuple(map(float, read))
            move_up_var.set(str(values[0]))
            move_left_var.set(str(values[1]))
            move_right_var.set(str(values[2]))
            move_down_var.set(str(values[3]))
            time_sleep_var.set(str(values[4]))
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, r"Couldn't load jitter.txt, Make Sure Its In This Path C:\Users\YourHostName", "Not.Read", 0)

def save_example_file():
    pyautogui.press("win")
    pyautogui.write("notepad")
    time.sleep(0.6)
    pyautogui.press("enter")
    time.sleep(2.4)
    pyautogui.write("20,20,20,24,0.004")
    time.sleep(0.5)
    ctypes.windll.user32.MessageBoxW(0, "Name the file 'jitter.txt' to be able to run it later.", "jitter.txt", 0)

customtkinter.CTkLabel(app, text="Move Up").pack(pady=2)
customtkinter.CTkEntry(app, textvariable=move_up_var).pack()

customtkinter.CTkLabel(app, text="Move Left").pack(pady=2)
customtkinter.CTkEntry(app, textvariable=move_left_var).pack()

customtkinter.CTkLabel(app, text="Move Right").pack(pady=2)
customtkinter.CTkEntry(app, textvariable=move_right_var).pack()

customtkinter.CTkLabel(app, text="Move Down").pack(pady=2)
customtkinter.CTkEntry(app, textvariable=move_down_var).pack()

customtkinter.CTkLabel(app, text="Jitter Speed").pack(pady=2)
customtkinter.CTkEntry(app, textvariable=time_sleep_var).pack()

customtkinter.CTkButton(app, text="Start Jitter", command=start_jitter).pack(pady=6)
customtkinter.CTkButton(app, text="Stop Jitter", command=stop_jitter).pack(pady=6)

customtkinter.CTkButton(app, text="Load from jitter.txt", command=load_from_file).pack(pady=3)
customtkinter.CTkButton(app, text="Open Notepad Example", command=save_example_file).pack(pady=3)

app.mainloop()
