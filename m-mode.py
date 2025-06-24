import os 

start_monitor_mode = "sudo airmon-ng start wlan0"
os.system(start_monitor_mode)

kill_process = "sudo airmon-ng check kill"
os.system(kill_process)

auto_airodump = "sudo airodump-ng wlan0"
os.system(auto_airodump)
