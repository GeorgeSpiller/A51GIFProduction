from ImageManager import  ExportGif
from PIL import Image, ImageDraw, ImageFont
import os
from colors import bcolors

CANVAS_SIZE = (1920, 1080)
RESOURCE_DIR = os.path.abspath(os.getcwd() + "\\resources")


def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def RotatedSliderAnimation(speed, teamList, saveImages=False):
    # create the font for each team
    # FONT_TEXT =  ImageFont.truetype(RESOURCE_DIR + "\\PALADINS.TTF", 40, encoding="utf-8") 

    # starting from 0,0:
    # draw text (alternating team) until off canvas
    # new line, offset by len(team/2)
    # do until start pos y 

    pass

if __name__ == "__main__":
    print(f"{bcolors.FAIL}Please run main.py for full functionality.{bcolors.ENDC}{bcolors.WARNING}{bcolors.ENDC}")

    exit()


