#IMPORT GUI MODULE
from Tkinter import *

#MAKE FUNCTION THAT CALCULATES USER-INPUT
def calculate(entry):
	num1, operator, num2 = entry.widget.get().split()
	num1 = float(num1)
	num2 = float(num2)
	
	# DEFINE CALCULATION METHODS
	if (operator == '+'):
		result = Label(root, text='{} + {} = {}'.format(num1, num2, num1+num2))
	if (operator == '-'):
		result = Label(root, text='{} - {} = {}'.format(num1, num2, num1-num2))
	if (operator == '*'):
		result = Label(root, text='{} * {} = {}'.format(num1, num2, num1*num2))
	if (operator == '/'):
		result = Label(root, text='{} / {} = {}'.format(num1, num2, num1/num2))
	if (operator == '%'):
		result = Label(root, text='{} % {} = {}'.format(num1, num2, num1%num2))

	#DISPLAYS RESULT WIDGET TO SCREEN AND RESIZES IT
	result.pack()
	result.place(x=-75, y=50)
	result.configure(width=50)

#MAKE A VARIABLE FOR THE TK FUNCTION
root = Tk()

# MAKE TITLE FOR APPLICATION
TITLE = Label(root, text='Enter Calculation:')
TITLE.pack()

# MAKE TEXT-FIELD BOX
entry = Entry(root)
entry.pack()
entry.bind('<Return>', calculate)

# SET UP APPLICATION WINDOW
root.geometry('300x300')
root.title('Calculator')
root.mainloop()