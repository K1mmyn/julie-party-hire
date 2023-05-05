from tkinter import *
from tkinter import messagebox
from tkinter import ttk

allData = [
    {
      "Customer Name" : "Kim",
      "Reciept Number" : 12345678,
      "Item Hired" : "Spoon",
      "Number Hired": 12,
      "id" : 1
    }
  ]

# Data Validation 

def customerNameValidation():
    try:
        isinstance(customerName.get(), str)
        print(customerName.get())
    except:
        pass

def deleteButton(id):
    print(id)

def displayData():
    dataWindow.deiconify()
    row = 1
    Label(dataWindow, text="Customer Name").grid(padx=10,column=0, row=0, sticky=W)
    Label(dataWindow, text="Reciept Number").grid(padx=10,column=1, row=0, sticky=W)
    Label(dataWindow, text="Item Hired").grid(padx=10,column=2, row=0, sticky=W)
    Label(dataWindow, text="Number Hired").grid(padx=10,column=3, row=0, sticky=W)
    for obj in allData:
        Label(dataWindow, text=obj.get("Customer Name")).grid(padx=10,column=0, row=row, sticky=W)
        Label(dataWindow, text=obj.get("Reciept Number")).grid(padx=10,column=1, row=row, sticky=W)
        Label(dataWindow, text=obj.get("Item Hired")).grid(padx=10,column=2, row=row, sticky=W)
        Label(dataWindow, text=obj.get("Number Hired")).grid(padx=10,column=3, row=row, sticky=W)
        Button(dataWindow, text="Delete", command=lambda:deleteButton(obj.get(id))).grid(padx=10,column=4, row=row, sticky=W)
        row += 1

main = Tk()
dataWindow = Toplevel()
dataWindow.withdraw()
main.geometry("550x450")
dataWindow.geometry("550x450")

# Customers Name
Label(main, text="Customer Name").grid(column=0, row=0, sticky=W)
customerName = Entry(main)
customerName.grid(column=1, row=0)

# Recipt Number
Label(main, text="Receipt Number").grid(column=0, row=1, sticky=W)
recieptNumber = Entry(main)
recieptNumber.grid(column=1, row=1)

# Item Hired
Label(main, text="Item Hired").grid(column=0, row=2, sticky=W)
itemHired = Entry(main)
itemHired.grid(column=1, row=2)

# Number Hired
Label(main, text="Number Hired").grid(column=0, row=3, sticky=W)
numberHired = Entry(main)
numberHired.grid(column=1, row=3)

# Show Data & 
Button(main, text="Show Entries", command=customerNameValidation).grid(columnspan=1, column=0, row=4, sticky=W)

main.mainloop()