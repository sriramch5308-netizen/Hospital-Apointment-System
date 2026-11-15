import tkinter as tk
from tkinter import ttk, messagebox


# Main window
root = tk.Tk()
root.title("Hospital Appointment System")
root.geometry("750x550")
root.resizable(False, False)


# ---------------- FUNCTIONS ----------------

appointments = []


def book_appointment():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_combo.get()
    doctor = doctor_combo.get()
    date = date_entry.get()

    if name == "" or age == "" or gender == "" or doctor == "" or date == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number")
        return

    appointment = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Doctor": doctor,
        "Date": date
    }

    appointments.append(appointment)

    table.insert(
        "",
        "end",
        values=(name, age, gender, doctor, date)
    )

    messagebox.showinfo("Success", "Appointment booked successfully!")

    clear_fields()


def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_combo.set("")
    doctor_combo.set("")
    date_entry.delete(0, tk.END)


def delete_appointment():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select an appointment"
        )
        return

    for item in selected:
        table.delete(item)

    messagebox.showinfo(
        "Deleted",
        "Appointment deleted successfully!"
    )


def exit_program():
    root.destroy()


# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="HOSPITAL APPOINTMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


# ---------------- INPUT FRAME ----------------

input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# Patient Name
tk.Label(
    input_frame,
    text="Patient Name:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=8)

name_entry = tk.Entry(
    input_frame,
    width=30,
    font=("Arial", 11)
)

name_entry.grid(row=0, column=1, padx=10)


# Age
tk.Label(
    input_frame,
    text="Age:",
    font=("Arial", 12)
).grid(row=1, column=0, padx=10, pady=8)

age_entry = tk.Entry(
    input_frame,
    width=30,
    font=("Arial", 11)
)

age_entry.grid(row=1, column=1, padx=10)


# Gender
tk.Label(
    input_frame,
    text="Gender:",
    font=("Arial", 12)
).grid(row=2, column=0, padx=10, pady=8)

gender_combo = ttk.Combobox(
    input_frame,
    values=["Male", "Female", "Other"],
    width=28,
    state="readonly"
)

gender_combo.grid(row=2, column=1, padx=10)


# Doctor
tk.Label(
    input_frame,
    text="Doctor:",
    font=("Arial", 12)
).grid(row=3, column=0, padx=10, pady=8)

doctor_combo = ttk.Combobox(
    input_frame,
    values=[
        "Dr. Kumar - General",
        "Dr. Priya - Cardiology",
        "Dr. Ravi - Neurology",
        "Dr. Anitha - Pediatrics"
    ],
    width=28,
    state="readonly"
)

doctor_combo.grid(row=3, column=1, padx=10)


# Date
tk.Label(
    input_frame,
    text="Appointment Date:",
    font=("Arial", 12)
).grid(row=4, column=0, padx=10, pady=8)

date_entry = tk.Entry(
    input_frame,
    width=30,
    font=("Arial", 11)
)

date_entry.grid(row=4, column=1, padx=10)


# ---------------- BUTTONS ----------------

button_frame = tk.Frame(root)
button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Book Appointment",
    command=book_appointment,
    width=18
).grid(row=0, column=0, padx=5)


tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=12
).grid(row=0, column=1, padx=5)


tk.Button(
    button_frame,
    text="Delete",
    command=delete_appointment,
    width=12
).grid(row=0, column=2, padx=5)


tk.Button(
    button_frame,
    text="Exit",
    command=exit_program,
    width=12
).grid(row=0, column=3, padx=5)


# ---------------- TABLE ----------------

table_frame = tk.Frame(root)
table_frame.pack(pady=15)


columns = (
    "Name",
    "Age",
    "Gender",
    "Doctor",
    "Date"
)

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=8
)


for column in columns:
    table.heading(column, text=column)
    table.column(column, width=130)


table.pack()


# ---------------- START PROGRAM ----------------

root.mainloop()