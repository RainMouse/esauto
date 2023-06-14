from pickle import TRUE
import numpy as np
import imutils
import cv2

result = {'state': False}

accept_value = 0.8

def matchTemplate(background, template):

    # img = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

    # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result['state'] = False
    r = cv2.matchTemplate(background, template, cv2.TM_CCOEFF_NORMED)
    _, maxval,_ ,maxLoc = cv2.minMaxLoc(r)

    if(maxval > accept_value):
        result['state'] = True
        result['maxLoc'] = maxLoc
        # result['template'] = [tw, th]

    return result    
