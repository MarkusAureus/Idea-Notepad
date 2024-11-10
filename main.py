from tkinter import *
import os

# ROOT
window = Tk()
window.title("Idea Archive")
window.minsize(1125,995)
window.resizable(width=False,height=False)


background = PhotoImage(file="images/space.png")

canvas = Canvas(window, width=1125,height=995)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=background)




# Function SAVE FILE
def save_it():
    text = note_list.get(1.0, END)
    name = name_input.get()
    type_f = type_input.get()

    with open(os.path.join("/home/secret/Desktop", f"{name}.{type_f}"), "w") as file:
        file.write(text)


# Function OPEN FILE
def open_file():
    name = name_input.get()
    type_f = type_input.get()
    
    with open(f"/home/secret/Desktop/{name}.{type_f}", "r") as file:
        for line in file:
            note_list.insert(END, line)
        

# Function CLEAR ALL
def clear_it():
    note_list.delete(1.0, END)
    name_input.delete(0, END)
    type_input.delete(0, END)


# Function VERTICAL SCROLL - Y
def scroll_y():
    note_list.yview()


# Function HORIZONTAL SCROLL - X
def scroll_x():
    note_list.xview()






# NOTES LIST
note_list = Text(window,width=58, height=29, bg="#CCCDC6", fg="black", font=("Helvetica", 20),borderwidth=7, relief="groove")
note_list.focus()
note_list.place(x=110,y=100)

# SCROLLBAR - VERTICAL
scrollbar_y = Scrollbar(window, bg="#318CE7",command=scroll_y,cursor="hand2")
scrollbar_y.place(x=995, y=100, width=20, height=830)

# CONECTION - NOTES LIST + SCROLLBAR
note_list.config(yscrollcommand=scrollbar_y.set)




# LABELS
name_file = Label(window,text="Name file", bg="black", fg="white", font=("Helvetica",15,), width=16)
name_file.place(x=80,y=20)

type_file = Label(window,text="Type file", bg="black", fg="white", font=("Helvetica",15,), width=16)
type_file.place(x=320,y=20)


# ENTRIES
name_input = Entry(window,bg="black", width=15, fg="white", font=("Helvetica",15), borderwidth=7, relief="ridge")
name_input.place(x=113,y=50)


type_input = Entry(window,bg="black", width=15, fg="white", font=("Helvetica",15), borderwidth=7, relief="ridge")
type_input.place(x=320,y=50)


# BUTTONS
save_button = Button(window,text="Save it", bg="#63645E", fg="white", font=("Helvetica",14,"bold"), width=10, borderwidth=5, relief="raised", activebackground="#03AC13",activeforeground="white" , command=save_it,cursor="hand2")
save_button.place(x=527,y=47.5)

open_button = Button(window,text="Open file", bg="#63645E", fg="white", font=("Helvetica",14,"bold"), width=10, borderwidth=5, relief="raised", activebackground="#318CE7",activeforeground="white" , command=open_file,cursor="hand2")
open_button.place(x=703,y=47.5)

clear_button = Button(window,text="Clear up", bg="#C21807", fg="white", font=("Helvetica",14,"bold"), width=10, borderwidth=5, relief="raised", activebackground="#FF0800",activeforeground="white" ,command=clear_it,cursor="hand2")
clear_button.place(x=880,y=47.5)





window.mainloop()