# IMPORT TKINTER MODULE
from Tkinter import *

# MAKE THE GRADE-AVERAGING FUNCTION
def average():
	# GET THE USER-INPUT FROM ENTRY-FORMS AND ASSIGN THEM TO VARIABLES
	Math = SUB_HOLDER[0].get() ; Language = SUB_HOLDER[1].get() ; Science = SUB_HOLDER[2].get() ; History = SUB_HOLDER[3].get()

	# CONVERT STRING DATA INTO INTEGER
	Math = int(Math) ; Language = int(Language) ; Science = int(Science) ; History = int(History)

	# CALCULATE GRADE AND PRESENT IT TO USER WITH LABEL
	add = Math + Language + Science + History
	grade = Label(root, text='Your Grade Average Is: {}'.format(add / 4))
	grade.pack()
	grade.place(x=175, y=200)

# DEFINE SOME WINDOW CONSTATNS
TITLE = 'My Test Application'
DIMENSIONS = '500x300'

root = Tk()

# MAKE AN ARRAY OF SCHOOL SUBJECTS
subjects = ['math', 'language', 'science', 'history']

y_cor = 10

SUB_HOLDER = []

# LOOP THROUGH SUBJECTS ARRAY, MAKE LABELS, AND MAKE ENTRY-FORMS
for subject in subjects:
	label = Label(root, text=subject)
	label.pack()
	label.place(x=100, y=y_cor)
	subject = Entry(root)
	SUB_HOLDER.append(subject)
	subject.pack()
	subject.place(x=175, y=y_cor)
	y_cor += 50

# MAKE THE GRADE BUTTON
submit = Button(root, text='Grade', command=average)
submit.pack()
submit.place(x=225, y=250)

# SETUP WINDOW
root.title(TITLE)
root.geometry(DIMENSIONS)
root.mainloop()