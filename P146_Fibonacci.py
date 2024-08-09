from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Fibonacci (X)')

def fibo():
    l = int(e.get())
    a = 0
    b = 1
    c = 0
    t = 0
    s = 1
    l1['text'] =  'Fibonacci Series'
    while(t != l):
        l1['text'] += ' ' + str(c)
        a = b
        b = c
        c = a + b
        t += 1
        s += b
    l2['text'] = 'Sum:' + str(s)
    
l1 = Label(root,text='Fibonacci Series')
l2 = Label(root,text='Sum:')
e = Entry(root)
btn = Button(root,text='Calculate Series', command = fibo)

btn.pack()
e.pack()
l1.pack()
l2.pack()

root.mainloop()