##>Hyper-Hole.py
##>
##>Developed by "HyperWoo" at - github.com/hyperwoo


from watchdog import observers
from watchdog.events import FileSystemEventHandler
import os
import json
import time
import shutil

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(path):

            file_folder = os.path.join(path,file)
            shutil.move(file_folder, move_folder)

path = "C://Users//harsh//Desktop//Hyper-Hole"
move_folder = "D://HARSH (FOLDER)//Projects//HYPER-HOLE//Drop"

event_handler = FileHandler()
observer = observers.Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()

observer.join()
