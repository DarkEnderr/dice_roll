from tkinter import *
import random

root = Tk()
root.title("Xúc xắc")
root.geometry("400x320")

#dice_faces = [
#"\u2680",
#"\u2681",
#"\u2682",
#"\u2683",
#"\u2684",
#"\u2685",
#]
dice_faces = [
"⚀",
"⚁",
"⚂",
"⚃",
"⚄",
"⚅",
]

dice_label = Label(root, font={"Helvetica", 200})
result_label = Label(root, font={"Helvetica", 40})

def roll():
	dice1 = random.randint(1, 6)
	dice2 = random.randint(1, 6)
	dice3 = random.randint(1, 6)

	dice_label.config(text=f'{dice_faces[dice1 - 1]}{dice_faces[dice2 - 1]}{dice_faces[dice3 - 1]}')
	dice_label.pack()

	sum = dice1 + dice2 + dice3
	result_label.config(text='Tài' if sum > 10 else 'Xỉu', foreground='red' if sum > 10 else 'green')
	result_label.pack(after=dice_label)

b1 = Button(root, text='Quay', foreground='blue', command=roll)
b1.pack()

root.mainloop()