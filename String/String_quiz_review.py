import keyboard
import pyperclip
# src='''
# Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[29]
#
# Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[30]
#
# Guido van Rossum began working on Python in the late 1980's, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[31] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.[32] Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.
#  '''
#

def paste_word_count():
    src=pyperclip.paste()
    word_list = src.split()
    clean_word_list = [w for w in word_list if w.isalpha()]
    clean_word_list.sort()
    count = {}
    for w in clean_word_list:
        count.setdefault(w, 0)
        count[w] += 1

    # print('word count'.center(20,'='))
    # for k,v in count.items():
    #     print(k.ljust(20,'.')+str(v).rjust(20,'.'))

    keyboard.write('word count'.center(20,'=')+'\n',delay=0.001)
    for k,v in count.items():
        keyboard.write(k.ljust(20,'.')+str(v).rjust(20,'.')+'\n',delay=0.001)


keyboard.add_hotkey('shift+windows+v',paste_word_count)
keyboard.wait('esc')