from urllib.request import Request, urlopen
from datetime import datetime
import time
import os
import json

path_log = os.path.dirname(os.path.abspath(__file__))
path_log = path_log.replace("tools", "")
path_log = fr'''{path_log}\json\url.json'''

f = open(path_log,)
data = json.load(f)
url_raw = data["url_raw"]


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    data = urlopen(Request(url_raw)).read().decode()
    print(f"[{current_time}]: API data: {data}")
    time.sleep(2)

