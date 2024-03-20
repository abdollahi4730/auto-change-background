from os import system
from time import sleep
class Congig:
    def __init__(self, time : int ,*args):
        timeSec = time * 60
        while(True):
            for arg in args:

                system(f'gsettings set org.gnome.desktop.background picture-uri {arg}')
                sleep(timeSec)

x = Congig(
    # this is timer of random background (Minute)
    0.5 ,

    # these are all adress your Picture that you want join to random background (number of pictures is not important)
    "file:///home/mohammad/Desktop/1.jpg",
    "file:///home/mohammad/Desktop/2.jpg",
    # for add new address picture you can add it here ...
    )
