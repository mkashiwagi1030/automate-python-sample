import os
import pyautogui as gui
from time import sleep

meeting_id = '************'
password = '*******************'


def get_image_location(filename):
    location = None
    while location is None:
        sleep(0.1)
        # 画像をグレースケールで80%の制度で解析
        location = gui.locateCenterOnScreen(filename, grayscale=True, confidence=0.8)
    return location


os.system("open /Applications/zoom.us.app")
# アプリの起動を待つ
sleep(5)
plus_button = get_image_location('img/plus_button.png')
gui.moveTo(plus_button.x / 2, plus_button.y / 2, duration=0.3)
gui.click()
gui.write(meeting_id)
checkbox = get_image_location('img/video_off.png')
gui.moveTo(checkbox.x / 2, checkbox.y / 2, duration=0.3)
gui.click()
submit_button = get_image_location('img/submit_button.png')
gui.moveTo(submit_button.x / 2, submit_button.y / 2, duration=0.3)
gui.click()
# パスワード入力画面が開くのを待つ
sleep(1)
gui.write(password)
submit_button = get_image_location('img/submit_button.png')
gui.moveTo(submit_button.x / 2, submit_button.y / 2, duration=0.3)
gui.click()
# 入室を待つ
sleep(4)
submit_button = get_image_location('img/audio_button.png')
gui.moveTo(submit_button.x / 2, submit_button.y / 2, duration=0.3)
gui.click()
