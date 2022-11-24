from tkinter import *

die = {
0: "🎲",
1: "⚀",
2: "⚁",
3: "⚂",
4: "⚃",
5: "⚄",
6: "⚅",
}

App = Tk()
App.title("Xúc xắc")
dice = Label(App, text=die[0], font=('Times', 100), foreground='white')
dice.grid(row=0, column=0, padx=25, pady=5)

def roll():
	from random import randint
	i = randint(1, 6)
	i1 = randint(1, 6)
	i2 = randint(1, 6)
	msg = Label(App, text=die[i], font=('Time', 100), foreground='white')
	msg.grid(row=0, column=0, padx=25, pady=5)
	msg1 = Label(App, text=die[i1], font=('Time', 100), foreground='white')
	msg1.grid(row=0, column=0, padx=25, pady=5)
	msg2 = Label(App, text=die[i2], font=('Time', 100), foreground='white')
	msg2.grid(row=0, column=0, padx=25, pady=5)

rollB = Button(App, text="Quay", command=roll)
rollB.grid(row=1, column=1)

App.mainloop()