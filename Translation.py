import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize Translator
translator = Translator()

def translate_text():
    """Translate input text into the selected target language."""
    source_text = text_input.get("1.0", tk.END).strip()
    target_lang = target_lang_combo.get()

    if not source_text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    try:
        translated = translator.translate(source_text, dest=target_lang)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation Failed: {e}")

# Create the main window
root = tk.Tk()
root.title("KESAVAN's Translator")
root.geometry("600x400")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="KESAVAN's Translator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input Text Box
text_input = tk.Text(root, height=5, width=60)
text_input.pack(pady=5)

# Target Language Selection
lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

tk.Label(lang_frame, text="Translate to: ").pack(side=tk.LEFT)
target_lang_combo = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), state="readonly", width=20)
target_lang_combo.set("Select Language")
target_lang_combo.pack(side=tk.LEFT, padx=5)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, bg="green", fg="white", font=("Arial", 12, "bold"))
translate_button.pack(pady=10)

# Output Text Box
text_output = tk.Text(root, height=5, width=60, bg="#f0f0f0")
text_output.pack(pady=5)

# Run the application
root.mainloop()
