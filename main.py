import threading
import time
import numpy as np
import cv2
import keyboard
import win32api
import win32con
from PIL import ImageGrab
from scipy import spatial

y_ayar = 0
x_ayar = 0


def ekran_goruntusu_cek(isim='ekran_goruntusu.jpg'):
    im = ImageGrab.grab()
    im.save(isim)


def fare_hareketi(x, y):
    x_offset, y_offset = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x - x_offset - round(((x - x_offset) * 0.35)),
                         y - y_offset - round(((y - y_offset) * 0.35)), 0, 0)

    time.sleep(0.00001)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x - x_offset - round(((x - x_offset) * 0.35)),
                         y - y_offset - round(((y - y_offset) * 0.35)), 0, 0)

    time.sleep(0.0191)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x - x_offset - round(((x - x_offset) * 0.35)),
                         y - y_offset - round(((y - y_offset) * 0.35)), 0, 0)


def script_kapat():
    global bot
    bot = True
    while bot:
        if keyboard.is_pressed('capslock'):
            bot = False
            print("Program kapatılıyor!")
            exit()
        time.sleep(1)


def renk_bulma(boyut=1):
    global bot
    bot = True
    while bot:
        ekran_goruntusu_cek()
        resim = cv2.imread('ekran_goruntusu.jpg')

        lower = np.array([160, 140, 0], dtype="uint8")
        upper = np.array([255, 255, 45], dtype="uint8")

        mask = cv2.inRange(resim, lower, upper)

        ret, thresh = cv2.threshold(mask, 40, 255, 0)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        close_points = []
        for c in contours:
            if cv2.contourArea(c) > boyut:
                x1, y1, w1, h1 = cv2.boundingRect(c)
                close_points.append((round(x1 + (w1 / 2)), round(y1 + (h1 / 2))))

        if len(contours) != 0:
            pt = win32api.GetCursorPos()
            closest = close_points[spatial.KDTree(close_points).query(pt)[1]]
            fare_hareketi(closest[0], closest[1])


if __name__ == '__main__':
    print("Program başlatılıyor!!!")
    time.sleep(5)
    threading.Thread(target=script_kapat).start()
    print("Program Açık!!!")
    renk_bulma()
