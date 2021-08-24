from ImageManager import  ExportGif
from PIL import Image, ImageDraw, ImageFont
import os
from colors import bcolors

CANVAS_SIZE = (1920, 1080)
RESOURCE_DIR = os.path.abspath(os.getcwd() + "\\resources")

def RotatedSliderAnimation(speed, teamList, saveImages=False):
    # create the font for each team
    # FONT_TEXT =  ImageFont.truetype(RESOURCE_DIR + "\\PALADINS.TTF", 40, encoding="utf-8") 

    # starting from 0,0:
    # draw text image on canvas, rotated starting at 0,0
    # if the image furthest end pos not on canvas skip to next line until start pos not on canvas
    pass

if __name__ == "__main__":
    print(f"{bcolors.FAIL}Please run main.py for full functionality.{bcolors.ENDC}{bcolors.WARNING}{bcolors.ENDC}")

    exit()


