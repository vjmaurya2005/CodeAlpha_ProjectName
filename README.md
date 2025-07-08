# CodeAlpha_ProjectName
This project is part of CodeAlpha Artificial Intelligence(AI) Internship. It is a language translation tool that allow users to translate the language one to another using Tkinter based GUI in python.
# CodeAlpha AI Internship – 
Task 1-Language Translation Tool

##Language Translation Tool
This is a simple language translation desktop app created as part of the CodeAlpha AI Internship. It allows users to enter text, select source and target languages, and view the translated output instantly. It can Translate between multiple languages ,User-friendly interface using Tkinter, Uses Google Translate API.

How to Run:
1)Install Python

2)Install Required Libraries using the file requirement_using_GoogleAPI.txt

3)Open the file code googletranslator.py & copy this code to your VS code or Pythonn & save it.

4)Run the Program: python googletranslator.py from command prompt using my file python googletranslator.py

import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
# Create the main window
win = tk.Tk()
win.title("Language Translator")
win.geometry("500x400")
# Translator object
translator = Translator()

# Function to translate
def translate():
    from_lang = language_codes[from_lang_box.get()]
    to_lang = language_codes[to_lang_box.get()]
    text = input_box.get("1.0", tk.END)
    result = translator.translate(text, src=from_lang, dest=to_lang)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result.text)
# Convert language codes to full names
language_names = [lang.title() for lang in LANGUAGES.values()]
language_codes = {lang.title(): code for code, lang in LANGUAGES.items()}
# Input label and box
tk.Label(win, text="Enter text:").pack()
input_box = tk.Text(win, height=5, width=50)
input_box.pack()
# Language selection
tk.Label(win, text="From:").pack()
from_lang_box = ttk.Combobox(win, values=language_names)
from_lang_box.set("English")
from_lang_box.pack()
tk.Label(win, text="To:").pack()
to_lang_box = ttk.Combobox(win, values=language_names)
to_lang_box.set("Hindi")
to_lang_box.pack()
# Translate button
tk.Button(win, text="Translate", command=translate).pack(pady=10)
# Output label and box
tk.Label(win, text="Translation:").pack()
output_box = tk.Text(win, height=5, width=50)
output_box.pack()
# Run the app
win.mainloop()
