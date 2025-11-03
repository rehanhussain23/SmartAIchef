import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from utils import load_dataset, find_recipes_by_ingredients

# Load dataset
try:
    df = load_dataset("data/recipes_dataset.csv")
except Exception as e:
    messagebox.showerror("Error", f"Failed to load dataset:\n{e}")
    df = None

# App window setup
root = tk.Tk()
root.title("SmartChef AI")
root.geometry("750x600")
root.configure(bg="white")

# ----------- STYLING -----------
accent_color = "#e50914"  # Apple-style red
font_main = ("Helvetica Neue", 12)
font_heading = ("Helvetica Neue", 20, "bold")

# Custom ttk style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background=accent_color, foreground="white", font=font_main, padding=8, relief="flat")
style.map("TButton", background=[("active", "#ff3344")])
style.configure("TLabel", background="white", font=font_main)
style.configure("TEntry", padding=5)
style.configure("TFrame", background="white")

# ----------- HEADER -----------
title_label = ttk.Label(root, text="🍎 SmartChef AI", font=font_heading, background="white", foreground=accent_color)
title_label.pack(pady=15)

desc_label = ttk.Label(root, text="Find recipes based on what’s in your kitchen!", font=("Helvetica Neue", 13),
                       background="white", foreground="#444")
desc_label.pack(pady=5)

# ----------- INPUT SECTION -----------
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

entry_label = ttk.Label(input_frame, text="Enter ingredients (comma separated):")
entry_label.grid(row=0, column=0, padx=5, pady=5)

ingredients_entry = ttk.Entry(input_frame, width=50)
ingredients_entry.grid(row=0, column=1, padx=5, pady=5)

# ----------- RESULTS AREA -----------
result_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=85, height=20,
                                       font=("Helvetica Neue", 11), bg="#fffafa", fg="#222")
result_box.pack(pady=15, padx=10)
result_box.insert(tk.END, "👩‍🍳 Your recipes will appear here...\n")

# ----------- FUNCTIONS -----------
def find_recipes():
    ingredients = ingredients_entry.get()
    if not ingredients:
        messagebox.showwarning("Input Error", "Please enter at least one ingredient.")
        return

    try:
        matches = find_recipes_by_ingredients(df, ingredients)
        result_box.delete("1.0", tk.END)

        if matches.empty:
            result_box.insert(tk.END, "😔 No recipes found for those ingredients.\nTry something else!")
        else:
            for i, row in matches.iterrows():
                result_box.insert(tk.END, f"🍽️ {row['Recipe Name']}\n", "bold")
                result_box.insert(tk.END, f"Ingredients: {row['Ingredients']}\n", "normal")
                result_box.insert(tk.END, f"Instructions: {row['Instructions']}\n\n", "normal")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to find recipes:\n{e}")

# Apply bold tag
result_box.tag_configure("bold", font=("Helvetica Neue", 12, "bold"), foreground=accent_color)
result_box.tag_configure("normal", font=("Helvetica Neue", 11))

# ----------- BUTTON -----------
find_button = ttk.Button(root, text="Find Recipes", command=find_recipes)
find_button.pack(pady=10)

# ----------- FOOTER -----------
footer = ttk.Label(root, text="SmartChef AI • Powered by Data & Love for Cooking",
                   font=("Helvetica Neue", 10), background="white", foreground="#888")
footer.pack(side=tk.BOTTOM, pady=10)

# ----------- RUN -----------
root.mainloop()
