import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.my_integer = 0

    def on_created(self, event):
        self.my_integer += 1
        print(event.src_path)
        os.system(f"python shadowit.py \"{event.src_path}\" -o images\output\sha_{self.my_integer}.png --exe \"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe\"")
        
if __name__ == '__main__':
    observer = Observer()
    file_handler = MyEventHandler()
    observer.schedule(file_handler, "./event", False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()