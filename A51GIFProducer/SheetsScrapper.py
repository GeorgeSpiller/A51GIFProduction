from colors import bcolors

COLOR_DICT = {
    "RED":(255, 153, 153),
    "ORANGE":(255, 204, 153),
    "YELLOW":(255, 255, 153),
    "GREEN":(153, 255, 153),
    "BLUE":(153, 204, 255),
    "PURPLE":(204, 153, 255),
    "PINK":(255, 153, 204),
}


def manualTeamSetup():
    # tmp line for dev
    return [("Mighty Blues", (153, 204, 255)), ("Pink Panthers", (255, 153, 204))]

    team1_name = input("Team1 name: ")
    team1_color = input("Team1 color: ").upper().strip()

    team2_name = input("Team2 name: ")    
    team2_color = input("Team2 color: ").upper().strip()

    try:
        team1_color = COLOR_DICT[team1_color]
        team2_color = COLOR_DICT[team2_color]
    except KeyError:
        print(f"{bcolors.WARNING}One of the colors entered did not match an available color.{bcolors.ENDC}")
        print(f"Please choose a color from: {COLOR_DICT.keys()}")
        manualTeamSetup()

    warn = ""
    if team1_name == team2_name:
        warn += f"{bcolors.WARNING}Teams have the same names.{bcolors.ENDC}\n"
    if team1_color == team2_color:
        warn += f"{bcolors.WARNING}Teams have the same colors.{bcolors.ENDC}\n"

    if warn:

        restart = False
        userImp = input(f"\n{warn}Do you wish to continue? (y/n): ")
        restart = True if "n" in userImp.lower() else False
        if restart:
            manualTeamSetup()
        else:
            return [(team1_name, team1_color), (team2_name, team2_color)]
    else:
        return [(team1_name, team1_color), (team2_name, team2_color)]