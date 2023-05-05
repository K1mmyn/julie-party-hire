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