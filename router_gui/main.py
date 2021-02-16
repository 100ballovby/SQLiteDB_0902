from tkinter import *
from tkinter.ttk import Treeview

app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

lbl_search = Label(frame_search, text='Искать по названию',
                   font=('bold', 14), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)

hostname_search = StringVar()
hostname_search_entry = Entry(frame_search, textvariable=hostname_search)
hostname_search_entry.grid(row=0, column=1, sticky=W)

query_search = StringVar()
query_search.set("SELECT * FROM routers WHERE ram > 1024")
query_search_entry = Entry(frame_search,
                           textvariable=query_search,
                           width=40)
query_search_entry.grid(row=1, column=1)

app.mainloop()
