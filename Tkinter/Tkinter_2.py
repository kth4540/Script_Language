wiki_python = '''
Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[31]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.[33] Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.

Python consistently ranks as one of the most popular programming languages.[34][35][36][37][38]
'''

import re

import logging
from logging import info as print
logging.basicConfig(level=logging.DEBUG)

from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title('My Tkinter App')
window.geometry("+700+400")
window.resizable(False, False)

label = Label(text="Regular Expression Program".center(100, ' '))
label.pack()
# label.place(x=100, y=100)

# def rotate():
#     text = label.cget('text')
#     text = text[1:] + text[0]
#     label.configure(text=text.center(100, ' '))
#     pass

#   input_frame = entry + button
input_frame = Frame()
input_frame.pack()

entry = Entry(input_frame, width=100)
entry.insert(END, 'Python')
entry.pack(side=LEFT)

def find(event=None):

    text.tag_configure("found",background='yellow',foreground='red')

    # prepare re
    input_text = entry.get()
    target_re = re.compile(input_text)

    # get scrolled text's all text
    src_text = text.get("1.0", END)
    lines = src_text.splitlines()
    for i,line in enumerate(lines):
        for mo in target_re.finditer(line):
            text.tag_add('found',f"{i+1}.{mo.span()[0]}",f"{i+1}.{mo.span()[1]}")
            print(mo)
    pass

button = Button(input_frame, text="Find", command=find, takefocus=False)
button.pack(side=RIGHT)

#   text
text = ScrolledText(height=30, font=("Consolas", 11))
text.insert(END, wiki_python)
text.pack(side=BOTTOM, fill=X)

def stop(event=None):
    window.quit()

window.bind("<Escape>", stop)
window.mainloop()