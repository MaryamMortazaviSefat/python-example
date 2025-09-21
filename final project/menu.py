import Classes


def continue_menu():
        print("آیا می خواهید دوباره به منو برگردید؟\n")
        print("لطفا عدد گزینه مورد نظر را انتخاب کنید:\n1.یله\n2.خیر\n")
        option=int(input())
        if option==1:
            return True
        elif option==2:
            return False
        else:
            print("لطفا تنها عدد وارد کنید")
            continue_menu()




print("سلام خوش آمدید\n")
Is_run=True

while(Is_run):
    
    print("منوی پروژه لیست کارهای انجامی: \n"
          "لطفا یک گزینه را انتخاب کنید\n"
          "1.اضافه کردن کار جدید\n"
          "2.حذف کار\n"
          "3.مشاهده لیست کار ها\n"
          "4.ذخیره ی لیست کار ها در فایل csv\n"
          "5.بارگزاری از فایل  csv\n"
          "6.انتخاب اوبویت کارها\n"    
    )

    option=int(input())

    if option==1:
         pass
    elif option==2:
         pass
    elif option==3:
         print("str todolist")
    elif option==3:
         pass
    elif option==4:
         pass
    elif option==5:
         pass
    elif option==6:
         pass
    else:
         print(" لطفا تنها عدد یکی از گزینه ها را وارد کنید\n")



    Is_run= continue_menu()

    











