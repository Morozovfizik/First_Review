from tkinter import *
from threading import *
import time

root = Tk()
root.title("Click to win")
root.geometry('600x400+0+0')

score = 0
multy = 1
price = 50
au_price = 1000
au_multy = 1
activate = False
text1 = Text(width=19, height=1, font='Times 20', fg='blue')
text2 = Text(width=19, height=1, font='Times 20')
text3 = Text(width=19, height=2, font='Times 20')
textend = Text(width=35, height=3, font='Times 27', fg='red')


def click(event):
    global score
    global multy
    score += 1 * multy
    deltext(text1)
    instext("Your score: " + str(score), text1)


def deltext(text):
    text.delete(1.0, END)


def instext(ins, text):
    text.insert(1.0, str(ins))


def improve():
    global multy
    global score
    global price
    if score >= price:
        score -= price
        price *= 2
        multy += 2
        deltext(text1)
        instext("Your score: " + str(score), text1)
        deltext(text2)
        instext("Upgrade price: " + str(price), text2)


def autoclick():
    Thread(target=Autoclick).start()


def Autoclick():
    global activate
    if not(activate):
        activate = True
        global score
        global au_price
        global au_multy
        if score >= au_price:
            score -= au_price
            au_price *= 4
            deltext(text3)
            instext("Auto upgrade\nprice: " + str(au_price), text3)
            while True:
                score += 1 * au_multy
                deltext(text1)
                instext("Your score: " + str(score), text1)
                if score >= 10000000:
                    instext("Congratulations!!!\nYOU WIN!", textend)
                    time.sleep(10)
                    sys.exit()
                time.sleep(1)


def impauto():
    global activate
    if activate:
        global score
        global au_multy
        global au_price
        if score >= au_price:
            score -= au_price
            au_price *= 2
            au_multy += 2
            deltext(text3)
            instext("Auto upgrade\nprice: " + str(au_price), text3)


instext("Your score: " + str(score), text1)
instext("Upgrade price: " + str(price), text2)
instext("Auto upgrade\nprice: " + str(au_price), text3)
instext("Click right now!!!", textend)

rule = Label(text="Click to increase your score. To upgrade your clicker\nyou need to save up " +
                  "essential score number.",
             font='Times 15', bg='grey', fg='black', width=55, height=2)
hint = Label(text="Collect 10'000'000\nscores to complete\nthe game.", font='Times 18', fg='black', bg='grey',
             width=20, height=4)
auto_click = Button(text="Buy autoclicker", font='Times 20', fg='red', width=22, height=2, command=autoclick)
upgrader = Button(text="Improve multiplicator", font='Times 20', fg='green', width=22, height=2, command=improve)
upclicker = Button(text="Improve autoclicker", font='Times 20', fg='blue', width=22, height=2, command=impauto)

activate_auto = Button()
root.bind("<space>", click)
textend.place(x=0, y=305)
auto_click.place(x=0, y=50)
upgrader.place(x=0, y=135)
upclicker.place(x=0, y=220)
text1.place(x=340, y=50)
text2.place(x=340, y=85)
text3.place(x=340, y=120)
rule.place(x=0, y=0)
hint.place(x=340, y=189)

root.mainloop()
