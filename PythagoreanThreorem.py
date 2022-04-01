from math import sqrt
from tkinter import *

root = Tk()
root.title("Pythagorean Theorem Calculator")
root.geometry("450x250")

ValueLabel = Label(root, text="First leg length: ").pack()
e1 = Entry(root, width=25)
e1.pack()
ValueLabel2 = Label(root, text="Second leg length: ").pack()
e2 = Entry(root, width=25)
e2.pack()

answer = Entry(root, width=50)


def solve():
    value = float(e1.get())
    value2 = float(e2.get())
    hypotenuse = sqrt((value**2)+(value2**2))
    answer.delete(0, "end")
    answer.insert(0, "The lenght of the hypotenuse is " + str(round(hypotenuse, 3)) + " units long!")

solveButton = Button(root, text="Solve!", command=solve)
solveButton.pack()

answer.pack()

mainloop()