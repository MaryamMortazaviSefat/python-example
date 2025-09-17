def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"the error is :{e}\n please enter the correct numbers again:") 
        result=None
    else:
        pass
    finally:
        print("برنامه با موفقیت اجرا شد!")
        return result


def do():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result=divide(num1,num2)
    except ValueError as e:
        print(f"the error is {e}\n please enter the int numbers again:")
        result=None
        print("برنامه با موفقیت اجرا شد!")
    finally:
        if result is None:
            do()
        else:
            print(f"Result: {result}")


do()