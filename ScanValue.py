import threading 
import time

num = 0

def incSet(num1):
    global num
    while num<100:
        num+=1
        time.sleep(2)
def valueScan(num1):
    global num
    while True:
        print(num)
        time.sleep(1)




if __name__ == '__main__':
    sett = threading.Thread(target=incSet, args = (0, ))
    scan = threading.Thread(target=valueScan, args = (0, ))
    sett.start()
    scan.start()
    scan.join()
    sett.join()
