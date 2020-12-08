import os
import sys
import requests
import time
import socket
from colorama import Fore

os.system("clear")
def __target__():
        os.system("clear")
        time.sleep(Fore.RED + "Helloe . Welcome Back ;)")
        time.sleep(2)
        target = input(Fore.BLUE + "\nEnter Your Address Target" + Fore.YELLOW + " ==>  ")
        time.sleep(2)
        if target == "" or None :
            try:
                print(Fore.RED + "\n[!] - Error Your Target Is Not Found ;(")
                time.sleep(2)
                print(Fore.RED + "\n[*] - Ok Good Lunch ;)")
                time.sleep(2)
                # __________
                clear = int(input(Fore.YELLOW + "\n[!] - Your Sestem Is Clear 1 : Yes  2 : No  ==>  "))
                if clear == 1:
                    try:
                        print(Fore.YELLOW + "\n[!] - Ok Your System Thas 2 Sec Clear ;)")
                        time.sleep(2)
                        os.system("clear")
                        sys.exit()
                    except:
                        pass
                if clear == 2:
                    time.sleep(2)
                    print(Fore.YELLOW + "\n[+] - Ok Good Bay ;)")
            except:
                pass
        s = socket.gethostbyname(target))
        #r = requests.get("https://who.is/whois-ip/ip-address/"+ s).text
        r = "https://who.is/whois-ip/ip-address/" + s
        print(r)

__target__()
