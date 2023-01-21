# import every thing from TKinter

from tkinter import *
from tkinter import messagebox

# creat the main app window
age_app = Tk()

# change App Text
age_app.title("My Calculate Age App")

# Set Dimensions
age_app.geometry("400x200")

# Write Age Label
the_text = Label(age_app, text="Write Your Age", height=2, font=("Arial", 20))
the_text.pack() # Place The Text Into the Main Window

# Age Variables
age = StringVar()

# Set default Value For age
age.set("00")

# Creat The Input for Age
age_input = Entry(age_app, width=2, font=("Arial", 30), textvariable = age)
age_input.pack() # Place The Input Into the Main Window


def calc():

    # Get Afe In Years
    the_age_value = age.get()

    print(the_age_value)

    # Get time Unites
    months = int(the_age_value) * 12
    weeks = months * 4
    days = int(the_age_value) * 365

    line_one = f"Your Age in months is: {months}"
    line_two = f"Your Age in weeks is: {weeks}"
    line_three = f"Your Age in days is: {days}"
     
    all_lines = [line_one, line_two, line_three]

    messagebox.showinfo("Your are in All Time Unites","\n".join(all_lines))

# Creat The Calculate Button
btn = Button(age_app, text="Calculate Age", width=20,
            height=2, bg="red", fg="white", borderwidth=0, command=calc)
btn.pack() # Place Button in The Main Window

#Run App Infinitely
age_app.mainloop()