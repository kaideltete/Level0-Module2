import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)



from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window_3 = Tk()
    # Hide the window using the window's .withdraw() method
    window_3.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)

    # 2. Print your variable to the console
    # 3. Get the user to enter something that they think is awesome



    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    for i in range(10):
        v1=random.randint(0,3)
        print(v1)

        if (v1==0):
            messagebox.showinfo(message="your awesome")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
        if (v1==1):
            messagebox.showinfo(message=" your nice")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
        if (v1==2):
            messagebox.showinfo(message=" you are intristing")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        if (v1==3):
            messagebox.showinfo(message=" you are cool")
    # Run the window's .mainloop() method
