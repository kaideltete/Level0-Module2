import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    from tkinter import messagebox, simpledialog, Tk
    import random
    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3

    # If the random number is 0

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer

    v1=random.randint(0,3)
    print(v1)

    if (v1==0):
        messagebox.showinfo(message="yes!")

    if (v1==1):
        messagebox.showinfo(message=" no.")

    if (v1==2):
        messagebox.showinfo(message=" google it.")

    if (v1==3):
        messagebox.showinfo(message="why are you asking me?")
