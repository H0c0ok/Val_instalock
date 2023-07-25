import cv2
import pyautogui
import os
import time
import mouse
from skimage.metrics import structural_similarity as ssim


def are_images_similar(main_s, user, threshold=0.9):
    image1 = cv2.imread(main_s)
    image2 = cv2.imread(user)
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    simi = ssim(gray1, gray2)

    if simi > threshold:
        return True
    else:
        return False


def select_agent(agents_list, agent):
    return agents_list[agent]


def picking(coordinates, delay):
    mouse.move(int(coordinates[0]), int(coordinates[1]), absolute=True, duration=0.0001)
    time.sleep(delay)
    mouse.click('left')
    time.sleep(delay)
    mouse.move(949, 809, absolute=True, duration=0.0001)
    time.sleep(delay)
    mouse.click('left')
    os.remove("user_lockscreen.jpg")


def make_screenshot():
    myscreenshot = pyautogui.screenshot(region=(0, 700, 1900, 380))
    myscreenshot.save(r'User_lockscreen.jpg')
    user_lockscreen = "User_lockscreen.jpg"
    return user_lockscreen


def main(agent):
    with open("agents.txt") as file:
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
        for i in file.readlines():
            key, val = i.strip().split(":")
            agents_list[key] = val.split(" ")

    main_lockscreen = "Lock_screen.jpg"
    delay_between_mouse_moves = 0.001
    curTime = time.time()

    coordinates = select_agent(agents_list, agent)
    similar = False
    while not similar:
        similar = are_images_similar(main_lockscreen, make_screenshot())
        time.sleep(0.01)
        if time.time() - curTime > 120:
            return "Time"
    else:
        picking(coordinates, delay_between_mouse_moves)
        return "True"


if __name__ == '__main__':
    main()
