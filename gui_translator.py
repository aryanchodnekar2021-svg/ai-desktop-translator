import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def perform_translation():
    text = input_box.get("1.0", tk.END).strip()
    target_lang = lang_choice.get()
    
    # Map friendly names to codes
    lang_map = {"Hindi": "hi", "Spanish": "es", "French": "fr", "German": "de"}
    lang_code = lang_map.get(target_lang)

    if not text:
        messagebox.showwarning("Empty Text", "Please type something to translate!")
        return

    try:
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", f"Could not translate: {e}")

# --- Setup the Window ---
root = tk.Tk()
root.title("AI Desktop Translator")
root.geometry("500x450")

# 1. Input Label and Box
tk.Label(root, text="Enter Text:", font=("Arial", 12, "bold")).pack(pady=5)
input_box = tk.Text(root, height=5, width=50)
input_box.pack(pady=5)

# 2. Language Selection Dropdown
tk.Label(root, text="Translate to:", font=("Arial", 10)).pack(pady=5)
lang_choice = ttk.Combobox(root, values=["Hindi", "Spanish", "French", "German"])
lang_choice.current(0) # Default to Hindi
lang_choice.pack(pady=5)

# 3. Translate Button
btn = tk.Button(root, text="Translate Now", command=perform_translation, bg="blue", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=20)

# 4. Output Label and Box
tk.Label(root, text="Result:", font=("Arial", 12, "bold")).pack(pady=5)
output_box = tk.Text(root, height=5, width=50, bg="#f0f0f0")
output_box.pack(pady=5)

root.mainloop()