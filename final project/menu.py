import Classes

print("سلام خوش آمدید\n")
todolist=Classes.ToDoList()

while(True):
    
    print("منوی پروژه لیست کارهای انجامی: \n"
          "لطفا یک گزینه را انتخاب کنید\n"
          "1.اضافه کردن کار جدید\n"
          "2.حذف کار\n"
          "3.مشاهده لیست کار ها\n"
          "4.ذخیره ی لیست کار ها در فایل csv\n"
          "5.بارگزاری از فایل  csv\n"
          "6.انتخاب اوبویت کارها\n" 
          "7.ذخیره لیست کار ها در فایل json\n"
          "8.بارگزاری کار ها از فایل json\n"  
          "9.خروج" 
    )

    option=int(input())

    if option==1:
         name=input("لطفا نام کار را وارد کنید:")
         description=input("لطفا توضیحات کار را وارد کنید:")
         priority=int(input("لطفا اولویت کار خود را وارد کنید:"))
         new_task=Classes.Task(name,description,priority)
         if todolist.add_task(new_task):
              print(f"کار{name} با موفقیت به لیست اضافه شد")
         else:
              print("عملیات ناموفق")
              
 
    elif option==2:
          name=input("لطفا نام کار را وارد کنید:")
          if todolist.remove_task(name):
               print(f"کار{name} با موفقیت حذف شد")
          else:
               print("عملیات نا موفق")

         
    elif option==3:
         try:
             print(str(todolist))
         except "error":
              print("لیست قابل مشاهده نیست!")


    elif option==4:
         try: 
              if todolist.save_tasks_csv():
                  print(f"لیست در فایل {todolist.get_path_file()} ذخیره شد ")
         except "error":
              print("مشکلی در ذخیره سازی رخ داده است!")
              
              
    elif option==5:
         try:
              if todolist.load_tasks_scv():
                  print(f"لیست از فایل {todolist.get_path_file()} خوانده شد ")
         except "error":
              print("مشکلی در بارگزاری رخ داده است!")
         

    elif option==6:
         print(str(todolist))
         name=input("لطفا نام کاری که قصد تفییر اولویت آن را دارید وارد کنید:")
         new_priority=int(input("میخواهید کار را در اولویت چندم قرار دهید"))
         if todolist.change_priority(name,new_priority):
              print("اولویت کار را شما با موفیقت رخ داد")


    elif option==7:
         try: 
              if todolist.save_tasks_json():
                  print(f"لیست در فایل {todolist.get_path_file()} ذخیره شد ")
         except "error":
              print("مشکلی در ذخیره سازی رخ داده است!")

     
    elif option==8:
         try:
              if todolist.load_tasks_json():
                  print(f"لیست از فایل {todolist.get_path_file()} خوانده شد ")
         except "error":
              print("مشکلی در بارگزاری رخ داده است!")


    elif option==9:
         exit()
         
         
    else:
         print(" لطفا تنها عدد یکی از گزینه ها را وارد کنید")



     
    











