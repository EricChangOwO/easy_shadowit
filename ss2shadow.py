import pyautogui
import os 
import keyboard

count = 1 

for i in range(5):
    while True:
        if keyboard.is_pressed("q"):
            print("You pressed q")
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f'images\{count}.png')
            os.system(f"python shadowit.py images\{count}.png -o images\output\sha_{count}.png --exe \"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe\"")
            count += 1
            break


# for i in range(5):
#     myScreenshot.save(f'images\{count}.png')
#     os.system(f"python shadowit.py images\{count}.png -o images\output\sha_{count}.png --exe \"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe\"")
#     count += 1
