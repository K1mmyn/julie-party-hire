from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

allData = []

def submitData():
    
    # Getting Data from Entry Boxes
    
    # Data Validation
    # TODO create a hide window button on data entry
    # TODO Create quit button

    while True:

    # * Checking that Customer's Name doesn't include Numbers

        FirstName = firstName.get()
        LastName = lastName.get()

        if FirstName.isalpha() == False or LastName.isalpha() == False:

            messagebox.showerror(title="Name Error", message="Name must only include letters from a-z")
            break
    
    # * Asking if the User Input can be converted into an int if not throw Error

        try:
            reciept = int(recieptNumber.get())
        except:
            messagebox.showerror(title="Reciept Number Error", message="Receipt Number must only include numbers")
            break

    # * Checking that item has been changed from orignally set Value

        item = itemHiredVar.get()

        if item == "...":
            messagebox.showerror(title="Item Hired Error", message="Select an Item which has been Hired")
            break
    
    # * Asking if the User Input can be converted into an int if not throw Error

        try:
            itemHired = int(numberHired.get())
        except:
            messagebox.showerror(title="Number Hired Error", message="Number Hired must only include numbers")
            break

    # * New Entry Creation

        userEntry = dict(
            CustomerFirstName = FirstName, 
            CustomerLastName = LastName,
            RecieptNumber = reciept, 
            ItemHired = item,
            NumberHired = itemHired,
            id = random.random()
            )
        
        allData.append(userEntry)
        displayData()

    # * Clearing Entry Boxes

        for widget in main.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, END)
            itemHiredVar.set("...")

        break

def deleteEntry(id):

    # * askyesno return either a truthy value or a falsey value so if askyesno returns a truthy value we run the 
    # * Delete function 

    if messagebox.askyesno(message="Do you want to delete this Entry?", title="Delete Confirmation"):

        global allData
        newArr = []

        for item in allData:
            if item.get("id") != id:
                newArr.append(item)

        allData = newArr
        displayData()

def displayData():
    
    # Clearing Previous Data in Data Window

    for widget in dataWindow.winfo_children():
      if isinstance(widget, Widget):
        widget.destroy()

    # Display Header for Data 
    Label(dataWindow, text="First Name").grid(padx=10,column=0, row=0, sticky=W)
    Label(dataWindow, text="Last Name").grid(padx=10,column=1, row=0, sticky=W)
    Label(dataWindow, text="Reciept Number").grid(padx=10,column=2, row=0, sticky=W)
    Label(dataWindow, text="Item Hired").grid(padx=10,column=3, row=0, sticky=W)
    Label(dataWindow, text="Number Hired").grid(padx=10,column=4, row=0, sticky=W)
    Button(dataWindow, text="Hide Window", command=lambda: hideWindow(dataWindow)).grid(padx=10,column=5, row=0, sticky=W)

    # Revealing Data Window
    dataWindow.deiconify()

    row = 1

    # Printing Data for allData
    for obj in allData:
        Label(dataWindow, text=obj.get("CustomerFirstName").capitalize()).grid(padx=10,column=0, row=row, sticky=W)
        Label(dataWindow, text=obj.get("CustomerLastName").capitalize()).grid(padx=10,column=1, row=row, sticky=W)
        Label(dataWindow, text=obj.get("RecieptNumber")).grid(padx=10,column=2, row=row, sticky=W)
        Label(dataWindow, text=obj.get("ItemHired")).grid(padx=10,column=3, row=row, sticky=W)
        Label(dataWindow, text=obj.get("NumberHired")).grid(padx=10,column=4, row=row, sticky=W)

        Button(dataWindow, text="Delete", command=lambda d=obj.get('id'): deleteEntry(d)).grid(padx=10,column=5, row=row, sticky=W)

        row += 1

def hideWindow(window):
    window.withdraw()

# Avaliable Items for Rental

items = [
    "Spoon",
    "Knife",
    "Fork",
    "Cup",
    "Plate",
]

# Main Window
main = Tk()
main.title("Julie Party Hire")

# Data Window
dataWindow = Toplevel()

# Hiding Data Window
hideWindow(dataWindow)

# Window Geometry 
main.geometry("550x450")
dataWindow.geometry("650x450")

Label(main, text="First Name", font=("Helvetica", 12, "italic", "bold")).grid(pady=10, padx=10, sticky=W, column=0, row=0)
firstName = Entry(main, width=30, font=("Helvetica", 10), bg="ivory3", borderwidth=0)
firstName.grid(padx=20, column=0, row=1, ipady=6)

Label(main, text="Last Name", font=("Helvetica", 12, "italic", "bold")).grid(pady=10, padx=10, sticky=W, column=1, row=0)
lastName = Entry(main, width=30, font=("Helvetica", 10), bg="ivory3", borderwidth=0)
lastName.grid(padx=20, column=1, row=1, ipady=6)

# Recipt Number
Label(main, text="Receipt Number", font=("Helvetica", 12, "italic", "bold")).grid(pady=10, padx=10, sticky=W, column=0, row=2)
recieptNumber = Entry(main, width=30, font=("Helvetica", 10), bg="ivory3", borderwidth=0)
recieptNumber.grid(padx=20, column=0, row=3, ipady=6)

# Item Hired
itemHiredVar = StringVar()
itemHiredVar.set("...")

itemHiredDropDown = OptionMenu(main, itemHiredVar, *items)
itemHiredDropDown.configure(width=26, borderwidth=0, bg="ivory3")
Label(main, text="Item Hired", font=("Helvetica", 12, "italic", "bold")).grid(pady=10, padx=10, column=1, row=2, sticky=W)
itemHiredDropDown.grid(padx=20, column=1, row=3, ipady=6)

# Number Hired
Label(main, text="Number Hired", font=("Helvetica", 12, "italic", "bold")).grid(pady=10, padx=10, column=0, row=4, sticky=W)
numberHired = Entry(main, width=30, font=("Helvetica", 10), bg="ivory3", borderwidth=0)

numberHired.grid(padx=20, column=0, row=5, ipady=6)

# Show Data & Add Data

Button(main, text="Show Entries", font=("Helvetica", 16, "bold"), height=1, bg='black', fg='white', width=20, 
       command=displayData).grid(columnspan=2, pady=20, column=0, row=6)

Button(main, text="Submit Entry", font=("Helvetica", 16, "bold"), height=1, bg="black", fg="white", width=20,
       command=submitData).grid(columnspan=2, column=0, row=7)

main.mainloop()