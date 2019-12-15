#!/usr/bin/python2
# -*- coding: utf8 -*-


from Tkinter import *
from printer import pages_in_order


def calculate(*args):
    try:
        npages = int(feet.get())
        assert npages > 1, "calculate::assert npages > 1"
        inst = make_instructions(npages)
        showInstructions(inst)
    except ValueError:
        print("value error")
        showInstructions(u"바보야. 숫자만 입력해.")
        
    except AssertionError as ae:
        print("assertion error")
        print(ae)
        showInstructions(u"2장 미만은 알아서 해야하지 않겠니?")
        
def showInstructions(t):
    resultText.delete("0.0", END)
    resultText.insert(INSERT, t)
    
def make_instructions(npages):
    fp, sp = pages_in_order(npages, pages_per_each.get())
    fp = [str(p) for p in fp]
    sp = [str(p) for p in sp]
    step1 = ", ".join(fp)
    step2 = ", ".join(sp)

    list_inst = []

    list_inst.append("Print me : " + step1)
    if(pages_per_each==1):
        list_inst.append(u"프린트된 면이 보이면서 상단이 프린터 안쪽을 "
                        u"향하도록 트레이에 다시 넣어줍니다.")
    else:
        list_inst.append(u"프린트물을 현재 위상 그대로 트레이에 다시 넣어줍니다.")
    
    list_inst.append("Print me : " + step2)
    
    return "\n\n".join(list_inst)

def sel():
   selection = "You selected the option " + str(pages_per_each.get())
   print(selection)
   
root = Tk()
root.title(u"양면 프린터 도우미")

mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=1, row=1, sticky=(W, E))

resultText = Text(mainframe)
resultText.grid(column=1, row=2, sticky=(W, E))
Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=4, sticky=W)

Label(mainframe, text="pages").grid(column=2, row=1, sticky=W)
Label(mainframe, text="Instructions").grid(column=2, row=2, sticky=W)
Label(mainframe, text=u"Made by 용달이 for 멍굴이").grid(column=1, row=4, sticky=W)

radiobuttons = Frame(mainframe)
radiobuttons.grid(column=1, row=3)

pages_per_each = IntVar()
pages_per_each.set(1)
R1 = Radiobutton(radiobuttons, text=u"1 page per each", variable=pages_per_each, value=1, command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(radiobuttons, text="2 pages per each", variable=pages_per_each, value=2, command=sel)
R2.pack( anchor = W )
R3 = Radiobutton(radiobuttons, text="4 pages per each", variable=pages_per_each, value=4, command=sel)
R3.pack( anchor = W)
R3 = Radiobutton(radiobuttons, text="8 pages per each", variable=pages_per_each, value=8, command=sel)
R3.pack( anchor = W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

