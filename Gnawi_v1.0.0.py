import requests
import socket

def main():
    try:
        Domain = input("""Enter To DomainExample >> "facebook.com" : """)
        ip = socket.gethostbyname(Domain)
        page = f"https://{Domain}/robots.txt"
        req = requests.get(page).text  
        
        print(f"Ip Address in Site Web " + str(ip))
        fa = open(f"{Domain}_robots.txt","w")
        fa.write(ip + "\n" + req)
        fa.close 
    except:
        print(f"""Error Domain Example "facebook.com" >>> """ + str(Domain))
        main()
        
main()