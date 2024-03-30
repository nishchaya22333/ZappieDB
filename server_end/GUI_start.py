import tkinter as tk
from tkinter import messagebox
import loader

def connect_to_database():
    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    connect = loader.connectServer(host, username, password)
    if not connect:
        messagebox.showerror("Error", f"Unable to connect to server")
    else:
        server = loader.getServer()
        load = loader.load(server)
        if not load:
            messagebox.showerror("Error", f"Unable to load database")
        else:
            messagebox.showinfo("Success", "Connected to MySQL database!")
            print("Okay")
        
        

# Create main window
root = tk.Tk()
root.title("MySQL Database Connection")

# Host
host_label = tk.Label(root, text="Host:")
host_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1, padx=10, pady=5)

# Username
username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

# Password
password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Connect button
connect_button = tk.Button(root, text="Connect", command=connect_to_database)
connect_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()