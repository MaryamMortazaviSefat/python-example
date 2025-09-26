import csv
import os
import json

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def get_name(self):
        return self.name
    
    def get_priority(self):
        return self.priority
    
    def set_priority(self,new_priority):
        self.priority=new_priority

    def __str__(self):
        return f"Name: {self.name}   description: {self.description}    priority: {self.priority}"
    
    def __iter__(self):
        yield self.name 
        yield self.description
        yield self.priority


class ToDoList:
    def __init__(self):
        self.tasks=[]
        self.file_path=self.defult_file_path()


    def get_path_file(self):
        return self.file_path

    
    def defult_file_path(self):
        script_dir=os.path.dirname(__file__)
        return os.path.join(script_dir,"todolist")


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


    def load_tasks_scv(self):
        with open(self.file_path+".csv","r",newline='',encoding='utf-8') as file:
            reader=csv.reader(file)
            next(reader)
            self.tasks=list(Task(row[0],row[1],row[2]) for row in reader)
            return True
        return False    


    def save_tasks_csv(self):
        with open(self.file_path+".csv","w",newline='',encoding='utf-8') as file:
            writer=csv.writer(file)
            writer.writerow(['name','description','priority'])
            writer.writerows(list(task) for task in self.tasks)
            return True
        return False 
    

    def load_tasks_json(self):
        with open(self.file_path+".json","r",encoding='utf-8') as file:
            data=json.load(file)
            self.tasks=[Task(**item) for item in data]
            return True
        return False    


    def save_tasks_json(self):
        with open(self.file_path+".json","w",encoding='utf-8') as file:
            json.dump([task.__dict__ for task in self.tasks],file,ensure_ascii=False,indent=2)
            return True
        return False


    def change_priority(self,name,new_priority):
        task=self.search_task(name)
        if task != -1:
            self.tasks.remove(task)
            task.set_priority(new_priority)
            self.add_task(task)
            return True
        return False
    

    def __str__(self):
        result=":کل لیست کار ها \n"
        for task in self.tasks:
            result= result+str(task)
            result= result+"\n"
        return result
     

    


   



        

    


