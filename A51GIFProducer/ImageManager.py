from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import os
from colors import bcolors

PALADINS_LOC = os.path.abspath(os.getcwd() + "\\resources\\PALADINS.TTF")
FONT_USER_INFO = ImageFont.truetype("arial.ttf", 90, encoding="utf-8")
TWEET_FONT_TEXT = ImageFont.truetype("arial.ttf", 110, encoding="utf-8")
TEAM_FONT_TEXT = ImageFont.truetype(PALADINS_LOC, 40, encoding="utf-8")
TWEET_IMAGE_OUTPUT_DIR = os.path.abspath(os.getcwd() + "\\TweetsOut")
TEAMTEXT_IMAGE_OUTPUT_DIR = os.path.abspath(os.getcwd() + "\\TeamTextOut")
GIF_RAW_DIR = os.path.abspath(os.getcwd() + "\\bin")
WIDTH = 2600
HEIGHT = 800
COLOR_BG = 'white'
COLOR_NAME = 'black'
COLOR_TAG = (64, 64, 64)
COLOR_TEXT = 'black'
COORD_PHOTO = (250, 190) #(250, 170)
COORD_NAME = (600, 185)
COORD_TAG = (600, 305)
COORD_TEXT = (250, 510)
LINE_MARGIN = 15


COLOR_TEXT_LIGHT = (220, 220, 220)  # 192
COLOR_TEXT_DARK = (192, 192, 192)

user_name = "Arena 51 Gaming"
user_tag = "@Arena_51_Gaming"


def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


def createTweetImage(tweetBody, imageName):
    # create output dir 
    try:
        if not os.path.exists(TWEET_IMAGE_OUTPUT_DIR):
            os.makedirs( TWEET_IMAGE_OUTPUT_DIR)
    except OSError as e:
        print(f"{bcolors.FAIL}Could not create output directory at: \n{TWEET_IMAGE_OUTPUT_DIR}{bcolors.ENDC}")
        print(e)
        exit()
    # Setup of variables and calculations
    # Break the text string into smaller strings, each having a maximum of 37\
    # characters (a.k.a. create the lines of text for the image)
    text_string_lines = wrap(tweetBody, 37)

    # Horizontal position at which to start drawing each line of the tweet body
    x = COORD_TEXT[0]

    # Current vertical position of drawing (starts as the first vertical drawing\
    # position of the tweet body)
    y = COORD_TEXT[1]

    # Create an Image object to be used as a means of extracting the height needed\
    # to draw each line of text
    temp_img = Image.new('RGB', (0, 0))
    temp_img_draw_interf = ImageDraw.Draw(temp_img)

    # List with the height (pixels) needed to draw each line of the tweet body
    # Loop through each line of text, and extract the height needed to draw it,\
    # using our font settings
    line_height = [
        temp_img_draw_interf.textsize(text_string_lines[i], font=TWEET_FONT_TEXT)[1]
        for i in range(len(text_string_lines))
    ]

    # Image creation
    # Create what will be the final image
    img = Image.new('RGB', (WIDTH, HEIGHT+line_height[0]*len(text_string_lines)), color='white')
    # Create the drawing interface
    draw_interf = ImageDraw.Draw(img)

    # Draw the user name
    draw_interf.text(COORD_NAME, user_name, font=FONT_USER_INFO, fill=COLOR_NAME)
    # Draw the user handle
    draw_interf.text(COORD_TAG, user_tag, font=FONT_USER_INFO, fill=COLOR_TAG)

    # Draw each line of the tweet body. To find the height at which the next\
    # line will be drawn, add the line height of the next line to the current\
    # y position, along with a small margin
    for index, line in enumerate(text_string_lines):
        # Draw a line of text
        draw_interf.text((x, y), line, font=TWEET_FONT_TEXT, fill=COLOR_TEXT)
        # Increment y to draw the next line at the adequate height
        y += line_height[index] + LINE_MARGIN

    # Load the user photo (read-mode). It should be a 250x250 circle 
    user_photo = Image.open('resources/A51-profile-pic.png', 'r')

    # Paste the user photo into the working image. We also use the photo for\
    # its own mask to keep the photo's transparencies
    img.paste(user_photo, COORD_PHOTO, mask=user_photo)

    # Finally, save the created image
    img.save(f'{ TWEET_IMAGE_OUTPUT_DIR}\\{imageName}.png')


def createTeamTextImage(teamTextList, imageName):
    try:
        if not os.path.exists(TEAMTEXT_IMAGE_OUTPUT_DIR):
            os.makedirs(TEAMTEXT_IMAGE_OUTPUT_DIR)
    except OSError as e:
        print(f"{bcolors.FAIL}Could not create output directory at: \n{TEAMTEXT_IMAGE_OUTPUT_DIR}{bcolors.ENDC}")
        print(e)
        exit()
    pass

    fullTextString = teamTextList[0][0] + " vs  " + teamTextList[1][0]
    padding = 3
    w, h = get_text_dimensions(fullTextString, TEAM_FONT_TEXT)
    team1w, _ = get_text_dimensions(teamTextList[0][0], TEAM_FONT_TEXT)
    vsw, _ = get_text_dimensions(" vs ", TEAM_FONT_TEXT)

    TeamTextImg = Image.new('RGB', (w+padding, h+padding), color='white')
    draw_interf = ImageDraw.Draw(TeamTextImg)
    draw_interf.text((0, 0), teamTextList[0][0], font=TEAM_FONT_TEXT, fill=teamTextList[0][1])
    draw_interf.text((team1w, 0), " vs", font=TEAM_FONT_TEXT, fill=(220,220,220))
    draw_interf.text((team1w + vsw, 0), " " + teamTextList[1][0], font=TEAM_FONT_TEXT, fill=teamTextList[1][1])

    TeamTextImg.save(f'{TEAMTEXT_IMAGE_OUTPUT_DIR}\\{imageName}.png')


def ExportGif(imgList,duration, name="OUT"):
    print(" Exporting GIF...", end='\r')
    if imgList == None:
        images = []
        for file in os.listdir(GIF_RAW_DIR):
            filename = os.fsdecode(file)
            if filename.endswith(".png"): 
                imagePath = os.path.join(GIF_RAW_DIR, filename)
                images.append(Image.open(imagePath, "r"))
    else:
        images = imgList
    images[0].save(f'{name}.gif',
               save_all=True, append_images=images[1:], optimize=True, loop=0, duration=duration)
    print(f"{bcolors.OKGREEN}GIF Exported as {name}.gif{bcolors.ENDC}")
    

def clearOutputDir():
    complete = True
    dir_name = os.path.abspath(os.getcwd() + "\\" +  TWEET_IMAGE_OUTPUT_DIR)
    if os.path.exists(dir_name) and os.path.isdir(dir_name):
        if not os.listdir(dir_name):
            # DIR is empty
            pass
        else:    
            # DIR not empty
            print(f"{bcolors.WARNING}{bcolors.UNDERLINE}Removing all previously generated tweets:{bcolors.ENDC}")
            for file in os.listdir(dir_name):
                if file.endswith(".png"):
                    try:
                        fileAbsPath = os.path.abspath(dir_name + "\\" + file)
                        print(f"\t{bcolors.WARNING}Deleting file: {file}{bcolors.ENDC}")
                        os.remove(os.path.abspath(fileAbsPath))
                    except OSError as e:
                        print(f"{bcolors.FAIL}Error: {fileAbsPath} : {e.strerror}{bcolors.ENDC}")  
                        complete = False       
    else:
        # DIR does not exist
        pass
    if complete:
        print(f"{bcolors.OKGREEN}Output Dir { TWEET_IMAGE_OUTPUT_DIR} ready.{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}This python script could not delete the pre-existing files in the directory: \n\t{dir_name}\nPlease navigate to that directory, delete all .png files, and re-run this script.{bcolors.ENDC}")
        exit()


if __name__ == "__main__":
    print(f"{bcolors.FAIL}Please run main.py for full functionality.{bcolors.ENDC}{bcolors.WARNING} This script alone will: \n\tDelete all files in the TweetsOut dir (if any exist)\n\tConvert a line of text to an @Arena_51_Gaming tweet image, and save it in ./TweetsOut/{bcolors.ENDC}")

    #createTweetImage("Sample Tweet.", "sample-tweet")
    clearOutputDir()
    exit()