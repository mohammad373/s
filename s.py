# s
import os
import time
import sys
import requests
from colorama import Fore
os.system("clear")
def __name__():


        print(Fore.BLUE + "Hello . Welcome Back" + Fore.YELLOW + " ;)")
        time.sleep(2)
        target = input(Fore.RED + "Enter Your Address Target" + Fore.YELLOW + " ==>  ")
        time.sleep(1.3)
        
        if target == "" or None :
            try:
                print(Fore.RED + "Error : This Is None" + Fore.YELLOW + " ;( ")
                time.sleep(1.3)
                sys.exit()
            except:
                pass
        r = requests.get("http://" + target + "/wp-content/plugins/")
        if r.status_code == 404 or r.status_code == 500:
            print(Fore.RED + f"Your Target Is Not WordPress : {target}" + Fore.YELLOW + " ;( ")
        else:
            print(Fore.GREEN + f"Your Target Is WordPresss : {target}" + Fore.YELLOW + " ;) ")

__name__()
