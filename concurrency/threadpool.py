import threading
from concurrent.futures import ThreadPoolExecutor

def task():
    #print(r)
    #task_number=task_number+1
    #print("Executing task  "+ task_number)
    result=0
    i=0
    for i in range(10):
        result=result+i
    print("task number  "+str(i+1))
    print("I :{}".format(result))
    print("Tasks executed by {}".format(threading.current_thread()))
    #r=r+1

def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        task1=executor.submit(task)
        task2=executor.submit(task)
        task3=executor.submit(task)
        task4=executor.submit(task)



main()


