from colorama import Fore, Back, Style
from os.path import exists
import re, json
from abc import ABC, abstractmethod


class List:
    def __init__(self, name):
        self.name = name
        self.list = []
        if not re.search('[a-zA-Z]', name):
            raise NameError()

    def priority(self, index, priority):
        if priority == 'urgent':
            self.list[index].category = Urgent()
        elif priority == 'intermediate':
            self.list[index].category = Intermediate()
        elif priority == 'trivial':
            self.list[index].category = Trivial()

    def add(self, newToDo):
        self.list.append(newToDo)

    def set_achieved(self, index, achieved):
        self.list[index].set_achieved(achieved=achieved)

    def remove(self, index):
        self.list.pop(index)

    def change_category(self, index, category):
        self.list[index].set_category(category)

    def display(self):
        for i,el in enumerate(self.list):
            achieved = 'not achieved'
            if el.achieved:
                achieved = 'achieved'
            print(el.category.get_color()+str(i),el.name,achieved,Style.RESET_ALL)

    def get_list(self):
        return self.list

class JsonList(List):
    def __init__(self, name):
        List.__init__(self, name)
        self.filename = name + '.json'
        if exists(self.filename):
            self.list = self.read()
        else:
            self.store()

    def add(self, newToDo):
        self.list.append(newToDo)
        self.store()

    def remove(self, index):
        self.list.pop(index)
        self.store()

    def store(self):
        new_list = []
        for el in self.list:
            new_list.append(self.convertToDo(el))
        dict_to_store = {
            'name': self.name,
            'list': new_list
        }
        json_to_store = json.dumps(dict_to_store, indent=4)
        with open(self.filename,'w') as file:
            file.write(json_to_store)

    def convertToDo(self, to_do):
        category = {
            'name': to_do.category.name,
            'color': to_do.category.color
        }
        new_to_do = {
            'category': category,
            'name': to_do.name,
            'achieved': to_do.achieved
        }
        return new_to_do

    def read(self):
        f = open(self.filename)
        data = json.load(f)
        list = []
        self.name = data['name']
        for el in data['list']:
            if el['category']['name'] == 'Urgent':
                list.append(ToDo(el['name'], Urgent()))
            elif el['category']['name'] == 'Trivial':
                list.append(ToDo(el['name'], Trivial()))
            if el['category']['name'] == 'Intermediate':
                list.append(ToDo(el['name'], Intermediate()))
        f.close()
        return list

class ToDo:
    def __init__(self, name, category):
        assert len(name) >= 2
        self.name = name
        self.achieved = False
        self.category = category

    def set_achieved(self, achieved):
        self.achieved = achieved

    def set_category(self,category):
        self.category = category


class Category(ABC):
    # def __init__(self, color, name):
    #     self.color = color
    #     self.name = name
    def get_color(self):
        return Fore.__dict__[self.color.upper()]

class Urgent(Category):
    # def __init__(self, color, name):
    #     Category.__init__(self, color, name)
    name = 'Urgent'
    color = 'RED'

class Trivial(Category):
    name = 'Trivial'
    color = 'GREEN'

class Intermediate(Category):
    name = 'Intermediate'
    color = 'BLUE'
