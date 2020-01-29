import tkinter as tk

listFile = "toDoList.txt"


class TaskList:
    def __init__(self, initialTasks = []):
        self.toDoList = []
        self.changed = False
        self.master = tk.Tk()
        self.listbox = tk.Listbox(self.master, width=40, height=20)
        deleteB = tk.Button(self.master, text="Check Off", command=self.deleteTask)
        addB = tk.Button(self.master, text="Add", command=self.displayAddBox)

        self.listbox.pack()
        deleteB.pack()
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
            self.listbox.insert(i, newTask)
            self.changed = True

    def deleteTask(self):
        highlighted = self.listbox.curselection()
        if highlighted != ():
            del self.toDoList[highlighted[0]]
            self.listbox.delete(highlighted[0])
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
