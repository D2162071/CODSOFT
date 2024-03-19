import string
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string
import random

root = Tk()
root.geometry("500x500")
root.title("Password Generator")
root.config(bg="light blue")
root.resizable(False, False)

def password_generate():
    try:
        length_password = solidboss.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset_password():
    username_entry.delete(0, END)
    password.set("")

all_no = {str(i): str(i) for i in range(1, 31)}

Title = Label(root, text="Password Generator", bg="light blue", fg="black", font=("arial", 20, "bold"))
Title.pack(anchor="center", pady="20px")

username_label = Label(root, text="Username:", bg="light blue", fg="black", font=("ubuntu", 12))
username_label.place(x="20px", y="70px")

username = StringVar()
username_entry = Entry(root, textvariable=username, fg="black", font=("ubuntu", 12))
username_entry.place(x="200px", y="70px")

length = Label(root, text="Length of characters: ", bg="light blue", fg="black", font=("ubuntu", 12))
length.place(x="20px", y="100px")

solidboss = IntVar()
selector = Combobox(root, textvariable=solidboss, state="readonly")
selector['values'] = [l for l in all_no.keys()]
selector.current(7)
selector.place(x="200px",y="102px")

generate_btn = Button(root, text="Generate Password", bg="purple", fg="white", font=("arial", 15), cursor="hand2", command=password_generate)
generate_btn.pack(anchor="center", pady="60px")

reset_btn = Button(root, text="Reset", bg="purple", fg="white", font=("arial", 15), cursor="hand2", command=reset_password)
reset_btn.pack(anchor="center", pady="10px")

result_lable = Label(root, text="Generated Password here: ", bg="light blue", fg="black", font=("ubuntu", 12))
result_lable.place(x="20px", y="170px")

password = StringVar()
password_final = Entry(root, textvariable= password, state="readonly", fg="black", font=("ubuntu", 15))
password_final.place(x="195px", y="170px")

root.mainloop()
