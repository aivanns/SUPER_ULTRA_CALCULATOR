from tkinter import *

win = Tk()
win.geometry("435x450")
win.resizable(0, 0)

can = Canvas(win, width=435, height=450)

can.create_text(215, 25, text='SUPER ULTRA CALCULATOR', font="Arial 22 bold", fill='red')
can.create_text(215, 125, text='Microsoft 2024-2025Ⓡ', font="Arial 22 bold", fill='red')

res = Entry(win, width=19, font='Arial 30')
res.place(x=5, y=50)
res.insert(0, '')

class Counter:
    count = 0
    is_counted = False
    def check(self):
        if c.is_counted:
                c.is_counted = False
                print(res.get())
                pk()

c = Counter()

def p1():
    c.check()
    res.insert(c.count, '1')
    c.count += 1
def p2():
    c.check()
    res.insert(c.count, '2')
    c.count += 1
def p3():
    c.check()
    res.insert(c.count, '3')
    c.count += 1
def p4():
    c.check()
    res.insert(c.count, '4')
    c.count += 1
def p5():
    c.check()
    res.insert(c.count, '5')
    c.count += 1
def p6():
    c.check()
    res.insert(c.count, '6')
    c.count += 1
def p7():
    c.check()
    res.insert(c.count, '7')
    c.count += 1
def p8():
    c.check()
    res.insert(c.count, '8')
    c.count += 1
def p9():
    c.check()
    res.insert(c.count, '9')
    c.count += 1
def p0():
    c.check()
    res.insert(c.count, '0')
    c.count += 1
def pp():
    c.check()
    res.insert(c.count, '+')
    c.count += 1
def pm():
    c.check()
    res.insert(c.count, '-')
    c.count += 1
def py():
    c.check()
    res.insert(c.count, '*')
    c.count += 1
def pd():
    c.check()
    res.insert(c.count, '/')
    c.count += 1
def pk():
    c.check()
    res.delete(0, END)
    c.count = 0
def calc():
    result = res.get()
    pk()
    try:
        res.insert(0, eval(result))
    except Exception as e:
        res.insert(0, f'error: {e}')
    c.is_counted = True
    
b0 = Button(win, text="0", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p0)
b1 = Button(win, text="1", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p1)
b2 = Button(win, text="2", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p2)
b3 = Button(win, text="3", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p3)
b4 = Button(win, text="4", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p4)
b5 = Button(win, text="5", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p5)
b6 = Button(win, text="6", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p6)
b7 = Button(win, text="7", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p7)
b8 = Button(win, text="8", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p8)
b9 = Button(win, text="9", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=p9)
bp = Button(win, text="+", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=pp)
bm = Button(win, text="-", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=pm)
by = Button(win, text="x", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=py)
bd = Button(win, text="/", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=pd)
br = Button(win, text="=", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=calc)
bk = Button(win, text="<<", width=4, height=2, bg="lightblue", fg="white", font='Arial 24', command=pk)

b1.place(x=0, y=150)
b2.place(x=87, y=150)
b3.place(x=87*2, y=150)
b4.place(x=0, y=250)
b5.place(x=87, y=250)
b6.place(x=87*2, y=250)
b7.place(x=0, y=350)
b8.place(x=87, y=350)
b9.place(x=87*2, y=350)
b0.place(x=87*3, y=350)
bp.place(x=87*3, y=150)
bm.place(x=87*3, y=250)
by.place(x=87*4, y=250)
bd.place(x=87*3, y=250)
br.place(x=87*4, y=350)
bk.place(x=87*4, y=150)

can.pack()


'''b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()
b0.pack()'''


win.mainloop()