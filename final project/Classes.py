import csv
import os

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Name: {self.name}   description: {self.description}    priority: {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks=[]
        self.file_path=self.defult_file_path()


    def search_task(self,name):
        for task in self.tasks:
            if task.get_name()==name:
                return task
        return -1



    def add_task(self,task):
        if self.search_task(task.get_name()) == -1:
            self.tasks.append(task)
            return True
        return False



    def remove_task(self,name):
        task=self.search_task(name)
        if task != -1:
            self.tasks.remove(task)
            return True
        return False
  
    

    def __str__(self):
        result=":کل لیست کار ها \n"
        for task in self.tasks:
            result= result+str(task)
            result= result+"\n"
        return result
     

    def defult_file_path(self):
        script_dir=os.path.dirname(__file__)
        return os.path.join(script_dir,"todolist.csv")


    def load_taskS(self):
        with open(self.file_path,"r") as file:
            reader=csv.DictReader(file)
            self.tasks=list(reader)
            return True
        return False    


        

    


