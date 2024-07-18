import requests
from termcolor import colored

def banner():
    print(colored("-----------------------------------",'red', attrs=['bold']))
    print(colored("|||          GnawiX1            |||" ,'blue', attrs=['bold'])) 
    print(colored("-----------------------------------", 'red',  attrs=['bold']))
def main():
    Exi_T = True
    loop = True
    while loop == True and Exi_T == True:
        try:
            Domain = input(colored("""Enter To Domain (Example >> "example.com") """ , 'blue' , attrs=['bold']))
            x = colored("Hello " , 'red')
            page = f"https://{Domain}/robots.txt"
            req = requests.get(page).text  
        except requests.exceptions.ConnectionError as err1:
            print(colored(err1 , 'red' , attrs=['bold']))
        except KeyboardInterrupt:
            Exi_T = False
        else:
            print(req)
            with open(f"{Domain}_robots.txt","w") as f:
                   f.write(req)
            print(colored("Save File >> " + Domain + "_robots.txt",'yellow', attrs=['bold']))
            loop = False
banner() 
main()
