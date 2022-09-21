from tkinter import *

# Classes and Functions definition


def greet():
    return "Hello World!"


if __name__ == "__main__":
    root = Tk()
    root.title("Welcome")

    # Main Program

    root.geometry("320x240")

    label = Label(root, text=greet(), font=("JetBrains Mono", 14))
    label.pack()

    txt = Entry(root, width=5)
    txt.pack()
    # txt.focus()

    root.mainloop()
    print("Application exited successfully.")
