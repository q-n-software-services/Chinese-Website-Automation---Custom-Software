import datetime
import os
import time
import requests
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pt

if __name__ == '__main__':
    now = datetime.datetime.now()
    while now.hour != 6 and now.minute != 00:
        time.sleep(5)
        now = datetime.datetime.now()
        pt.moveRel(122, 112, duration=0.5)
        pt.moveRel(-122, -112, duration=0.5)

    cwd = os.getcwd()
    os.environ['PATH'] += r"{}/chromedriver.exe".format(cwd)
    driver = webdriver.Chrome()


    ip_now = '000000000000'
    available1 = []
    available2 = []
    available3 = []
    available4 = []
    available5 = []
    left_overs = []
    browser = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    for i in browser:

        options = webdriver.ChromeOptions()

        browser[i] = uc.Chrome(
            options=options,
        )
        try:
            browser[i].get('https://w2.leisurelink.lcsd.gov.hk/leisurelink/index/index.jsp?lang=en')
            time.sleep(22)
            available1.append(browser[i].current_window_handle)
            b = time.time()

            c = time.time()
            time.sleep(22)
            # available2.append(browser[i].current_window_handle)
            available3.append(i)
            time.sleep(1)
            print(browser[i].current_window_handle)
            print("elapsed time = ", (c - b) / 2)


        except:
            print("didn't work")
            browser[i].quit()

    now = datetime.datetime.now()
    while now.hour < 6 or (now.hour == 6 and now.minute < 20):
        time.sleep(1)
        now = datetime.datetime.now()

    for i in available3:
        first_element = browser[i].find_element(By.ID, 'iamsmartLogin')
        try:
            first_element.click()
            first_element.click()
            first_element.click()
            first_element.click()
            first_element.click()
        except:
            print(' ')
            available3.pop(i)
            browser[i].quit()
        browser[i].implicitly_wait(30)

    now = datetime.datetime.now()
    while now.hour < 6 or (now.hour == 6 and now.minute < 40):
        time.sleep(1)
        now = datetime.datetime.now()

    for i in available3:
        try:
            browser[i].minimize_window()
            browser[i].maximize_window()

            my_element = browser[i].find_element_by_id('LCSD_2')
            my_element.click()
            browser[i].implicitly_wait(30)
            time.sleep(30)
            this_tab = browser[i].current_window_handle

            positions1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
            available4.append((browser[i], browser[i].current_window_handle, positions1))
            available5.append(this_tab)


        except:
            print('Error operating window for query ', i)

    now = datetime.datetime.now()
    while now.hour < 3 or now.minute < 59 or now.second < 57:
        time.sleep(1)
        now = datetime.datetime.now()

    for controller, tab, position in available4:
        try:
            controller._switch_to.window(tab)
            pt.moveTo(position)
            pt.click()
        except:
            print("not done")

    time.sleep(5)
    i = 0
    for controller, tab, position in available4:
        i += 1
        try:
            controller._switch_to.window(tab)
            position1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
            pt.moveTo(position1)
            pt.click()
        except:
            print("not done")
            left_overs.append((controller, available5[i - 1]))

    time.sleep(5)

    for controller, tab, position in available4:
        try:
            controller._switch_to.window(tab)
            position1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
            pt.moveTo(position1)
            pt.click()
        except:
            print("not done")

    # left-overs
    left_over2 = []
    for controller, tab in left_overs:
        first_element = controller.find_element(By.ID, 'iamsmartLogin')
        try:
            first_element.click()
            first_element.click()
            first_element.click()
            first_element.click()
            first_element.click()
        except:
            print(' ')

    time.sleep(5)

    for controller, tab in left_overs:

        try:
            controller.minimize_window()
            controller.maximize_window()

            my_element = controller.find_element_by_id('LCSD_2')
            my_element.click()
            controller.implicitly_wait(30)
            time.sleep(30)
            this_tab = controller.current_window_handle

            positions1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
            left_over2.append((controller, controller.current_window_handle, positions1))


        except:
            print('Error operating window for query ', i)

    for controller, tab, position in left_over2:
        try:
            controller._switch_to.window(tab)
            pt.moveTo(position)
            pt.click()
        except:
            print("not done")

    time.sleep(5)
    i = 0
    for controller, tab, position in left_over2:
        i += 1
        try:
            controller._switch_to.window(tab)
            position1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
            pt.moveTo(position1)
            pt.click()
        except:
            print("not done")

    time.sleep(5)

    for controller, tab, position in left_over2:
        try:
            controller._switch_to.window(tab)
            position1 = pt.locateCenterOnScreen('continue.png', grayscale=False, confidence=0.9)
            pt.moveTo(position1)
            pt.click()
        except:
            print("not done")

    time.sleep(120000)
