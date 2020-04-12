from tkinter import *
import random
def insert_buttons(n_buttons):
    global buttons
    global score
    buttons = []
    win_but = random.randint(0, n_buttons - 1)
    for i in range(n_buttons):
        if i == win_but:
            buttons.append(Button(t, text = 'Press me', command = hit))
        else:
            buttons.append(Button(t, text = 'Press me', command = loss))
    for but in buttons:
        but.pack(fill = 'both', expand = 'YES')

    t.mainloop()
def hit():
    for but in buttons:
        but.destroy()
    global lab, score, counter
    score = score + 1
    counter = counter + 1
    lab = Label(t, text = 'You have scored!!! Current score = ' + str(score))
    lab.pack(fill = 'both', expand = 'YES')
    t.after(1000, restart)
def loss():
    for but in buttons:
        but.destroy()
    global lab, score, counter
    counter = counter + 1
    lab = Label(t, text='You have missed! Current score = ' + str(score))
    lab.pack(fill='both', expand='YES')
    t.after(1000, restart)

def restart():
    global lab
    if counter < 30 and score < 5:
        lab.destroy()
        insert_buttons(8)
    elif counter >= 30 and score < 5:
        lab = Label(t, text='You have lost please play again!')
        lab.pack(fill = 'both', expand = 'YES')
    elif counter < 30 and score >= 5:
        lab = Label(t, text='You have won! Congratulations!')
        lab.pack(fill='both', expand='YES')

### --- MAIN PROGRAMME --- ###
global score, counter
counter = 0
score = 0
t = Tk()
t.title('Wybierz przycisk')
t.geometry('300x350')
insert_buttons(8)


