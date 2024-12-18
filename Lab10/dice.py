import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random
import os

def roll_dice():
    result = random.randint(1, 6)
    dice_image = dice_images[result - 1]
    label_result.config(image=dice_image)
    label_result.image=dice_image

root = tk.Tk()
root.title("Rzut sześcienną kostką")
root.geometry("400x250")

script_dir = os.path.dirname(os.path.abspath(__file__))
dice_folder = os.path.join(script_dir, "Dice")

dice_images = []
for i in range(1, 7):
    image_path = os.path.join(dice_folder, f"{i}.png")
    img = Image.open(image_path)
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
    dice_images.append(ImageTk.PhotoImage(img))

label_description = tk.Label(root, text="Kliknij przycisk, aby rzucić kostką", font=("Arial", 14))
label_description.pack(pady=10)

button = tk.Button(root, text="Rzuć kostką", font=("Arial", 12), command=roll_dice)
button.pack(pady=10)

label_result = tk.Label(root)
label_result.pack(pady=10)

root.mainloop()

