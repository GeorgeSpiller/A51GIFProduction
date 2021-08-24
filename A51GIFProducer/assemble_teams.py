from ImageManager import  createTeamTextImage, ExportGif
from PIL import Image, ImageDraw, ImageFont
import os
from colors import bcolors

CANVAS_SIZE = (1920, 1080)
RESOURCE_DIR = os.path.abspath(os.getcwd() + "\\resources")
TEAMTEXT_DIR = os.path.abspath(os.getcwd() + "\\TeamTextOut")


def RotatedSliderAnimation(speed, teamList, saveImages=False):
    # starting from 0,0:
    # draw text image on canvas, rotated starting at 0,0
    # if the image furthest end pos not on canvas skip to next line until start pos not on canvas
    main = Image.new('RGB', (1920,1080), color='white')
    tmp = Image.open(f"{TEAMTEXT_DIR}\\temp.png", "r")

    # refactor so they image does not need to be saved (image obj as param)
    # https://stackoverflow.com/questions/5252170/specify-image-filling-color-when-rotating-in-python-with-pil-and-setting-expand


    teamTextImage = tmp.rotate(45)

    currPosRow = [500, 500]
    currPosLine = currPosRow
    print(f"row:{currPosRow}, line: {currPosLine}")
    for i in range(10):
        currPosLine = currPosRow
        # draw a line
        while currPosLine[0] < CANVAS_SIZE[0] and currPosLine[1] < CANVAS_SIZE[1]:
            main.paste(teamTextImage, (currPosLine[0], currPosLine[1]))
            print(f"row:{currPosRow}, line: {currPosLine}")
            currPosLine[0] += teamTextImage.size[0]
        currPosRow[1] += teamTextImage.size[1]
    print(f"Saved as {os.getcwd()}\\TeamTextOut.png")
    main.save(os.getcwd() + "\\TeamTextOut.png")
    

if __name__ == "__main__":
    print(f"{bcolors.FAIL}Please run main.py for full functionality.{bcolors.ENDC}{bcolors.WARNING}{bcolors.ENDC}")

    exit()


