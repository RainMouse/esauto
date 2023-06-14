import adb_utiles as adbu
import image_contrast as contrast
import cv2
import json
import time

adb = adbu.AdbUtiles()
templates = {
    'buy' : cv2.cvtColor(cv2.imread("./images/buy.png"), cv2.COLOR_BGR2GRAY),
    'mystery' : cv2.cvtColor(cv2.imread("./images/mystery.png"), cv2.COLOR_BGR2GRAY),
    'covenant' : cv2.cvtColor(cv2.imread("./images/covenant.png"), cv2.COLOR_BGR2GRAY),
    'refresh' : cv2.cvtColor(cv2.imread("./images/refresh.png"), cv2.COLOR_BGR2GRAY),
    'confirm' : cv2.cvtColor(cv2.imread("./images/confirm.png"), cv2.COLOR_BGR2GRAY)
}

relative_buy = {
    'h' : 60,
    'w' : 900
}

final_data = {
    'refresh' : 0,
    'mystery' : 0,
    'covenant': 0
}

config = json.load(open("config/config.json"))

use_diamonds = config['use_diamonds']

is_mystery = 0
is_covenant = 0

def start():
    global use_diamonds, is_mystery, is_covenant

    while 1:
        use_diamonds -= 3
        if use_diamonds < 3:
            break

        time.sleep(1.5)

        seek_click()

        adb.swip()

        seek_click()

        result = contrast.matchTemplate(adb.screenshot(), templates['refresh'])
        if result['state']:
            th, tw = templates['refresh'].shape[:2]
            maxLoc = result['maxLoc']
            confirm_click(maxLoc[0] + tw/2, maxLoc[1] + th/2)

            final_data['refresh'] = final_data['refresh'] + 1
            is_mystery = 0 
            is_covenant = 0
            with open("config/result.json", "w") as outfile:
                json.dump(final_data, outfile)
              
        else:
            break        

def seek_click():

    global is_mystery, is_covenant

    if is_mystery == 0:
        result = contrast.matchTemplate(adb.screenshot(), templates['mystery'])

        if result['state']:
            maxLoc = result['maxLoc']
            buy_click(maxLoc[0] + relative_buy['w'], maxLoc[1] + relative_buy['h'])
            final_data['mystery'] = final_data['mystery'] + 1
            is_mystery = 1 

    if is_covenant == 0:
        result = contrast.matchTemplate(adb.screenshot(), templates['covenant'])

        if result['state']:
            maxLoc = result['maxLoc']
            buy_click(maxLoc[0] + relative_buy['w'], maxLoc[1] + relative_buy['h'])
            final_data['covenant'] = final_data['covenant'] + 1
            is_covenant = 1    

def buy_click(x, y):
    # for i in range(10):
        adb.click([x, y])
        result = contrast.matchTemplate(adb.screenshot(), templates['buy'])
        if result['state']:
            th, tw = templates['buy'].shape[:2]
            maxLoc = result['maxLoc']
            adb.click([maxLoc[0] + tw/2, maxLoc[1] + th/2])
            # if not contrast.matchTemplate(adb.screenshot(), templates['confirm'])['state']:
            #     break
def confirm_click(x, y):
    # for i in range(10):
        adb.click([x, y])
        result = contrast.matchTemplate(adb.screenshot(), templates['confirm'])
        if result['state']:
            th, tw = templates['confirm'].shape[:2]
            maxLoc = result['maxLoc']
            adb.click([maxLoc[0] + tw/2, maxLoc[1] + th/2])
            # if not contrast.matchTemplate(adb.screenshot(), templates['confirm'])['state']:
            #     break            

if __name__ == "__main__":
    start()








