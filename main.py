from tkinter import *
from hexagons import *


def question_getter(q_decide):
    if q_decide:
        f = open("normal.txt", "r")
    else:
        f = open("binary.txt", "r")

    question_arr = []
    for g in range(len(pos_q)):
        question_arr.append(f.readline())
    f.close()
    return question_arr


def question_create():
    bin_q = question_getter(0)
    nor_q = question_getter(1)
    array_questions = [Hexagon(pos_q[g], 0, 0, g, nor_q[g], bin_q[g]) for g in range(len(pos_q))]
    return array_questions


def correct(player, q_num):
    global p1, p2
    if player:
        p2 += 1
        canvas.itemconfig(pos_q[q_num], fill=colors[2])
        canvas.itemconfig("p2", text=str(p2))
        canvas.update()
    else:
        p1 += 1
        canvas.itemconfig(pos_q[q_num], fill=colors[1])
        canvas.itemconfig("p1", text=str(p1))
        canvas.update()


def incorrect(player, q_num):
    global p1, p2, dat_q
    if dat_q[q_num].state:
        if player:
            p1 += 1
            canvas.itemconfig(pos_q[q_num], fill=colors[1])
            canvas.itemconfig("p1", text=str(p2))
            canvas.update()
        else:
            p2 += 1
            canvas.itemconfig(pos_q[q_num], fill=colors[2])
            canvas.itemconfig("p1", text=str(p1))
            canvas.update()
    else:
        canvas.itemconfig(pos_q[q_num], fill=colors[3])
        dat_q[q_num].state = 1


def submit():
    global dat_q, p
    question_var = question.get()
    print(f"{question_var}")

    if question_var not in pos_q:
        print("Invalid question")

    else:
        t = 0
        for t in range(len(pos_q)):
            if question_var == dat_q[t].name:
                break
        q_root = Tk()
        q_canvas = Canvas(q_root, bg="white", height=500, width=500)
        q_canvas.pack()
        if dat_q[t].state == 0:
            q_canvas.create_text(250, 250, text=dat_q[t].normal_q, font=("Arial", 20), width=500)
        else:
            q_canvas.create_text(250, 250, text=dat_q[t].binary_q, font=("Arial", 20), width=500)

        yes_b = Button(q_root, text="YES", command=lambda: correct(p, t), bg="black", fg="white")
        no_b = Button(q_root, text="NO", command=lambda: incorrect(p, t), bg="black", fg="white")
        yes_b.pack(side=LEFT)
        no_b.pack(side=RIGHT)
        if p:
            p = 0
        else:
            p = 1
        q_root.mainloop()


p = 1
root = Tk()
question = StringVar()
dat_q = question_create()
canvas = Canvas(root, width=800, height=800, background="white")
choose = Entry(root, textvariable=question)
button = Button(root, text="Submit", command=lambda: submit())

canvas.pack()
choose.pack(side=LEFT)
button.pack(side=RIGHT)

x, y, r, n = 400, 150, 40, 0
for i in range(7):
    for j in range(i+1):
        canvas.create_polygon((x, y), (x-r, y-r), (x-r, y-2*r), (x, y-3*r), (x+r, y-2*r), (x+r, y-r),
                              fill=colors[dat_q[n].color], outline="black", tags=pos_q[n])
        canvas.create_text((x, y-1.5*r), text=pos_q[n].upper(), font="Arial 32")
        n += 1
        x += 2*r
    y += 2*r
    x = 400-r*(i+1)

p1, p2 = 0, 0
canvas.create_text(50, 675, text="Player 1: ", font="Arial 16")
canvas.create_text(130, 675, text=str(p1), font="Arial 16", tags="p1")
canvas.create_text(50, 700, text="Player 2: ", font="Arial 16")
canvas.create_text(130, 700, text=str(p2), font="Arial 16", tags="p2")

root.mainloop()
