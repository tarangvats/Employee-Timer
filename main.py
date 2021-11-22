from tkinter import *
from math import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
WHITE ="#FFFFFF"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
tiktok = None
chance =0

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global chance
    window.after_cancel(tiktok)
    chance = 0
    canvas.itemconfig(timer,text = "0:00", fill=WHITE)
    check.config(text="")
    label.config(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global chance
    chance = chance+1


    work = int(WORK_MIN * 60)
    short_break = int(SHORT_BREAK_MIN * 60)
    long_break = int(LONG_BREAK_MIN * 60)

    if chance%2==1:
        label.config(text = "Work",fg = RED)
        # canvas.itemconfig(timer, fill=WHITE)
        countdown(work)
    elif chance<=5:
        label.config(text="Break", fg=PINK)
        # canvas.itemconfig(timer, fill=RED)
        countdown(short_break)
    elif chance==6:
        label.config(text = "Lunch Time",fg = GREEN)
        # canvas.itemconfig(timer, fill=GREEN)
        countdown(long_break)
    else:
        canvas.itemconfig(timer, text="completed")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global tiktok
    minute = floor(count/60)
    second = count%60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer, text=f"{minute}:{second}")
    if count>0:
         tiktok = window.after(1000,countdown,count-1)
    else:

        tick = "✅"
        if chance%2==1:
            tick = tick*ceil(chance/2)
            check.config(text = tick)
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(1000,1000)
window.title("Pomodoro")
window.config(padx =90 ,pady =50,bg = YELLOW)

label = Label(text = "Timer" , font = (FONT_NAME,40),bg = YELLOW, fg = GREEN)
label.grid(column = 1, row =0)

canvas  = Canvas(width=200,height = 224,bg = YELLOW, highlightthickness=0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato)
timer = canvas.create_text(100,130,text = "00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(column = 1, row = 1)








button1 = Button(text = "Start",command = start, highlightthickness = 0)
button2 = Button(text = "Reset",command = reset,highlightthickness = 0)
button1.grid(column = 0, row = 2)
button2.grid(column = 2, row=2)

check = Label( bg = YELLOW)
check.grid(column = 1, row =2)



window.mainloop()
