import tkinter as tk

listFile = "toDoList.txt"


class TaskList:
    def __init__(self, initialTasks = []):
        self.toDoList = []
        self.changed = False
        self.master = tk.Tk()
        self.listbox = tk.Listbox(self.master, width=40, height=20)
        self.listbox.pack()
        deleteB = tk.Button(self.master, text="Check Off", command=self.deleteTask)
        deleteB.pack()
        addB = tk.Button(self.master, text="Add", command=self.addBox)
        addB.pack()

        for task in initialTasks:
            self.addTask(task)

    def addBox(self):
        enter = tk.Tk()
        frame1 = tk.Frame(enter, width=300, height=25)
        label = tk.Label(enter, text="Enter a task")
        self.eBox = tk.Entry(enter, width=50)
        en = tk.Button(enter, text="Add", command=self.addTask)
        frame2 = tk.Frame(enter, width=300, height=25)
        frame1.pack()
        label.pack()
        self.eBox.pack()
        en.pack()
        frame2.pack()
        enter.mainloop()

    def addTask(self, newTask = None):
        fromEBox = False

        if newTask is None:
            newTask = self.eBox.get()
            fromEBox = True

        if newTask != "":
            if len(self.toDoList) > 0:
                i = 0
                while self.toDoList[i].lower() < newTask.lower():
                    i += 1
                    if i >= len(self.toDoList):
                        break

                self.toDoList.insert(i, newTask + "\n")
                self.listbox.insert(i, newTask)
                if fromEBox:
                    self.eBox.delete(0, "end")
                self.changed = True
            else:
                self.toDoList.insert(0, newTask + "\n")
                self.listbox.insert(0, newTask)
                if fromEBox:
                    self.eBox.delete(0, "end")
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
