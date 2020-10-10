from colorama import Fore, init, Style
import requests,os,threading, time,datetime,random

init(convert = True)
colortheme = "red"
count = int(0)
print(f"""
   {Fore.RED} ██╗    ██╗{Fore.GREEN}███████╗{Fore.RED}██████╗ {Fore.GREEN}██╗  ██╗{Fore.RED} ██████╗ {Fore.GREEN} ██████╗ {Fore.RED}██╗  ██╗    
    {Fore.RED}██║    ██║{Fore.GREEN}██╔════╝{Fore.RED}██╔══██╗{Fore.GREEN}██║  ██║{Fore.RED}██╔═══██╗{Fore.GREEN}██╔═══██╗{Fore.RED}██║ ██╔╝    
    {Fore.RED}██║ █╗ ██║{Fore.GREEN}█████╗  {Fore.RED}██████╔╝{Fore.GREEN}███████║{Fore.RED}██║   ██║{Fore.GREEN}██║   ██║{Fore.RED}█████╔╝     
   {Fore.RED} ██║███╗██║{Fore.GREEN}██╔══╝  {Fore.RED}██╔══██╗{Fore.GREEN}██╔══██║{Fore.RED}██║   ██║{Fore.GREEN}██║   ██║{Fore.RED}██╔═██╗     
   {Fore.RED} ╚███╔███╔╝{Fore.GREEN}███████╗{Fore.RED}██████╔╝{Fore.GREEN}██║  ██║{Fore.RED}╚██████╔╝{Fore.GREEN}╚██████╔╝{Fore.RED}██║  ██╗    
    {Fore.RED} ╚══╝╚══╝ {Fore.GREEN}╚══════╝{Fore.RED}╚═════╝ {Fore.GREEN}╚═╝  ╚═╝ {Fore.RED}╚═════╝ {Fore.GREEN} ╚═════╝ {Fore.RED}╚═╝  ╚═╝   
                                                                  
    {Fore.GREEN}███████╗{Fore.RED}██████╗ {Fore.GREEN} █████╗ {Fore.RED}███╗   ███╗{Fore.GREEN}███╗   ███╗{Fore.RED}███████╗{Fore.GREEN}██████╗   
    {Fore.GREEN}██╔════╝{Fore.RED}██╔══██╗{Fore.GREEN}██╔══██╗{Fore.RED}████╗ ████║{Fore.GREEN}████╗ ████║{Fore.RED}██╔════╝{Fore.GREEN}██╔══██╗  
    {Fore.GREEN}███████╗{Fore.RED}██████╔╝{Fore.GREEN}███████║{Fore.RED}██╔████╔██║{Fore.GREEN}██╔████╔██║{Fore.RED}█████╗  {Fore.GREEN}██████╔╝  
    {Fore.GREEN}╚════██║{Fore.RED}██╔═══╝ {Fore.GREEN}██╔══██║{Fore.RED}██║╚██╔╝██║{Fore.GREEN}██║╚██╔╝██║{Fore.RED}██╔══╝  {Fore.GREEN}██╔══██╗  
    {Fore.GREEN}███████║{Fore.RED}██║     {Fore.GREEN}██║  ██║{Fore.RED}██║ ╚═╝ ██║{Fore.GREEN}██║ ╚═╝ ██║{Fore.RED}███████╗{Fore.GREEN}██║  ██║  
    {Fore.GREEN}╚══════╝{Fore.RED}╚═╝     {Fore.GREEN}╚═╝  ╚═╝{Fore.RED}╚═╝     ╚═╝{Fore.GREEN}╚═╝     ╚═╝{Fore.RED}╚══════╝{Fore.GREEN}╚═╝  ╚═╝  
{Fore.RED}
""")
def sendtowebhook():
    global colortheme
    global count



   
    while True:

        while True:
            #lines = open('proxies.txt').read().splitlines() 
            #randomproxy =random.choice(lines)
            #proxy = randomproxy

            with open("messages.txt") as fr: 
                lines = fr.readlines() 
                random_line = random.choice(lines) if lines else None
            message = random_line
            with open("usernames.txt") as fr: 
                lines = fr.readlines() 
                random_line = random.choice(lines) if lines else None
            username = random_line
            with open("avatars.txt") as fr: 
                lines = fr.readlines() 
                random_line = random.choice(lines) if lines else None
            avat = random_line

            with open("webhooks.txt") as fr: 
                lines = fr.readlines() 
                random_line = random.choice(lines) if lines else None
            webhook = random_line



            data = {
                'content': message,
                'username': username,
                'avatar_url': avat
            }




            #proxies = {'http': 'http://%s' % (proxy)}    
            #kek = requests.post(webhook, data=data, proxies = proxies).status_code
            kek = requests.post(webhook, data=data).status_code
            if kek == 204:
                count = count + 1

                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                if colortheme == "red":
                    print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.YELLOW} Message Sent{Fore.WHITE} :{Fore.RED} {message.strip()} ")
                    colortheme = "e"
                else:
                    print(f"{Fore.GREEN}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.GREEN}]{Fore.YELLOW} Message Sent{Fore.WHITE} :{Fore.GREEN} {message.strip()}")
                    colortheme = "red"


            os.system(f"title github.com/kieronia/Webhook-Spammer // Messages Sent : [{count}]")
    #except:
    #    pass





        
threads = int(input(f"[!] How many threads?\n[>] "))
for x in range(threads):
    thread = threading.Thread(
        target=sendtowebhook(), args=(1,))
time.sleep(1)
thread.start()
