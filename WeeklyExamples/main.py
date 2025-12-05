import tkinter as tk
import customtkinter as ctk


window = ctk.CTk()
window.geometry("850x300")
window.title("My first UI")
window.iconbitmap("WeeklyExamples/uccs.ico")

# -------------------------------------------
# Set the them and appearance
# -------------------------------------------
ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("System")


# -------------------------------------------
# Display records button and text field
# -------------------------------------------

# Display records button
display_button = ctk.CTkButton(master=window, text="Display Records")
display_button.grid(
    row=0,
    rowspan=1,
    column=7,
    padx=5,
    pady=5,
    sticky="e"
)


# Records text widget
text_widget = ctk.CTkTextbox(master=window, width=450)
text_widget.grid(row=1, rowspan=5, column=5, columnspan=3, ipadx=5, padx=5, ipady=5, pady=5, sticky="e")

# --------------------------------------------
# Placeholder dummy column
# --------------------------------------------
placeholder_label = ctk.CTkLabel(master=window, text="")
placeholder_label.grid(row=0, column=2, columnspan=3, ipadx=5, padx=15, ipady=5, pady=5, sticky="e")


# --------------------------------------------
# Input fields and labels
# --------------------------------------------

# StudentID
studentID_label = ctk.CTkLabel(master=window, text="Student ID: ")
studentID_label.grid(row=0, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
studentID_input = ctk.CTkEntry(master=window)
studentID_input.grid(row=0, column=1, ipadx=2, padx=2, ipady=2, pady=2, sticky="w")

# First Name
firstName_label = ctk.CTkLabel(master=window, text="First Name: ")
firstName_label.grid(row=1, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
firstName_input = ctk.CTkEntry(master=window)
firstName_input.grid(row=1, column=1, ipadx=2, padx=2, ipady=2, pady=2, sticky="w")

# Last Name
lastName_label = ctk.CTkLabel(master=window, text="Last Name: ")
lastName_label.grid(row=2, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
lastName_input = ctk.CTkEntry(master=window)
lastName_input.grid(row=2, column=1, ipadx=2, padx=2, ipady=2, pady=2, sticky="w")

# Email
email_label = ctk.CTkLabel(master=window, text="Email: ")
email_label.grid(row=3, column=0, ipadx=1, padx=25, ipady=2, pady=2, sticky="w")
email_input = ctk.CTkEntry(master=window)
email_input.grid(row=3, column=1, ipadx=2, padx=2, ipady=2, pady=2, sticky="w")


# ---------------------------------------------
# Remaining buttons
# ---------------------------------------------

# Search Button
search_button = ctk.CTkButton(master=window, text="Search")
search_button.grid(row=4, column=0, padx=10, pady=10)

# Update Button
update_button = ctk.CTkButton(master=window, text="Update")
update_button.grid(row=4, column=1, padx=10, pady=10)

# Insert Button
insert_button = ctk.CTkButton(master=window, text="Insert")
insert_button.grid(row=5, column=0, padx=10, pady=10)

# Delete Button
delete_button = ctk.CTkButton(master=window, text="Delete", fg_color="red")
delete_button.grid(row=5, column=1, padx=10, pady=10)




window.mainloop()