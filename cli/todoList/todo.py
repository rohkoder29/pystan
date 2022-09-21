"""
TODO app v0.1
"""

# Required Modules
import sys

""" Functions """

# Create a New Task

def create():
    with open("todo.txt", "r") as f:
        todo = input("Create a task: ")
        all_todo = f.readlines()
        if (todo + " -P\n") in all_todo:
            print("Task already created!")
        else:
            with open("todo.txt", "a+") as f:
                f.writelines(todo.strip() + " -P\n")
            print("Task successfully created!")

# Complete a Task

def complete():
    todo = int(input("Which task has been completed? "))
    with open("todo.txt", "r") as f:
        all_todo = f.readlines()
        if " -P" in all_todo[todo - 1]:
            with open("todo.txt", "w") as f:
                comp_todo = all_todo[todo - 1].replace(" -P", " -C")
                all_todo[todo - 1] = comp_todo
                f.writelines(all_todo)
                print("Task successfully marked as completed!")
        else:
            print("Sorry. Task already completed or does'nt exist.")

# Modify a Task

def modify():
    todo = int(input("Which task has changed? "))
    with open("todo.txt", "r") as f:
        all_todo = f.readlines()
        if " -P" in all_todo[todo - 1]:
            with open("todo.txt", "w") as f:
                new_todo = input("Enter the updated task: ")
                all_todo[todo - 1] = new_todo + " -P\n"
                f.writelines(all_todo)
                print("Task successfully modified!")
        else:
            print("Sorry. Task already completed or doesn't exist.")

# Delete a Task

def delete():
    todo = int(input("Enter todo number to delete: "))
    with open("todo.txt", "r") as f:
        all_todo = f.readlines()
        if todo in range(1, len(all_todo)):
            with open("todo.txt", "w") as f:
                del all_todo[todo - 1]
                f.writelines(all_todo)
                print("Task succesfully removed!")
        else:
            print("Sorry. There's no such task in the list.")

# Show All Tasks

def showAll():
    with open("todo.txt", "r") as f:
        print("\n********** All Tasks **********\n")
        for i, line in enumerate(f.readlines(), start=1):
            print(f"[{i:>2}] - {line}", end="")

# Show Pending Tasks

def showPending():
    with open("todo.txt", "r") as f:
        print("\n********** Pending Tasks **********")
        for i, line in enumerate(f.readlines(), start=1):
            if " -P" in line:
                print(f"[{i}] - {line}", end="")

# Quit

def quit():
    q = input("Quit the app? (Y/N) ")
    if q in ["Y", "y"]:
        print("Hasta luego!")
        sys.exit()


""" Main Program """

print("\nWelcome to a modest cli TODO manager!")
MENU = """\n********** MENU **********\n
Select an option to perform an action:
1 - Create a New Task
2 - Complete a Task
3 - Modify a Task
4 - Delete a Task
5 - Show All Tasks
6 - Show Pending Tasks
7 - Quit
>>> """

while True:
    try:
        option = int(input(MENU))
    except ValueError:
        print("Error. Please choose a valid option.")
    else:
        match option:
            case 1:
                create()
            case 2:
                complete()
            case 3:
                modify()
            case 4:
                delete()
            case 5:
                showAll()
            case 6:
                showPending()
            case 7:
                quit()
