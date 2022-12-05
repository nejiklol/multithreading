import os
from os.path import isdir, join
from threading import Lock, Thread

locker = Lock()
finded = []


def FileFinder(root, filename):
    print("Finding in:", root)
    childs = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            locker.acquire()
            finded.append(full_path)
            locker.release()
        if isdir(full_path):
            t = Thread(target=FileFinder, args=([full_path, filename]))
            t.start()
            childs.append(t)
    for t in childs:
        t.join()


t = Thread(target=FileFinder, args=(["C:/SKLIT", "README.md"]))
t.start()
t.join()
for m in finded:
    print("Finded:", m)


