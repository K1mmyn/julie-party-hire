from tkinter import *
from tkinter import messagebox

allData = [
    {
      "Customer Name" : "Kim",
      "Reciept Number" : 12345678,
      "Item Hired" : "Spoon",
      "Number Hired": 12
    }
  ]

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
Label(text="Customer Name").grid(column=0, row=0, sticky=W)
Entry().grid(column=1, row=0)

# Recipt Number
Label(text="Receipt Number").grid(column=0, row=1, sticky=W)
Entry().grid(column=1, row=1)

# Item Hired
Label(text="Item Hired").grid(column=0, row=2, sticky=W)
Entry().grid(column=1, row=2)

# Number Hired
Label(text="Number Hired").grid(column=0, row=3, sticky=W)
Entry().grid(column=1, row=3)

# Show Data & 
Button(text="Show Entries", command=displayData).grid(columnspan=1, column=0, row=4, sticky=W)

main.mainloop()