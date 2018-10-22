# -*- coding: utf-8 -*-
#checklist.py

#As a user, I want to be able to create, read, update, and destroy items in a checklist

#As a user, I want to be able to mark off colors so I can know that it's already represented

#As a user, I want to be able to see everything in my list at once so I know what is in my list

from termcolor import colored

#creates our list to manipulate
checklist = list()
print(checklist)

#creates item and appends it to list
def create(item):
    checklist.append(item)

#reads item from certain index of list
def read(index):
    try:
        item = checklist[index]
    except IndexError:
        item = "NULL"
    print(item)

    # return item

#update item at certain index of list
def update(index, item):
        checklist[index] = item

#deletes item at certain index of list
def delete(index):
    try:
        checklist.pop(index)
    except IndexError:
        print("out of range")

#prints list
def print_all_items():
    index = 0
    for item in checklist:
        print("{} {}".format(index, item))
        index += 1

#gives item at certain index of list a '√'(check)
def mark_completed(index):
    try:
        checklist[index] = "√" + checklist[index]
        print(colored(checklist[index], "yellow"))
    except IndexError:
        print("NULL")
        return

#function to grab user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#function to select certain option
def select(function_code):

    if function_code == "C" or function_code == "c":
        input_item = user_input("Enter new item: ")
        create(input_item)
        return True

    elif function_code == "R" or function_code == "r":
        item_index = user_input("index #: ")
        item_index = int(item_index)
        read(item_index)
        return True

    elif function_code == "U" or function_code == "u":
        try:
            new_item = (user_input("new item: "))
            index = user_input("at index: ")
            index = int(index)
            update(index, new_item)
            return True
        except IndexError:
            print("out of range")
            return False


    elif function_code == "D" or function_code == "d":
        index = user_input("delete item at index: ")
        index = int(index)
        delete(index)
        return True

    elif function_code == "P" or function_code == "p":
        print_all_items()
        return True

    elif function_code == "Q" or function_code == "q":
        return False

    else:
        print("Unknown Option")


def test():
    create("bronze sword")
    create("wooden shield")

    read(0)
    read(1)

    update(0, "Silver Longsword")
    delete(1)

    read(0)
    read(1)

    print_all_items()
    mark_completed(0)

    select("C")
    select("P")
    select("R")
    select("U")
    select("P")
    select("D")
    select("p")

test()

running = True
while running:
    selection = user_input("Press C to add to list, R to read from list, U to update list, D to delete item from list, P to print list out, or Q to quit: \n" )
    running = select(selection)
