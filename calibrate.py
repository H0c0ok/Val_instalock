import cv2
import os
import pyautogui
import time


def find_object(template_path, image_path):
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)
    h, w, _ = template.shape
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    threshold = 0.8

    if max_val >= threshold:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        corx = int((top_left[0] + bottom_right[0]) / 2)
        cory = int((top_left[1] + bottom_right[1]) / 2)
        return [corx, cory]
    else:
        print("Can't find object:", template_path.replace("agents_icons/", "")[:-4])


def make_screenshot():
    myscreenshot = pyautogui.screenshot(region=(0, 700, 1900, 380))
    myscreenshot.save(r'image.jpg')
    user_lockscreen = "image.jpg"
    return user_lockscreen


time.sleep(5)
user_screen = make_screenshot()
agents_list = {
        "brimstone": [714, 938],
        "phoenix": [789, 1000],
        "sage": [1047, 1012],
        "sova": [1212, 996],
        "viper": [1310, 1013],
        "cypher": [869, 910],
        "reyna": [968, 995],
        "killjoy": [546, 1002],
        "breach": [625, 909],
        "omen": [706, 1007],
        "jett": [1298, 923],
        "raze": [875, 1012],
        "skye": [1130, 1010],
        "yoru": [1378, 1009],
        "astra": [548, 922],
        "kayo": [1377, 907],
        "chamber": [789, 923],
        "neon": [611, 995],
        "fade": [1040, 912],
        "harbor": [1214, 922],
        "gekko": [1128, 922],
        "deadlock": [972, 909],
        #   "": [0, 0],    # this for new agents, fist num is cor X, second is cor Y
    }
for i in os.listdir("agents_icons"):
    coors = find_object("agents_icons/" + i, user_screen)
    cors = ""
    for j in coors:
        cors += str(j) + " "
    agents_list[i[:-4]] = cors

with open("agents.txt", "w") as file:
    for i in agents_list:
        file.write(i + ":" + agents_list[i] + "\n")
print("Sucsessfuly calibrated!")
os.remove("image.jpg")
