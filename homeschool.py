'''
CREATED BY: JOEY BURGEE
DATE CREATED: 7-10-17
'''

# IMPORT MODULES
from Tkinter import *

# MAKE THE GRADE-CALCULATION FUNCTION
def grade():
	Math = int(math.get())
	Grammar = int(grammar.get())
	History = int(history.get())
	Science = int(science.get())
	add = Math + Grammar + History + Science
	Grade = Label(root, text='Your Grade Average Is: {}'.format(add/4))
	Grade.pack()
	Grade.place(x=225, y=300)

# ASSIGN VARIABLE TO THE TK FUNCTION
root = Tk()

# MAKE TITLE MESSAGE FOR APPLICATION
TITLE = Label(root, text='Enter Grades For School Subjects:')
TITLE.pack()

# MAKE MATH LABEL AND TEXT-FIELD
math_label = Label(root, text='Math:')
math_label.pack()
math_label.place(x=180, y=50)
math = Entry(root)
math.pack()
math.place(x=220, y=47)

# MAKE GRAMMAR LABEL AND TEXT-FIELD
grammar_label = Label(root, text='Grammar:')
grammar_label.pack()
grammar_label.place(x=155, y=80)
grammar = Entry(root)
grammar.pack()
grammar.place(x=220, y=80)

# MAKE HISTORY LABEL AND TEXT-FIELD
history_label = Label(root, text='History:')
history_label.pack()
history_label.place(x=167, y=110)
history = Entry(root)
history.pack()
history.place(x=220, y=110)

# MAKE SCIENCE LABEL AND TEXT-FIELD
science_label = Label(root, text='Science:')
science_label.pack()
science_label.place(x=167, y=140)
science = Entry(root)
science.pack()
science.place(x=220, y=140)

# MAKE THE GRADE BUTTON
submit = Button(root, text='Grade', command=grade)
submit.pack()
submit.place(x=275, y=350)

# SETUP THE SCREEN
root.geometry('600x400')
root.title('Homeschool Grader')
root.mainloop()