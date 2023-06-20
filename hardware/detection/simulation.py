import tkinter as tk
import random

# Function to generate a random number and update the compartments
def generate_number():
    number = random.randint(1, 4)
    
    # Update the color of the compartments
    for compartment in compartments:
        compartment.config(bg="white")
    
    # Update the color of the compartment corresponding to the generated number
    compartments[number-1].config(bg="red")

# Create the Tkinter window
window = tk.Tk()
window.title("Number Game")

# Create the compartments
compartments = []
for i in range(4):
    compartment = tk.Label(window, text=str(i+1), font=("Arial", 24), width=10, height=5, relief="solid")
    compartment.grid(row=0, column=i, padx=10, pady=10)
    compartments.append(compartment)

# Create the button to generate a number
generate_button = tk.Button(window, text="Generate", font=("Arial", 18), command=generate_number)
generate_button.grid(row=1, columnspan=4, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
