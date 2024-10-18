import mysql.connector
from tkinter import *
from tkinter import messagebox

# Establish connection to MySQL database
con = mysql.connector.connect(
    user='root', host='localhost', database='studentregistration', passwd='Susheel@123'
)
mycursor = con.cursor()

# Define the Clear Function for clear button
def clear_entry():
    e1.delete(0, END)
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    var_gender.set(0)

# Define the Submit button function
def submit_form():
    idnumber = e1.get()  # Retrieve idnumber from Entry e1
    FullName = entry_1.get()  # Retrieve FullName from Entry entry_1
    Email = entry_2.get()  # Retrieve Email from Entry entry_2
    Age = entry_3.get()  # Retrieve Age from Entry entry_3

    sql = "INSERT INTO student (idnumber, FullName, Email, Age) VALUES (%s, %s, %s, %s)"
    values = (idnumber, FullName, Email, Age)

    try:
        mycursor.execute(sql, values)
        con.commit()  # Commit changes to the database
        messagebox.showinfo("Success", "Registration form Successfully Submitted.")
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Student ID already exists.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Something went wrong: {err}")

# GUI setup
base = Tk()
base.geometry('500x500')
base.title("Registration ")

# Labels and Entry fields
Label(base, text=" Student Records", width=20, font=("bold", 20)).place(x=90, y=15)

Label(base, text="Id Number", width=20, font=("bold", 10)).place(x=80, y=80)
e1 = Entry(base)
e1.place(x=240, y=80)

Label(base, text="Full Name", width=20, font=("bold", 10)).place(x=80, y=130)
entry_1 = Entry(base)
entry_1.place(x=240, y=130)

Label(base, text="Email", width=20, font=("bold", 10)).place(x=68, y=180)
entry_2 = Entry(base)
entry_2.place(x=240, y=180)

Label(base, text="Gender", width=20, font=("bold", 10)).place(x=70, y=230)
var_gender = IntVar()
Radiobutton(base, text="Male", padx=5, variable=var_gender, value=1).place(x=235, y=230)
Radiobutton(base, text="Female", padx=20, variable=var_gender, value=2).place(x=290, y=230)

Label(base, text="Age:", width=20, font=("bold", 10)).place(x=70, y=280)
entry_3 = Entry(base)
entry_3.place(x=240, y=280)

# Submit button
Button(base, text='Submit', width=20, bg='green', fg='white', command=submit_form).place(x=90, y=380)

# Clear button
Button(base, text='Clear', width=20, bg='red', fg='white', command=clear_entry).place(x=280, y=380)

base.mainloop()

print("Registration form is created successfully...")
