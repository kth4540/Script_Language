import tkinter.tix
from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import re
window=Tk()
window.geometry("+100+100")
window.resizable(False,False)

def stop(event=None):
    window.quit()

# checkbox
ignore_case=IntVar(value=0)
Checkbutton(text="Ignore Case",variable=ignore_case).pack()


# radiobutton
find_color=StringVar(value='yellow')
Radiobutton(text='Green',value='green',variable=find_color).pack()
Radiobutton(text='Yellow',value='yellow',variable=find_color).pack()


input_frame=Frame()
input_frame.pack(side=TOP)

#combobox
pattern_var=StringVar(value='Python')
combobox=Combobox(input_frame,width=100,height=5,values=['Python','\d\d\d\d'],textvariable=pattern_var)
combobox.pack(side=LEFT)

# entry=Entry(input_frame,width=100)
# entry.insert(END,'Python')
# entry.pack(side=LEFT)

def find(event=None):
    input_text=text.get("1.0",END)  #1.0 : 1번째 줄 0번째 인덱스
    lines=input_text.splitlines()

    #pattern=entry.get()
    pattern=combobox.get()
    if ignore_case.get()==1:
        target_re=re.compile(pattern,re.IGNORECASE)
    else:
        target_re=re.compile(pattern)

    # history_listbox.insert(0,pattern)
    print(combobox['values'])
    combobox['values']=tuple(set(combobox['values'])|{pattern})

    text.tag_configure("found",background=find_color.get(),foreground='red')
    text.tag_remove("found","1.0",END)
    #text.tag_add('found',"1.0","1.20")

    for i, line in enumerate(lines):
        for mo in target_re.finditer(line):
            print(mo)
            text.tag_add('found',f"{i+1}.{mo.span()[0]}",f"{i+1}.{mo.span()[1]}")
            # i+1번째 줄에서 태그되는 첫번째 인덱스부터 마지막 인덱스까지 add
    pass
button=Button(input_frame,text="Find",command=find)
button.pack(side=RIGHT)

# listbox
# history_listbox=Listbox(height=5)
# history_listbox.insert(0,'Python')
# history_listbox.insert(1,'\d\d\d\d')
# history_listbox.insert(END,'[a-z]+')
# history_listbox.pack(fill=X)

# def select_pattern(event=None):
#     index=history_listbox.curselection()[0]
#     print(history_listbox.get(index))
#     entry.delete(0,END)
#     entry.insert(END,history_listbox.get(index))
# history_listbox.bind('<<ListboxSelect>>',select_pattern)

text=ScrolledText(width=50,height=50)
python_text='''
Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[31]
Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[32] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.[33] Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.
Python consistently ranks as one of the most popular programming languages.[34][35][36][37][38]
'''
text.insert(END,python_text)
text.pack(side=BOTTOM,fill=X)

def open_file():
    file_name=filedialog.askopenfilename(
        title='Select a text file',
        filetypes=(('txt files','*.txt'),)
    )
    print("open file")

def save_file_as():
    file_name=filedialog.asksaveasfilename(
        title='save file as ...',
        filetypes=(('txt files', '*.txt'),),
        defaultextension='txt'
    )
    print(file_name)

menu_root=Menu()
menu_file=Menu(menu_root)
menu_file.add_command(label="Open",command=open_file,accelerator='Ctrl+o')
menu_file.add_separator()
menu_file.add_command(label="save as ...",command=save_file_as)
menu_file.add_command(label='quit',command=stop)
menu_root.add_cascade(label="File",menu=menu_file)
window.config(menu=menu_root)

menu_search=Menu(menu_root)
menu_search.add_command(label="Search by text")
menu_root.add_cascade(label="Search",menu=menu_search)


window.bind("<Escape>",stop)
window.mainloop()