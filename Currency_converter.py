import tkinter as tk
from tkinter import messagebox

# Function to perform currency conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())
        converted_amount = amount * rate
        result_label.config(text=f"Converted amount: {converted_amount:.2f} {to_currency.get()}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create the main application window
app = tk.Tk()
app.title("Courage's Currency Converter")
app.geometry("400x300")  # Set window size

# Currency conversion form
amount_label = tk.Label(app, text="Amount:", font=("Arial", 14))
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(app, font=("Arial", 14))
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = tk.Label(app, text="From Currency:", font=("Arial", 14))
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency = tk.Entry(app, font=("Arial", 14))
from_currency.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = tk.Label(app, text="To Currency:", font=("Arial", 14))
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency = tk.Entry(app, font=("Arial", 14))
to_currency.grid(row=2, column=1, padx=10, pady=10)

rate_label = tk.Label(app, text="Exchange Rate:", font=("Arial", 14))
rate_label.grid(row=3, column=0, padx=10, pady=10)

rate_entry = tk.Entry(app, font=("Arial", 14))
rate_entry.grid(row=3, column=1, padx=10, pady=10)

convert_button = tk.Button(app, text="Convert", command=convert_currency, font=("Arial", 14))
convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the application
app.mainloop()
