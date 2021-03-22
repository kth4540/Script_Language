import pyperclip
import keyboard

def report():
    Dict={}
    tmp=pyperclip.paste()
    tmp=tmp.replace('-', ' ')
    tmp_2=''.join(a for a in tmp if a.isalpha() or a.isspace())
    tmp_2=tmp_2.split()

    for c in tmp_2:
        Dict.setdefault(c,0)
        Dict[c]=Dict[c]+1

    for k, v in Dict.items():
        print(k.ljust(20,'.') + str(v).rjust(7))

keyboard.add_hotkey('shift+windows+v',report)
print("start to catch hotkey")
keyboard.wait('esc')
print('end hotkey catching')
