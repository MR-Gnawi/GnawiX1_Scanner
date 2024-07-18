import requests
import os
from termcolor import colored

def banner():
    banner_text = """
-----------------------------------
|||                              |||
|||        GnawiX1 Scanner       |||
|||                              |||
-----------------------------------
"""
    print(colored("-----------------------------------", 'red', attrs=['bold']))
    print(colored("|||                              |||", 'cyan', attrs=['bold']))
    print(colored("|||", 'cyan', attrs=['bold']) + colored("        GnawiX1 Scanner       ", 'yellow', attrs=['bold']) + colored("|||", 'cyan', attrs=['bold']))
    print(colored("|||                              |||", 'cyan', attrs=['bold']))
    print(colored("-----------------------------------", 'red', attrs=['bold']))
    
def get_robots_txt(Domain):
    try:
        url = f"https://{Domain}/robots.txt"
        response = requests.get(url)
        return response.text # tete
    except requests.exceptions.ConnectionError as err1:
        print(colored(err1, 'red', attrs=['bold']))
    except requests.exceptions.HTTPError as err2:
        print(colored(err2, 'red', attrs=['bold']))
def save_robots_txt(Domain,tete):
    mkdir = os.mkdir(Domain)
    cd = os.chdir(Domain)
    filename = f"{Domain}_robots.txt"    
    with open(filename , 'w') as file:
        file.write(tete)
    print(colored(f"Save File >> {Domain}",'yellow', attrs=['bold']))
def main():
    banner()
    while True:
        try:
            domain = input(colored("Enter the domain (e.g., 'example.com'): ", 'blue', attrs=['bold']))
            tete = get_robots_txt(domain)
            if tete:
                print(tete)
                save_robots_txt(domain,tete)
                break
        except KeyboardInterrupt as err1:
            print(err1)
            break
if __name__ == "__main__":
    main()
