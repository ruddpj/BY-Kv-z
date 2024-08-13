from tkinter import *
from hexagons import *


def change_player():
    global p
    p = not p
    canvas.itemconfig("indicator", fill=colors[p+1])
    canvas.update()


def show_answer(cnv, ans_t):
    cnv.create_text(250, 400, text=ans_t, font=("Arial", 20), width=300)
    

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


def incorrect(q_num):
    global p
    canvas.itemconfig(pos_q[q_num], fill=colors[3])
    canvas.itemconfig(f"{pos_q[q_num]}text", fill="white")
    canvas.update()


def close_window(cnv, b1, b2, b3, b4):
    cnv.delete("all")
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    Misc.lift(canvas)
    

def submit(dat):
    question_var = question.get()

    if question_var not in pos_q:
        print("Invalid question")
    else:
        t = pos_q.index(question_var)
        q_canvas = Canvas(root, bg="white", height=500, width=500)
        q_canvas.place(x=150, y=150)
        q_canvas.create_text(250, 200, text=dat[t].question, font=("Arial", 20), width=300)

        show = Button(root, text="SHOW", command=lambda: show_answer(q_canvas, dat[t].answer))
        corr = Button(root, text="CORRECT", command=lambda: correct(p, t))
        incorr = Button(root, text="INCORRECT", command=lambda: incorrect(t))
        close = Button(root, text="CLOSE", command=lambda: close_window(q_canvas, show, corr, incorr, close))

        show.place(x=155, y=625)
        corr.place(x=510, y=625)
        incorr.place(x=575, y=625)
        close.place(x=205, y=625)


p = 0
root = Tk()

arr = []
file_1 = open("questions.txt", "r", encoding="utf8")
file_2 = open("answers.txt", "r", encoding="utf8")

i = 0
for i in range(28):
    arr.append(Hexagon(pos_q[i], file_1.readline(), file_2.readline()))

file_1.close()
file_2.close()

canvas = Canvas(root, width=800, height=800, background="white")
canvas.create_oval(750, 750, 780, 780, fill=colors[p+1], tags="indicator")

question = StringVar()
choose = Entry(root, textvariable=question)
button = Button(root, text="SUBMIT", command=lambda: submit(arr))
change = Button(root, text="CHANGE", command=change_player)

canvas.pack()
choose.pack(side=LEFT)
button.pack(side=RIGHT)
change.pack(side=RIGHT)

x, y, r, n = 400, 150, 40, 0
for i in range(7):
    for j in range(i+1):
        canvas.create_polygon((x, y), (x-r, y-(r/2)), (x-r, y-(3/2)*r), (x, y-2*r), (x+r, y-(3/2)*r), (x+r, y-(r/2)),
                              fill=colors[0], outline="black", tags=pos_q[n])
        canvas.create_text((x, y-r), text=pos_q[n].upper(), font="Arial 32", tags=f"{pos_q[n]}text")
        n += 1
        x += 2*r
    y += (3/2)*r
    x = 400-r*(i+1)

p1, p2 = 0, 0
canvas.create_text(50, 675, text="Player 1: ", font="Arial 16")
canvas.create_text(130, 675, text=str(p1), font="Arial 16", tags="p1")
canvas.create_text(50, 700, text="Player 2: ", font="Arial 16")
canvas.create_text(130, 700, text=str(p2), font="Arial 16", tags="p2")

root.mainloop()
