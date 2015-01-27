import sched, time
from datetime import datetime
from cv2 import *

scheduler = sched.scheduler(time.time, time.sleep)
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera

def take_picture(controller):    
    print "taking photo"
    frame, img = cam.read()
    if frame:    # frame captured without any errors
        imwrite("pics/{now}.jpg".format(now=datetime.now()),img) #save image
    controller.enter(60, 1, take_picture, (scheduler,))

scheduler.enter(60, 1, take_picture, (scheduler,))
scheduler.run()
