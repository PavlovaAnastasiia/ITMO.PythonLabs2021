from tkinter import *
from Deletion import *
from Addition import *
from Sorting import *
from ShowInfo import *
from FindCategory import *
from tkinter import messagebox

def edit_click():
    messagebox.showinfo("Warning", "You have decided to add some info.")
    addition()

root = Tk()
root.geometry("200x150")
root.resizable(width=False, height=False)
root.title("Shopping list")

lbl = Label(root, text="Hello :)", fg="red", bg="pink", font=("Times New Roman", 20))
lbl.grid(column=0, row=1)
lbl = Label(root, text="Please, choose an action ", font=("Times New Roman", 14))
lbl.grid(column=0, row=2)
lbl = Label(root, text="in the section above!", font=("Times New Roman", 14))
lbl.grid(column=0, row=3)

mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)

mainmenu.add_cascade(label="What would you like to do?", menu=filemenu)

filemenu.add_command(label="Add", command=edit_click())
filemenu.add_command(label="Show all", command=show_info())
filemenu.add_command(label="Show by category", command=show_by_category())
filemenu.add_command(label="Show by min->max", command=sorting())
filemenu.add_command(label="Delete", command=deletion)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

root.mainloop()