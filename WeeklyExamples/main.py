# from dbConfigPROD import create_conn
from dbConfig import create_conn
import tkinter as tk
import customtkinter as ctk

# Create our connection to the db
conn = create_conn()
cursor = conn.cursor()


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

# Create a function to retrieve all records and display them in the text widget.
def display_records():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    msg = ""
    for record in records:
        msg += f"ID: {record[0]}, First Name: {record[2]}, Last Name: {record[1]}, Email: {record[3]}\n"
    
    text_widget.delete("1.0", tk.END)  # Clear existing content
    text_widget.insert(tk.END, msg)

    
    

# Display records button
display_button = ctk.CTkButton(master=window, text="Display Records", command=display_records)
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


#----------------------------------------------------------------------------------
# Search Functionality
# ---------------------------------------------------------------------------------
def search_record():
    student_id = studentID_input.get()
    sql = "SELECT * FROM students WHERE studentID = %s"
    val = (student_id,)
    cursor.execute(sql, val)
    record = cursor.fetchone()
    if record:
        firstName_input.delete(0, tk.END)
        firstName_input.insert(0, record[2])
        lastName_input.delete(0, tk.END)
        lastName_input.insert(0, record[1])
        email_input.delete(0, tk.END)
        email_input.insert(0, record[3])
    else:
        clear_inputs()

search_button = ctk.CTkButton(master=window, text="Search", command=search_record)
search_button.grid(row=4, column=0, padx=10, pady=10)


#---------------------------------------------------------------------
# Update Functionality
# --------------------------------------------------------------------
def update_record():
    student_id = studentID_input.get()
    first_name = firstName_input.get()
    last_name = lastName_input.get()
    email = email_input.get()

    sql = "UPDATE students SET firstName = %s, lastName = %s, email = %s WHERE studentId = %s"
    val = (first_name, last_name, email, student_id)
    cursor.execute(sql, val)
    conn.commit()
    clear_inputs()


update_button = ctk.CTkButton(master=window, text="Update", command=update_record)
update_button.grid(row=4, column=1, padx=10, pady=10)


# ------------------------------------------------------------------------------
# Insert Functionality
# ------------------------------------------------------------------------------
def insert_record():
    first_name = firstName_input.get()
    last_name = lastName_input.get()
    email = email_input.get()

    sql = "INSERT INTO students (firstName, lastName, email) VALUES (%s, %s, %s)"
    val = (first_name, last_name, email)
    cursor.execute(sql, val)
    conn.commit()
    clear_inputs()

def clear_inputs():
    studentID_input.delete(0, tk.END)
    firstName_input.delete(0, tk.END)
    lastName_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
   

insert_button = ctk.CTkButton(master=window, text="Insert", command=insert_record)
insert_button.grid(row=5, column=0, padx=10, pady=10)


# ------------------------------------------------------------------------------
# Delete Functionality
# ------------------------------------------------------------------------------
def delete_record():
    student_id = studentID_input.get()

    sql = "DELETE FROM students WHERE studentId = %s"
    val = (student_id,)
    cursor.execute(sql, val)
    conn.commit()
    clear_inputs()


delete_button = ctk.CTkButton(master=window, text="Delete", fg_color="red", command=delete_record)
delete_button.grid(row=5, column=1, padx=10, pady=10)




window.mainloop()