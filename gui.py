# GUI for the to-do app
from tkinter import *
from tkinter import messagebox
from functools import partial
from toDoList import List, JsonList, Urgent, Trivial, Intermediate, ToDo


def add_to_do(entry_add, to_do_list, frame, list):
    name = entry_add.get()
    if (len(name)>1):
        to_do = ToDo(name=name, category=Intermediate())
        to_do_list.add(to_do)
        entry_add.delete(0, "end")
        insert_to_do(to_do, to_do_list, list, len(to_do_list.list)-1, frame)
    else:
        messagebox.showerror('showerror', "Name too short!")

def delete_to_do(to_do_list, list, frame, index):
    to_do_list.remove(index)
    list.delete(index)


def insert_to_do(to_do, to_do_list, list, index, frame):
    achieved = 'not achieved'
    if to_do.achieved:
        achieved = 'achieved'
    list.insert(END, str(index) + ' ' + to_do.name + ' ' + achieved)
    button_del = Button(frame, text="Delete to-do", font=("Times", 16), bg='#c5f776',
                            command=partial(delete_to_do, to_do_list, list, frame, index))
    button_del.pack(side=TOP, fill=BOTH, expand=False, pady=5, padx=5)

def main():
    try:
        to_do_list = JsonList('ToDo')
        window = Tk()
        window.geometry("1300x800+50+50")
        window.title("To-Do List")
        window.config(bg='#223441')
        frame = Frame(window)
        frame.pack(pady=10)
        label = Label(frame,text=to_do_list.name)
        label.pack(pady=10)
        list = Listbox(frame, width=70, height=65, font=("Times", 18), bd=0, fg="#464646",
                       highlightthickness=0, selectbackground="#A6A6A6", activestyle="none")
        list.pack(side=LEFT, fill=BOTH, expand=True)
        for i,el in enumerate(to_do_list.get_list()):
            insert_to_do(el, to_do_list, list, i, frame=frame)
        entry_add = Entry(frame, font=("Times", 20))
        entry_add.pack(pady=20, padx=10)
        button_add = Button(frame, text="Add to-do", font=("Times", 18), bg='#c5f776',
                            command=partial(add_to_do, entry_add, to_do_list, frame, list))
        button_add.pack(side=LEFT, fill=BOTH, expand=True, pady=20, padx=10)
        window.mainloop()
    except NameError as e:
        print(e)


