import keyboard
import pyperclip

# pyperclip.copy('hello from python')
# print(pyperclip.paste())

def report():
    keyboard.write('shift+windows+v key is pressed')

keyboard.add_hotkey('shift+windows+v',report)
print("start to catch hotkey")
keyboard.wait('esc')
print('end hotkey catching')