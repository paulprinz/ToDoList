# class Interface:
#     def __init__(self):

import sys
from toDoList import List, JsonList, Urgent, Trivial, Intermediate, ToDo

def interface():
    try:
        to_do_list = JsonList('ToDo')
        while True:
            command = input('Command, please: ')
            if 'add' == command:
                name = input("Give name of to-do please: ")
                to_do_list.add(ToDo(name=name, category=Intermediate()))
            elif 'display' == command:
                to_do_list.display()
            elif 'remove' == command:
                index = input("Index of item to be removed, please: ")
                to_do_list.remove(int(index))
            elif 'done' == command:
                index = input("Index of item that is done, please: ")
                to_do_list.set_achieved(int(index), True)
            elif 'doing' == command:
                index = input("Index of item that is still to do, please: ")
                to_do_list.set_achieved(int(index), False)
            elif 'priority' == command:
                priority = input("What is the priority (urgent, intermediate, trivial), please: ")
                index = input("Index of item, please: ")
                to_do_list.priority(int(index),priority)
            else:
                break
    except NameError as e:
        print(e)

