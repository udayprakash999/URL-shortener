import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyshorteners

def shorten():
    selected_service = service_var.get()
    shortener = pyshorteners.Shortener()
    
    try:
        long_url = longurl_entry.get()
        
        
        if selected_service == "TinyURL":
            short_url = shortener.tinyurl.short(long_url)
        elif selected_service == "Is.gd":
            short_url = shortener.isgd.short(long_url)
       
        else:
            raise ValueError("Invalid service selected.")
        
        shorturl_entry.delete(0, tk.END)
        shorturl_entry.insert(0, short_url)
        error_label.config(text="")  
    except Exception as e:
        shorturl_entry.delete(0, tk.END)
        error_label.config(text="Invalid URL or Service. Please try again.")

def copy_to_clipboard():
    short_url = shorturl_entry.get()
    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)
        root.update()
        messagebox.showinfo("Success", "Shortened URL copied to clipboard!")  

def clear_fields():
    longurl_entry.delete(0, tk.END)
    shorturl_entry.delete(0, tk.END)
    error_label.config(text="")  

def save_url():
    long_url = longurl_entry.get()
    short_url = shorturl_entry.get()
    if long_url and short_url:
        with open("shortened_urls.txt", "a") as file:
            file.write(f"{long_url} -> {short_url}\n")
        messagebox.showinfo("Success", "Shortened URL saved to file!")  
    else:
        messagebox.showerror("Error", "No URL to save!")  


root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x500")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 12, "bold"), padding=5)
style.configure("TCombobox", font=("Arial", 12))

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)


longurl_label = ttk.Label(frame, text="Enter Long URL:")
longurl_entry = ttk.Entry(frame, width=40)
service_label = ttk.Label(frame, text="Select Service:")
service_var = tk.StringVar(value="TinyURL")
service_dropdown = ttk.Combobox(frame, textvariable=service_var, values=["TinyURL", "Is.gd"], state="readonly", width=37)
shorturl_label = ttk.Label(frame, text="Shortened URL:")
shorturl_entry = ttk.Entry(frame, width=40)
shorten_button = ttk.Button(frame, text="Shorten URL", command=shorten)
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
reset_button = ttk.Button(frame, text="Clear", command=clear_fields)
save_button = ttk.Button(frame, text="Save URL", command=save_url)
error_label = ttk.Label(frame, text="", foreground="red")


longurl_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
longurl_entry.grid(row=1, column=0, columnspan=2, pady=5)
service_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")
service_dropdown.grid(row=3, column=0, columnspan=2, pady=5)
shorturl_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")
shorturl_entry.grid(row=5, column=0, columnspan=2, pady=5)
shorten_button.grid(row=6, column=0, columnspan=2, pady=20)
copy_button.grid(row=7, column=0, columnspan=2, pady=10)
reset_button.grid(row=8, column=0, columnspan=2, pady=10)
save_button.grid(row=9, column=0, columnspan=2, pady=10)
error_label.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
