import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi_label.config(text=f"Your BMI: {bmi:.2f}")
        if bmi < 18.5:
            category_label.config(text="Category: Underweight", fg="blue")
        elif 18.5 <= bmi < 24.9:
            category_label.config(text="Category: Normal weight", fg="green")
        elif 25 <= bmi < 29.9:
            category_label.config(text="Category: Overweight", fg="orange")
        else:
            category_label.config(text="Category: Obesity", fg="red")

        save_data(weight, height, bmi)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def save_data(weight, height, bmi):
    with open("bmi_data.txt", "a") as file:
        file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}\n")

root = tk.Tk()
root.title("BMI Calculator")

label_weight = tk.Label(root, text="Enter weight (kg):")
label_weight.grid(row=0, column=0, padx=5, pady=5)

entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

label_height = tk.Label(root, text="Enter height (m):")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


bmi_label = tk.Label(root, text="")
bmi_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

category_label = tk.Label(root, text="")
category_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

