from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
from DisplayData import displayData

allData = []

# Data Validation 

# For Dropdown if the variable is equal to the orginal set value throw an error

def submitData():
    
    # Getting Data from Entry Boxes
    # Todo: Use Try Except for Data Validation 
    
    # Data Validation
    while True:

    # * Checking that Customer's Name doesn't include Numbers

        customer = customerName.get()

        if customer.isalpha() == False:
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
            messagebox.showerror(title="Reciept Number Error", message="Item Hired must only include numbers")
            break

    # * New Entry Creation

        userEntry = dict(
            CustomerName = customer, 
            RecieptNumber = reciept, 
            ItemHired = item,
            NumberHired = itemHired,
            id = random.random()
            )
        
        allData.append(userEntry)
        displayData(dataWindow, allData)
        break

def deleteEntry(id):

    # ! Ask user if they want to delete this or not
    # TODO use a delete message box and based of the boolean value from it either do nothing or run the for loop

    global allData
    newArr = []

    for item in allData:
        if item.get("id") != id:
            newArr.append(item)

    allData = newArr

    displayData(dataWindow, allData)
    

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

# Data Window
dataWindow = Toplevel()

# Hiding Data Window
dataWindow.withdraw()

# Window Geometry 
main.geometry("550x450")
dataWindow.geometry("550x450")

# Customers Name
Label(main, text="Customer Name").grid(column=0, row=0, sticky=W)
customerName = Entry(main, width=17)
customerName.grid(column=1, row=0)

# Recipt Number
Label(main, text="Receipt Number").grid(column=0, row=1, sticky=W)
recieptNumber = Entry(main, width=17)
recieptNumber.grid(column=1, row=1)

# Item Hired
itemHiredVar = StringVar()
itemHiredVar.set("...")

itemHiredDropDown = OptionMenu(main, itemHiredVar, *items)
itemHiredDropDown.configure(width=13)
Label(main, text="Item Hired").grid(column=0, row=2, sticky=W)
itemHiredDropDown.grid(column=1, row=2)

# Number Hired
Label(main, text="Number Hired").grid(column=0, row=3, sticky=W)
numberHired = Entry(main, width=17)
numberHired.grid(column=1, row=3)

# Show Data & Add Data

Button(main, text="Show Entries", command=displayData).grid(column=0, row=4, sticky=W)
Button(main, text="Submit Entry", command=submitData).grid(column=1, row=4, sticky=W)

main.mainloop()