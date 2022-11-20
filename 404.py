from tkinter import *
import random
from threading import Thread
from playsound import playsound

def music():playsound('D:\\Download\\01-Alice- Madness Returns Theme.mp3')#функция которая будет играть музыка

Thread(target = music, daemon=True).start()#запускается функция в отдельном потоке

'''from tkinter import messagebox
top = Tk()

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\Даша\\Desktop\\Класссные картинки\\image.jpg")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
top.mainloop'''
def gen():
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    X = random.choice(s)
    return X
def clicked():
    DEC = int(txt.get(), 16)
    one = DEC // 10000
    two = DEC // 1000 % 10
    three = DEC // 100 % 10
    forfiv = DEC % 100
    lb2 = Label(window, text=f"{one}{gen()}{gen()}{gen()}{gen()}-{two}{gen()}{gen()}{gen()}{gen()}-{three}{gen()}{gen()}{gen()}{gen()} {forfiv}", font=("Arial Bold", 14))
    lb2.grid(column=1, row=2)

window = Tk()
window.title("Генератор ключей ультра макс 3000000")
window.geometry('500x500')
lbl = Label(window, text="Ведите 5-значный НEX", font=("Arial Bold", 14))
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
txt.focus()
a = txt.get()
btn = Button(window, text="Сгенерировать ключ", command=clicked)
btn.grid(column=0, row=2)
window.mainloop()
