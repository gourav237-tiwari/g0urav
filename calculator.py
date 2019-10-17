####### G    U              I
# import tkinter as tk
# window=tk.Tk()
#
#
# def handleClick():
#     s=ent.get()
#     strVar.set(s)
#
#
# strVar=tk.StringVar()
# strVar.set('coding')
# tk.Label(window,textvariable=strVar).pack()
# tk.Button(window,text='click',command=handleClick).pack()
# ent=tk.Entry(window)
# ent.pack()
#
# window.mainloop()


import tkinter as tk


window=tk.Tk()
def handleClick(btnVal):
    val=0
    if btnVal=='=':
        val=eval(exp.get())
    elif btnVal=='c':
        val=''
    else:
        val=exp.get()+btnVal
    exp.set(val)


exp=tk.StringVar()
tk.Label(window,textvariable=exp).grid(row=0,column=0,columnspan=4)
tk.Button(window,text='c',width=5,height=2,command=lambda:handleClick('c')).grid(row=0,column=3)

tk.Button(window,text='7',width=5,height=2,command=lambda:handleClick('7')).grid(row=1,column=0)
tk.Button(window,text='8',width=5,height=2,command=lambda:handleClick('8')).grid(row=1,column=1)
tk.Button(window,text='9',width=5,height=2,command=lambda:handleClick('9')).grid(row=1,column=2)
tk.Button(window,text='/',width=5,height=2,command=lambda:handleClick('/')).grid(row=1,column=3)

tk.Button(window,text='4',width=5,height=2,command=lambda:handleClick('4')).grid(row=2,column=0)
tk.Button(window,text='5',width=5,height=2,command=lambda:handleClick('5')).grid(row=2,column=1)
tk.Button(window,text='6',width=5,height=2,command=lambda:handleClick('6')).grid(row=2,column=2)
tk.Button(window,text='*',width=5,height=2,command=lambda:handleClick('*')).grid(row=2,column=3)

tk.Button(window,text='1',width=5,height=2,command=lambda:handleClick('1')).grid(row=3,column=0)
tk.Button(window,text='2',width=5,height=2,command=lambda:handleClick('2')).grid(row=3,column=1)
tk.Button(window,text='3',width=5,height=2,command=lambda:handleClick('3')).grid(row=3,column=2)
tk.Button(window,text='-',width=5,height=2,command=lambda:handleClick('-')).grid(row=3,column=3)

tk.Button(window,text='.',width=5,height=2,command=lambda:handleClick('.')).grid(row=4,column=0)
tk.Button(window,text='0',width=5,height=2,command=lambda:handleClick('0')).grid(row=4,column=1)
tk.Button(window,text='=',width=5,height=2,command=lambda:handleClick('=')).grid(row=4,column=2)
tk.Button(window,text='+',width=5,height=2,command=lambda:handleClick('+')).grid(row=4,column=3)




window.mainloop()

































































































































