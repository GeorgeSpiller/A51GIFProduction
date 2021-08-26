from ImageManager import  createTeamTextImage, ExportGif
from PIL import Image, ImageDraw, ImageFont
import os
from colors import bcolors
from math import sqrt

CANVAS_SIZE = (1920, 1080)
RESOURCE_DIR = os.path.abspath(os.getcwd() + "\\resources")
TEAMTEXT_DIR = os.path.abspath(os.getcwd() + "\\TeamTextOut")


def util_reletiveToAbsCords(cords, teamTextImage):
    return (cords[0], cords[1] - teamTextImage.size[1])


def util_drawLine(startCoords, main, teamTextImage):
    teamText_start = startCoords
    teamText_end = [teamText_start[0] + teamTextImage.size[0], teamText_start[1] - teamTextImage.size[1]]

    while teamText_start[0] < CANVAS_SIZE[0]:

        if teamText_end[0] < 0 and teamText_end[1] < 0:
            print(f"Cord caught off screen: {teamText_end}")
            while teamText_end[0] < 0 and teamText_end[1] < 0:
                teamText_start = teamText_end
                teamText_end = [teamText_start[0] + teamTextImage.size[0], teamText_start[1] - teamTextImage.size[1]]
                print(f"end cord off canvas; updated to: s: {teamText_start} e: {teamText_end}")
        print(f"Drawing cord {teamText_start} to {teamText_end}")

        pasteCords = util_reletiveToAbsCords(teamText_start, teamTextImage)
        main.paste(teamTextImage, pasteCords, mask=teamTextImage)
        # move the start to the next location
        teamText_start = teamText_end
        teamText_end = [teamText_start[0] + teamTextImage.size[0], teamText_start[1] - teamTextImage.size[1]]
    return main, teamTextImage


def RotatedSliderAnimation(speed, teamList, saveImages=False):

    ROTATION = 45
    SPACING_VERTICAL = 80
    ALPHA = 150

    main = Image.new('RGB', (1920,1080), color='white')
    rawRGB = Image.open(f"{TEAMTEXT_DIR}\\temp.png", "r")
    teamTextImage = rawRGB.convert("RGBA")
    # rotate teamTextImage
    teamTextImage = teamTextImage.rotate(ROTATION, expand=1)
    # Make any black pixels transparent
    newImage = []
    for item in teamTextImage.getdata():
        if item[:3] == (0, 0, 0):
            newImage.append((0, 0, 0, 0))
        else:
            newImage.append((item[0], item[1], item[2], ALPHA))
    teamTextImage.putdata(newImage)

    currPos = [0, 0] 
    xFlip = True

    while currPos[1] <= CANVAS_SIZE[1]*3:
        if xFlip:
            hypot = int((sqrt(teamTextImage.size[0]**2 + teamTextImage.size[1]**2))/2)
            print(hypot)
            currPos[0] = hypot
            xFlip = not xFlip
        else:
            currPos[0] = 0
        main, teamTextImage = util_drawLine(currPos, main, teamTextImage)
        currPos[1] += SPACING_VERTICAL
        print(currPos)

    print(f"Saved as {os.getcwd()}\\TeamTextOut.png")
    main.save(os.getcwd() + "\\TeamTextOut2.png")
    

if __name__ == "__main__":
    print(f"{bcolors.FAIL}Please run main.py for full functionality.{bcolors.ENDC}{bcolors.WARNING}{bcolors.ENDC}")
    exit()


