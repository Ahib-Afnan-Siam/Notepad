from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.geometry("700x650")
root.title("Notepad")
root.config(bg="lightblue")
root.resizable(False, False)

auto_save_interval = 30000

status_bar = Label(root, text="Ready", anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

def save_file():
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file is None:
        return
    text = str(entry.get(1.0, END))
    file.write(text)
    file.close()
    messagebox.showinfo("Success", "File saved successfully!")
    status_bar.config(text="File saved")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            entry.delete(1.0, END)  
            entry.insert(INSERT, content)
        status_bar.config(text="File opened")

def clear_text():
    entry.delete(1.0, END)
    status_bar.config(text="Text cleared")

def auto_save():
    save_file()
    status_bar.config(text="Auto-saved")
    root.after(auto_save_interval, auto_save)

Button(root, width=20, height=2, bg="#fff", text="Save File", command=save_file).place(x=100, y=5)
Button(root, width=20, height=2, bg="#fff", text="Open File", command=open_file).place(x=300, y=5)
Button(root, width=20, height=2, bg="#fff", text="Clear", command=clear_text).place(x=500, y=5)

entry_width = 80 * 7
entry_x_position = (700 - entry_width) // 2

entry = Text(root, height=30, width=80, wrap=WORD, bg="white", fg="black")
entry.place(x=entry_x_position, y=70)

root.bind_all("<Control-s>", lambda event: save_file())
root.bind_all("<Control-o>", lambda event: open_file())

root.after(auto_save_interval, auto_save)

root.mainloop()
