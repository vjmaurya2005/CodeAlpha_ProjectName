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
