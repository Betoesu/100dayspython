from tkinter import * 

def calculate():
    miles = float(milesInput.get())
    km = miles * 1.609
    kmNumberLabel.config(text=km)


window = Tk()
window.title("Mile to Km Converter")


milesInput = Entry()
milesInput.grid(row=0, column=1)

emptyLabel = Label(text="")
emptyLabel.config(padx=10,pady=10)
emptyLabel.grid(row=0, column=0)

milesLabel = Label(text="Miles")
milesLabel.config(padx=10,pady=10)
milesLabel.grid(row=0, column=2)

isEqualtoLabel = Label(text="is equal to")
isEqualtoLabel.config(padx=10,pady=10)
isEqualtoLabel.grid(row=1, column=0)

kmNumberLabel = Label(text=0)
kmNumberLabel.config(padx=10,pady=10)
kmNumberLabel.grid(row=1,column=1)

kmLabel = Label(text="Km")
kmLabel.config(padx=10,pady=10)
kmLabel.grid(row=1,column=2)

calculateButton = Button(text="Calculate", command=calculate)
calculateButton.config(padx=10,pady=10)
calculateButton.grid(row=2,column=1)


window.mainloop()