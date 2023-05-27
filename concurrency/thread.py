import threading

def myTask():
    t=threading.current_thread()
    print("Hello World" + str(t))
    
myThread=threading.Thread(target=myTask())
myThread.start()