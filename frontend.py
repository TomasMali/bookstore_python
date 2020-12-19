"""
A programm that stores the book information
Title, Author
Year, ISBN
 
USER CAN:

-View all records
-Search an entry
-Add entry
-Update entry
-Delete entry
-Close 
"""
from tkinter import *
import backend
window = Tk()
window.wm_title("Tomas Book Store")
#"""""""""""""""""""""""""""" FUNCTIONS """""""""""""""""""""""""""""


def get_selected_row(event):
    global selected_element
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    selected_element = selected_tuple
    # riempire le entry edit
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    # Inserisce valore quando si seleziona una
    e1.insert(END, selected_element[1])
    e2.insert(END, selected_element[2])
    e3.insert(END, selected_element[3])
    e4.insert(END, selected_element[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
     list1.delete(0,END)
     for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
         list1.insert(END,row)

def command_add_entry():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    search_command()

def command_delete():
    backend.delete(selected_element[0])
    view_command()

def command_update():
    backend.update(selected_element[0], title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    search_command()
    
#"""""""""""""""""""""""""""" LABELS """""""""""""""""""""""""""""
l1 = Label(window, text="Title")
l1.grid(row=0, column=0 )

l2 = Label(window, text="Author")
l2.grid(row=0, column=2 )

l3 = Label(window, text="Year")
l3.grid(row=1, column=0 )

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2 )

#""""""""""""""""""""""""Entry Text"""""""""""""""""""""""""""
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#""""""""""""""""""""""""""""""LIST""""""""""""""""""""""""""""""

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#""""""""""""""""""""""""""""""SCROLLBAR""""""""""""""""""""""""""""""

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#""""""""""""""""""""""""""""""BUTTONS""""""""""""""""""""""""""""""

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entity", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entity", width=12, command=command_add_entry)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=command_update)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=command_delete)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

view_command()

window.mainloop()