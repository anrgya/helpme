import tkinter as tk
from tkinter import messagebox
from app_logic import add_user_logic, get_users_logic

# Fungsi untuk menambahkan pengguna
def add_user():
    name = entry_name.get()
    age = entry_age.get()

    if not name or not age:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    success, message = add_user_logic(name, age)

    if success:
        messagebox.showinfo("Success", message)
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        display_users()  
    else:
        messagebox.showerror("Error", message)

# Fungsi untuk menampilkan daftar pengguna
def display_users():
    listbox_users.delete(0, tk.END)

    users = get_users_logic()
    if users:
        for user in users:
            listbox_users.insert(tk.END, f"Name: {user[0]}, Age: {user[1]}")
    else:
        listbox_users.insert(tk.END, "No users found.")

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("User Management")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Gaya font dan warna
font_title = ("Helvetica", 16, "bold")
font_label = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")
bg_color = "#ffffff"
button_color = "#4CAF50"
button_fg = "#ffffff"

# Label judul aplikasi
label_title = tk.Label(root, text="User Management", font=font_title, bg="#f0f0f0", fg="#333333")
label_title.pack(pady=10)

# Frame untuk input nama dan umur
frame_input = tk.Frame(root, bg=bg_color, padx=20, pady=10, relief=tk.RIDGE, bd=2)
frame_input.pack(pady=10)

# Label dan entry untuk nama
label_name = tk.Label(frame_input, text="Name:", font=font_label, bg=bg_color)
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(frame_input, font=font_label)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Label dan entry untuk umur
label_age = tk.Label(frame_input, text="Age:", font=font_label, bg=bg_color)
label_age.grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(frame_input, font=font_label)
entry_age.grid(row=1, column=1, padx=10, pady=10)

# Tombol Add User
btn_add = tk.Button(root, text="Add User", command=add_user, font=font_button, bg=button_color, fg=button_fg, padx=10, pady=5)
btn_add.pack(pady=10)

# Listbox untuk menampilkan pengguna
label_users = tk.Label(root, text="User List", font=font_label, bg="#f0f0f0", fg="#333333")
label_users.pack(pady=10)

listbox_users = tk.Listbox(root, font=font_label, height=8, width=40, bd=2, relief=tk.RIDGE)
listbox_users.pack(padx=20, pady=10)

# Menampilkan pengguna
display_users()

root.mainloop()
