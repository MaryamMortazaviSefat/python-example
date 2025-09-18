import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"زمان اجرا: {execution_time:.6f} ثانیه")
        return result
    return wrapper


@timer_decorator
def create_list():
    return list(range(1, n + 1))
    
            
n=int(input())
create_list()