import time
import os

import win32clipboard as clp
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# # This works for Paint.NET, but not for Discord:
# file = open(file_path, 'rb')
# clp.SetClipboardData(clp.RegisterClipboardFormat('image/png'), file.read())

class MyEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.my_integer = 0

    def on_created(self, event):
        self.my_integer += 1
        print(event.src_path)
        os.system(f"python shadowit.py \"{event.src_path}\" -o output.png --exe \"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe\"")
        file_path = f'output.png'
        clp.OpenClipboard()
        clp.EmptyClipboard()
        # This works for Discord, but not for Paint.NET:
        wide_path = os.path.abspath(file_path).encode('utf-16-le') + b'\0'
        clp.SetClipboardData(clp.RegisterClipboardFormat('FileNameW'), wide_path)
        clp.CloseClipboard()    
        
if __name__ == '__main__':
    observer = Observer()
    file_handler = MyEventHandler()
    observer.schedule(file_handler, r"C:\users\hiror\OneDrive\文件\ShareX\Screenshots\2024-04", False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()