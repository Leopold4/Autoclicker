import pyautogui as pag
from customtkinter import *
from time import sleep
import keyboard as kb
from PIL import Image

img = ''


def clicker(freq=1):
    pag.click()
    sleep(1/freq)


def clickloop():
    speed = int(IntVar.get(freq))
    stopper = StringVar.get(stop_bind)
    while (True) and kb.is_pressed(stopper) == False:
        clicker(speed)


def clickhold():
    stopper = StringVar.get(stop_bind)
    while (kb.is_pressed(stopper)) == False:
        if pag.mouseDown() == True:
            pass
        else:
            pag.mouseDown()
    pag.mouseUp()


def set_bind_clickloop():
    try:
        kb.remove_hotkey(clickhold)
    except TypeError:
        pass
    else:
        kb.remove_hotkey(clickhold)
    finally:
        kb.add_hotkey(StringVar.get(key_bind), clickloop)


def set_bind_clickhold():
    try:
        kb.remove_hotkey(clickloop)
    except TypeError:
        pass
    else:
        kb.remove_hotkey(clickloop)
    finally:
        kb.add_hotkey(StringVar.get(key_bind), clickhold)


def img_search():
    try:
        Image.open('./bg.jpg')
    except FileNotFoundError:
        pass
    else:
        return CTkImage(light_image=Image.open('./bg.jpg'), size=(400, 400))


root = CTk()
root.minsize(600, 350)
root.maxsize(600, 350)
set_appearance_mode('dark')
set_default_color_theme('green')  # window setup

y = 5
pos = 110/600

img = img_search()
freq = IntVar(value=1)
key_bind = StringVar(value='j')
stop_bind = StringVar(value='k')  # variable setup

bg = CTkLabel(root, text='', image=img).place(
    relx=0.68, rely=0.5, anchor='center')

frame = CTkFrame(root, width=220, height=410, fg_color='#1a0219', border_color='#1a0219').place(
    relx=pos, rely=0.5, anchor='center')

header = CTkLabel(frame, text='autoclicker', width=220, font=(
    'impact', 40), fg_color='#1a0219').grid(columnspan=2, column=0, row=0, pady=y)

freq_in_lab = CTkLabel(root, text='clicks per second',
                       font=('impact', 15), fg_color='#1a0219').grid(columnspan=2, column=0, row=1, pady=y)
freq_in = CTkEntry(
    root, textvariable=freq, fg_color='#1a0219', bg_color='#1a0219', border_color='#540853', corner_radius=40, font=(
        'impact', 15)).grid(columnspan=2, column=0, row=2, pady=y)

key_in_lab = CTkLabel(root, text='bind a start key, default is j',
                      font=('impact', 15), fg_color='#1a0219').grid(columnspan=2, column=0, row=3, pady=y)
key_in = CTkEntry(
    root, textvariable=key_bind, fg_color='#1a0219', bg_color='#1a0219', border_color='#540853', corner_radius=40, font=(
        'impact', 15)).grid(columnspan=2, column=0, row=4, pady=y)

stopper_in_lab = CTkLabel(root, text='bind a stop key, default is k',
                          font=('impact', 15), fg_color='#1a0219').grid(columnspan=2, column=0, row=5, pady=y)
stopper_in = CTkEntry(
    root, textvariable=stop_bind, fg_color='#1a0219', bg_color='#1a0219', border_color='#540853', corner_radius=40, font=(
        'impact', 15)).grid(columnspan=2, column=0, row=6, pady=y)

run_button = CTkButton(root, text='clicker', width=110, height=40, fg_color='#1a0219', bg_color='#1a0219', hover_color='#540853', border_width=2, border_color='#540853', corner_radius=10, font=(
    'impact', 15), command=set_bind_clickloop).grid(column=0, row=7, pady=y)

run_button2 = CTkButton(root, text='holder', width=110, height=40, fg_color='#1a0219', bg_color='#1a0219', hover_color='#540853', border_width=2, border_color='#540853', corner_radius=10, font=(
    'impact', 15), command=set_bind_clickhold).grid(column=1, row=7, pady=y)

root.mainloop()
