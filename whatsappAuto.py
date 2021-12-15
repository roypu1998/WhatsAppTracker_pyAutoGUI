#coding=utf8
import pyautogui as pg
import webbrowser as web
import time
import pyperclip
import os
import datetime

class WhatsappAuto():

    def __init__(self,phone_no:str):

        if os._exists('image.png'):
            os.remove('image.png')

        self.url = 'https://web.whatsapp.com'
        self.contact = phone_no

    def enter_chat(self):

        web.open(self.url)
        time.sleep(20)
        pg.click(x=1185, y=188)

        pyperclip.copy(self.contact)
        time.sleep(2)
        pg.hotkey('ctrl', 'v')
        time.sleep(2)
        pyperclip.paste()
        pg.press('enter')
        time.sleep(2)

        if pg.locateOnScreen('not_find_user.png'):
            return f'{self.contact} is not exists.',False
        else:
            self.screenShot()
            return f'{self.contact} found.',True

    def screenShot(self):
        pg.screenshot('image.png', (150, 100, 932, 67))

    def mark_activity(self):
        time.sleep(2)
        pg.click(x=850, y=142)

    def copy_and_check_active(self):
        time.sleep(2)
        pg.tripleClick(x=925, y=144)
        time.sleep(1)
        pg.hotkey('ctrl', 'c')
        time.sleep(1)
        active = pyperclip.paste()
        current_time = f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}'

        if len(active) < 10 and active != self.contact and active != '':
            pyperclip.copy('')
            return f'{self.contact} is online -> {current_time}'
        return f'{self.contact} is offline -> {current_time}'
