import requests
from termcolor import colored

print(colored("-----------------------------------", 'green'))
print(colored("|||         Gnawi_v1.0.0         |||", 'green'))
print(colored("-----------------------------------", 'green'))

def main():
    try:
        Domain = input("""Enter To Domain (Example >> "example.com") : """)
        page = f"https://{Domain}/robots.txt"
        req = requests.get(page).text  
             
        print(req)
        
        print("Save File >> " + Domain + "_robots.txt")
        fa = open(f"{Domain}_robots.txt","w")
        fa.write(req)
        fa.close 
        
    except:
        print(f"""Error Domain Example "example.com" >>> """ + str(Domain))
       
        
main()
