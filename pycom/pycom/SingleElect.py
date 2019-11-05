# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/7/24 17:22


import functools
import  os
from tkinter import *
from tkinter.filedialog import askdirectory ,askopenfilename

from tkinter import *


def callRadiobutton( root , value, re_value):
    re_value = value
    print(re_value)
    root.quit()
    root.destroy()

root = Tk()
re_value = 0
value_1=1
value_2=2
value_3=3

Radiobutton(root,  text="tip 1",value=False,
            command=functools.partial(callRadiobutton,root,value_1, re_value)).grid()
Radiobutton(root,  text="tip 2",value=False,
            command=functools.partial(callRadiobutton,root,value_2, re_value)).grid()
Radiobutton(root, text="tip 3",value=False,
            command=functools.partial(callRadiobutton,root,value_3, re_value)).grid()

root.mainloop()