import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket

    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket


v1=random.randint(0,6)
print(v1)


q1 = simpledialog.askstring(title='guess', prompt="guess a number 0, 1, 2, 3, 4, 5, or 6")





if int(q1) ==v1:
    messagebox.showinfo(message="win!")

elif int(q1) !=v1:
    messagebox.showinfo(message='lose')
