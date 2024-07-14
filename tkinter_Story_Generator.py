import tkinter as tk
import random

# Sample data for random story generation
characters = ["a dragon", "a wizard", "a knight", "a princess"]
settings = ["in a dark forest", "in a magical kingdom", "on a distant planet", "in a bustling city"]
plots = ["finds a hidden treasure", "battles an evil sorcerer", "goes on a quest to save the world", "discovers a secret power"]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    plot = random.choice(plots)
    story = f"Once upon a time, {character} {setting} {plot}."
    story_text.delete("1.0", tk.END)
    story_text.insert(tk.END, story)

# Create the main window
root = tk.Tk()
root.title("Random Story Generator")

# Create and place the widgets
story_label = tk.Label(root, text="Your Random Story:")
story_label.pack(pady=10)

story_text = tk.Text(root, height=10, width=50)
story_text.pack(pady=10)

generate_button = tk.Button(root, text="Generate Story", command=generate_story)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
