import tkinter as tk
from tkinter import ttk

listFile = "toDoList.txt"


class TaskList:
    def __init__(self, initialTasks = []):
        self.toDoList = []
        self.changed = False
        self.master = tk.Tk()
        self.master.title("To Do")
        s = ttk.Style()

        self.tree = ttk.Treeview(self.master, show="tree")
        self.tree.column("#0", width=300)
        s.configure('Treeview', rowheight=25)
        self.tree.pack()

        deleteB = tk.Button(self.master, text="Check Off", command=self.deleteTask)
        deleteB.pack()
        
        addB = tk.Button(self.master, text="Add", command=self.displayAddBox)
        addB.pack()

        for task in initialTasks:
            self.addTask(task)

    def displayAddBox(self):
        enter = tk.Tk()
        preFrame = tk.Frame(enter, width=300, height=25)
        label = tk.Label(enter, text="Enter a task")
        self.entryBox = tk.Entry(enter, width=50)
        addButton = tk.Button(enter, text="Add", command=self.__addTaskFromGui)
        postFrame = tk.Frame(enter, width=300, height=25)

        preFrame.pack()
        label.pack()
        self.entryBox.pack()
        addButton.pack()
        postFrame.pack()

        enter.mainloop()

    def __addTaskFromGui(self):
        self.addTask(self.entryBox.get())
        self.entryBox.delete(0, "end")

    def addTask(self, newTask = None):
        if newTask != "":
            i = 0
            if len(self.toDoList) > 0:
                while self.toDoList[i].lower() < newTask.lower():
                    i += 1
                    if i >= len(self.toDoList):
                        break

            self.toDoList.insert(i, newTask + "\n")
            self.tree.insert('', i, text=newTask)
            self.changed = True

    def deleteTask(self):
        highlighted = self.tree.focus()
        if highlighted != '':
            del self.toDoList[self.tree.index(highlighted)]
            self.tree.delete(highlighted)
            self.changed = True


tasks = TaskList()

with open(listFile, 'r') as file:
    for line in file.readlines():
        tasks.addTask(line.strip())

tasks.master.mainloop()

if tasks.changed:
    with open(listFile, 'w') as file:
        for task in tasks.toDoList:
            file.write(task)
