import tkinter as tk
from tkinter import ttk
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    try:
        long_url = longurl_entry.get()
        short_url = shortener.tinyurl.short(long_url)
        shorturl_entry.delete(0, tk.END)
        shorturl_entry.insert(0, short_url)
    except Exception as e:
        shorturl_entry.delete(0, tk.END)
        shorturl_entry.insert(0, "Error")

        
# main 
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12), padding=5)
style.configure("TButton", font=("Arial", 12, "bold"), padding=5)


frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

longurl_label = ttk.Label(frame, text="Enter Long URL:")
longurl_entry = ttk.Entry(frame, width=40)
shorturl_label = ttk.Label(frame, text="Shortened URL:")
shorturl_entry = ttk.Entry(frame, width=40)
shorten_button = ttk.Button(frame, text="Shorten URL", command=shorten)


longurl_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
longurl_entry.grid(row=1, column=0, columnspan=2, pady=5)
shorturl_label.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")
shorturl_entry.grid(row=3, column=0, columnspan=2, pady=5)
shorten_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
