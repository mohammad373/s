# s
import os
import time
import sys
import requests
from colorama import Fore
# os.system("clear")
def __name__():


        #print(Fore.BLUE + "Hello . Welcome Back" + Fore.YELLOW + " ;)")
        # m
        target = input(Fore.RED + "Enter Your Address Target" + For.YELLOW + " ==>  ")
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
            print(Fore.RED + "Your Target Is Not WordPress" + Fore.YELLOW + " ;( ")
        else:
            print(Fore.GREEN + "Your Target Is WordPresss" + Fore.YELLOW + " ;) ")

__name__()
