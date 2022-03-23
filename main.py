from tkinter import *

def calculate ():
	try : 
		if var.get() == 1 :
			first_number = int(FirstInput.get())
			second_number = int(SecondInput.get())
			result = first_number+second_number
			total.set(str(result))
		elif var.get() == 2 :
			first_number = int(FirstInput.get())
			second_number = int(SecondInput.get())
			result = first_number-second_number
			total.set(str(result))
		elif var.get() == 3 :
			first_number = int(FirstInput.get())
			second_number = int(SecondInput.get())
			result = first_number/second_number
			total.set(str(result))
		elif var.get() == 4 :
			first_number = int(FirstInput.get())
			second_number = int(SecondInput.get())
			result = first_number*second_number
			total.set(str(result))
	except (TypeError,ValueError):
		 total.set("Error")


def reset():
	first.set(" ")
	second.set(" ")
	total.set(0)


	

main_windows = Tk()
main_windows.geometry("400x360")
main_windows.title("Calculator")
main_frame = Frame(main_windows)
main_frame.pack()
first = StringVar()
second = StringVar()
total = StringVar()
var = IntVar()
var.set(1)
FirstLabel = Label(main_frame,text ="First Number")
FirstLabel.grid(row = 1 ,column = 1)
FirstInput = Entry(main_frame,textvariable=first)
FirstInput.grid(row = 1, column = 2)
SecondLabel = Label(main_frame,text="Second Number")
SecondLabel.grid(row = 2, column = 1)
SecondInput = Entry(main_frame,textvariable=second)
SecondInput.grid(row = 2, column = 2)
AdditionRadio = Radiobutton(main_frame,text="+",variable = var,value = 1)
AdditionRadio.grid(row = 3,column = 1)
SubstractionRadio = Radiobutton(main_frame,text="-",variable = var,value = 2)
SubstractionRadio.grid(row = 4,column = 1)
DivisionRadio = Radiobutton(main_frame,text="/",variable = var,value = 3)
DivisionRadio.grid(row = 3,column = 2)
MultiplicationRadio = Radiobutton(main_frame,text="*",variable = var,value = 4)
MultiplicationRadio.grid(row = 4,column = 2)
ButtonTest = Button(main_frame,text="Click Me",command=calculate)
ButtonTest.grid(row = 5, column = 1)
ButtonReset = Button(main_frame,text="Reset",command=reset)
ButtonReset.grid(row = 5, column = 2)
ResultLabel = Label(main_frame,textvariable = total )
ResultLabel.grid(row = 6,columnspan = 3)
main_windows.mainloop()