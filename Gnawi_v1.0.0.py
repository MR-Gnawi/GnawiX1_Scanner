import requests
from termcolor import colored

def banner():
    print(colored("-----------------------------------",'red', attrs=['bold']))
    print(colored("|||          GnawiX1            |||" ,'blue', attrs=['bold'])) 
    print(colored("-----------------------------------", 'red',  attrs=['bold']))
banner()
def main():
    try:
        Domain = input(colored("""Enter To Domain (Example >> "example.com") """ , 'blue' , attrs=['bold']))
        x = colored("Hello " , 'red')
        page = f"https://{Domain}/robots.txt"
        req = requests.get(page).text  
        print(req)
        
        print(colored("Save File >> " + Domain + "_robots.txt",'yellow', attrs=['bold']))
        fa = open(f"{Domain}_robots.txt","w")
        fa.write(req)
        fa.close     
    except requests.exceptions.ConnectionError as err1:
        print(err1) 
        main()
    except KeyboardInterrupt as err2:
        print(err2)
main()
