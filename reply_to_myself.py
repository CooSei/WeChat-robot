import os
import time
import cv2
from pymouse import *
import itchat
m = PyMouse()
def reply_to_filehelper(message):
   
    if message == "1": 
        os.system('shutdown -s -t 30')
    elif message == "2":
        os.system('shutdown -a')
    elif message == "3":#此处为电脑WiFi，仅我的电脑有用
        m.click(1180, 745)
        time.sleep(3)
        m.click(1243,679)
        m.click(1243,690)
    elif message == "4":
        cap=cv2.VideoCapture(0)
        ret,img =cap.read()
        cv2.imwrite("weixinTemp.jpg",img)
        itchat.send('@img@%s'%u'weixinTemp.jpg','filehelper')
        cap.release()
    elif message == '5':
        a = time.time()
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        cap = cv2.VideoCapture(0)
        out = cv2.VideoWriter('output.mkv',fourcc, 20.0, (640,480)) 
        while(time.time()-a<5):
                ret, frame = cap.read()
                out.write(frame)
                cv2.imshow('frame',frame)                        
        cap.release()
        out.release()
        cv2.destroyAllWindows()
##            cvReleaseVideoWriter(out)
        itchat.send('@vid@output.mkv','filehelper')
