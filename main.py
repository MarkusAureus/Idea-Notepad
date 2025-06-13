# --- Standard Library Imports ---
from tkinter import *
import os
from tkinter import messagebox # Import messagebox for showing errors

# --- GUI Initialization ---
# Create the main application window (root).
window = Tk()
window.title("Idea Archive")
window.minsize(1125, 995)
window.resizable(width=False, height=False) # Lock the window size.

# --- Background Image Setup ---
# Use a Canvas widget to place a background image.
try:
    background = PhotoImage(file="images/space.png")
    canvas = Canvas(window, width=1125, height=995)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor=NW, image=background)
except TclError:
    print("Warning: Could not load background image 'images/space.png'.")

# --- Core Functions ---

def save_it():
    """
    Saves the content of the Text widget to a file.
    The filename and extension are taken from the corresponding entry fields.
    """
    text_content = note_list.get(1.0, END)
    file_name = name_input.get().strip()
    file_type = type_input.get().strip()

    # Validate that the user has provided a filename.
    if not file_name:
        messagebox.showerror("Error", "Please enter a name for the file.")
        return
    if not file_type:
        # Default to .txt if no extension is provided.
        file_type = "txt"

    # Define a safe directory to save files (e.g., user's Documents folder).
    save_directory = os.path.expanduser("~/Documents")
    if not os.path.exists(save_directory):
        os.makedirs(save_directory) # Create the directory if it doesn't exist.

    file_path = os.path.join(save_directory, f"{file_name}.{file_type}")

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_content)
        messagebox.showinfo("Success", f"File saved successfully at:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")


def open_file():
    """
    Opens a specified file and loads its content into the Text widget.
    """
    file_name = name_input.get().strip()
    file_type = type_input.get().strip()

    if not file_name:
        messagebox.showerror("Error", "Please enter the name of the file to open.")
        return
    if not file_type:
        file_type = "txt"

    # Assume the file is in the same safe directory.
    save_directory = os.path.expanduser("~/Documents")
    file_path = os.path.join(save_directory, f"{file_name}.{file_type}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            note_list.delete(1.0, END) # Clear existing content first.
            note_list.insert(END, file.read())
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")


def clear_it():
    """
    Clears all text from the main Text widget and input fields.
    """
    note_list.delete(1.0, END)
    name_input.delete(0, END)
    type_input.delete(0, END)


# --- UI Widget Creation and Placement ---

# Main Text widget for notes.
note_list = Text(window, width=58, height=29, bg="#CCCDC6", fg="black",
                 font=("Helvetica", 20), borderwidth=7, relief="groove",
                 wrap="word") # 'wrap="word"' improves text wrapping.
note_list.focus()
note_list.place(x=110, y=100)

# Vertical Scrollbar for the Text widget.
# Note: The original scroll_y function is not needed; the scrollbar's command can be set directly.
scrollbar_y = Scrollbar(window, bg="#318CE7", cursor="hand2", command=note_list.yview)
scrollbar_y.place(x=995, y=100, width=20, height=830)

# Connect the Text widget's scroll command to the scrollbar.
note_list.config(yscrollcommand=scrollbar_y.set)

# --- Labels for Input Fields ---
name_file = Label(window, text="Name file", bg="black", fg="white", font=("Helvetica", 15,), width=16)
name_file.place(x=80, y=20)

type_file = Label(window, text="Type file", bg="black", fg="white", font=("Helvetica", 15,), width=16)
type_file.place(x=320, y=20)


# --- Entry Fields for Filename and Type ---
name_input = Entry(window, bg="black", width=15, fg="white", font=("Helvetica", 15),
                   borderwidth=7, relief="ridge")
name_input.place(x=113, y=50)

type_input = Entry(window, bg="black", width=15, fg="white", font=("Helvetica", 15),
                   borderwidth=7, relief="ridge")
type_input.place(x=320, y=50)


# --- Action Buttons (Save, Open, Clear) ---
save_button = Button(window, text="Save it", bg="#63645E", fg="white", font=("Helvetica", 14, "bold"),
                     width=10, borderwidth=5, relief="raised", activebackground="#03AC13",
                     activeforeground="white", command=save_it, cursor="hand2")
save_button.place(x=527, y=47.5)

open_button = Button(window, text="Open file", bg="#63645E", fg="white", font=("Helvetica", 14, "bold"),
                     width=10, borderwidth=5, relief="raised", activebackground="#318CE7",
                     activeforeground="white", command=open_file, cursor="hand2")
open_button.place(x=703, y=47.5)

clear_button = Button(window, text="Clear up", bg="#C21807", fg="white", font=("Helvetica", 14, "bold"),
                      width=10, borderwidth=5, relief="raised", activebackground="#FF0800",
                      activeforeground="white", command=clear_it, cursor="hand2")
clear_button.place(x=880, y=47.5)


# --- Main Event Loop ---
# Starts the Tkinter event loop, which listens for user actions.
window.mainloop()
