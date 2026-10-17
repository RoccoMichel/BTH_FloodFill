import graphics
import random
import time
import math

# Game Settings:
MINSIZE = 2
MAXSIZE = 26
MINCOLORS = 3
MAXCOLORS = 8 
MAXTURNMODIFIER = 100
STARTPOINT = [0, 0]
STARTPOINTBYPLAYER = False

# Visual Settings:
DYNAMICSCALING = True # affects: BOXSIZE
WIDTH = 700
HEIGHT = 780
BOXSIZE = 30
BOXMARGIN = 2
BOXOUTLINE = 2
BACKGROUNDOUTLINE = 10
BACKGROUNDCOLOR = "DarkOrchid3"
TEXTCOLOR = "white"


def get_status():
    return f"{turns}/{max_turns}  |  {size}x{size}  |  Colors: {colors}"


def generateGrid(size, variantion):
    grid = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.randint(0, variantion - 1))
        grid.append(row)

    return grid


def clamp(value, min, max):
    if value < min:
        value = min
    elif value > max:
        value = max    
    return value


def saveHighscore(turns, time, size):
    time = round(time, 2)
    score = int(turns + time) # Mät tiden för en spelomgång och låt den påverka poängen. Färre drag ska dock alltid ge bättre resultat än fler drag.
    file = open("highscores.txt", 'a')
    file.write(f"{score}:\t\t{turns} \t| {size}X{size}\t| {time} seconds\n")
    file.close()


def getValuesLeft(grid):
    left = []
    for row in grid:
        for value in row:
            if value not in left:
                left.append(value)

    return len(left)


def setTextStyle(texts, size, face, style, color, ):
    for text in texts:
        text.setSize(size)
        text.setFace(face)
        text.setStyle(style)
        text.setTextColor(color)


def getBoxLocation(location, boxes):
    grid_size = len(boxes)
    x = -1
    y = -1
    for i in range(grid_size):
        if location.y >= boxes[i][0].p1.y and location.y <= boxes[i][0].p2.y:
            x = i
    for j in range(grid_size):
        if location.x >= boxes[0][j].p1.x and location.x <= boxes[0][j].p2.x:
            y = j

    if x == -1 or y == -1:
        return None
    else:
        return [x, y]    


def getBoxValue(location, grid, boxes): # linear not exponential 
    location = getBoxLocation(location, boxes)

    if location == None:
        return None
    else:
        return grid[location[0]][location[1]]


def color_fill(grid, boxes, startpoint, new_value):
    compare_value = grid[startpoint[0]][startpoint[1]]
    grid[startpoint[0]][startpoint[1]] = new_value
    boxes[startpoint[0]][startpoint[1]].setFill(getColor(new_value))

    # Check North
    if startpoint[0]-1 >= 0:
        if grid[startpoint[0]-1][startpoint[1]] == compare_value:
            color_fill(grid, boxes, [startpoint[0]-1, startpoint[1]], new_value)

    # Check South
    if startpoint[0]+1 < len(grid):
        if grid[startpoint[0]+1][startpoint[1]] == compare_value:
            color_fill(grid, boxes, [startpoint[0]+1, startpoint[1]], new_value)     

    # Check West
    if startpoint[1]-1 >= 0:
        if grid[startpoint[0]][startpoint[1]-1] == compare_value:
            color_fill(grid, boxes, [startpoint[0], startpoint[1]-1], new_value)

    # Check East
    if startpoint[1]+1 < len(grid):
        if grid[startpoint[0]][startpoint[1]+1] == compare_value:
            color_fill(grid, boxes, [startpoint[0], startpoint[1]+1], new_value)  


def getMaxTurns(size, colors):
    return math.floor(25*((size+size)*colors)/((14+14)*6))

    
def getColor(index): # index is int
    match index:
        case 0:
            return "blue"
        case 1:
            return "red"
        case 2:
            return "pink"
        case 3:
            return "purple"
        case 4:
            return "green"
        case 5:
            return "gold"
        case 6:
            return "aquamarine"
        case 7:
            return "sandy brown"
        case _:
            return "light grey"


def draw_grid(size):
    box_size = BOXSIZE
    if DYNAMICSCALING:
        padding = 0.1
        shortest_side = min(WIDTH, HEIGHT * 0.875)
        box_size = (shortest_side - shortest_side * padding)/size

    grid_length = box_size * size + BOXMARGIN * (size-1)
    grid_start = graphics.Point(WIDTH/2 - grid_length/2, HEIGHT * 0.125)

    background = graphics.Rectangle(grid_start, graphics.Point(grid_start.x + grid_length, grid_start.y + grid_length))
    background.setFill(BACKGROUNDCOLOR)
    background.setWidth(BACKGROUNDOUTLINE)
    background.draw(window)
    
    for i in range(size):
        squres_row = []
        for j in range(size):            
            p1 = graphics.Point(grid_start.x + (box_size * j) + (BOXMARGIN * j), grid_start.y + (box_size * i) + ((BOXMARGIN) * i))
            p2 = graphics.Point(p1.x + box_size, p1.y + box_size)
            square = graphics.Rectangle(p1, p2)
            square.setFill(getColor(grid[i][j])) 
            square.setWidth(BOXOUTLINE)
            square.draw(window)

            squres_row.append(square)
        boxes.append(squres_row)

    return background


def main_menu(placeholder_size, placeholder_colors):
    # Valriabels
    height = 8
    title_string = "New Game?"
    title_text_size = 28
    standard_text_size = 18
    description_text_size = 12
    title_text_size = clamp(title_text_size, 5, 36)
    standard_text_size = clamp(standard_text_size, 5, 36)
    description_text_size = clamp(description_text_size, 5, 36)
    graphic_collection = []

    background = graphics.Rectangle(graphics.Point(0, int(HEIGHT/7)), graphics.Point(WIDTH, int(HEIGHT/7 + BOXSIZE * height + BOXMARGIN * (height-1))))
    background.setWidth(0)
    background.setFill("grey")
    background.draw(window)
    graphic_collection.append(background)

    title = graphics.Text(graphics.Point(WIDTH/2, background.p1.y + standard_text_size/2 + 10), title_string)
    title.draw(window)
    graphic_collection.append(title)


    # inputs
    input_text_size = clamp(int(standard_text_size * 0.7), 5, 36)
    input_y = int(background.p1.y + ((background.p2.y - background.p1.y) / 2))
    input_size = graphics.Entry(graphics.Point(int(WIDTH * 0.3), input_y), 10)
    input_size.setTextColor(TEXTCOLOR)
    input_size.setSize(input_text_size)
    input_size.setText(f"{placeholder_size}")
    input_size.setFill(BACKGROUNDCOLOR)
    input_size.draw(window)
    graphic_collection.append(input_size)


    input_size_text = graphics.Text(graphics.Point(input_size.anchor.x, (input_size.anchor.y - input_text_size - standard_text_size)), "Grid Size:")
    graphic_collection.append(input_size_text)
    input_size_text.draw(window)
    input_size_description = graphics.Text(graphics.Point(input_size.anchor.x, (input_size.anchor.y + input_text_size + description_text_size)), f"({MINSIZE} - {MAXSIZE})")
    input_size_description.draw(window)
    graphic_collection.append(input_size_description)

    input_color = graphics.Entry(graphics.Point(int(WIDTH * 0.7), input_y), 10)
    input_color.setTextColor(TEXTCOLOR)
    input_color.setSize(input_text_size)
    input_color.setText(f"{placeholder_colors}")
    input_color.setFill(BACKGROUNDCOLOR)
    input_color.draw(window)
    graphic_collection.append(input_color)

    input_color_text = graphics.Text(graphics.Point(input_color.anchor.x, input_color.anchor.y - input_text_size - standard_text_size), "Colors:")
    input_color_text.draw(window)
    graphic_collection.append(input_color_text)
    input_color_description = graphics.Text(graphics.Point(input_color.anchor.x, (input_color.anchor.y + input_text_size + description_text_size)), f"({MINCOLORS} - {MAXCOLORS})")
    input_color_description.draw(window)
    graphic_collection.append(input_color_description)

    # buttons
    quit_p1 = graphics.Point(int(WIDTH * 0.2), int(input_y + (background.p2.y - input_y)/2))
    quit_p2 = graphics.Point(int(WIDTH * 0.4), background.p2.y - 5) # 5 pixel padding at buttom
    quit_button = graphics.Rectangle(quit_p1, quit_p2)
    quit_button.setFill("red")
    quit_button.setWidth(2)    
    quit_button.draw(window)
    graphic_collection.append(quit_button)

    quit_button_text = graphics.Text(graphics.Point(int(WIDTH * 0.3), int(quit_p1.y + (quit_p2.y - quit_p1.y)/2)), "quit".upper())
    quit_button_text.draw(window)
    graphic_collection.append(quit_button_text)

    start_p1 = graphics.Point(int(WIDTH * 0.6), quit_p1.y)
    start_p2 = graphics.Point(int(WIDTH * 0.8), quit_p2.y)
    start_button = graphics.Rectangle(start_p1, start_p2)
    start_button.setFill("red")
    start_button.setWidth(2)
    start_button.draw(window)
    graphic_collection.append(start_button)

    start_button_text = graphics.Text(graphics.Point(int(WIDTH * 0.7), int(start_p1.y + (start_p2.y - start_p1.y)/2)), "start".upper())
    start_button_text.draw(window)
    graphic_collection.append(start_button_text)

    # styling
    setTextStyle([title], title_text_size, "times roman", "bold", TEXTCOLOR)
    setTextStyle([input_size_text, input_color_text, quit_button_text, start_button_text], standard_text_size, "times roman", "normal", TEXTCOLOR)
    setTextStyle([input_size_description, input_color_description], description_text_size, "times roman", "italic", TEXTCOLOR)

    # mouse input    
    user_input = None
    empty = graphics.Rectangle(graphics.Point(-1, -1), graphics.Point(-1, -1))
    while user_input == None:
        try:
            mouse_input = window.getMouse()
            user_input = getBoxValue(mouse_input, [["quit", "start"]], [[quit_button, start_button], [empty, empty]])
        except:
            print("Player closed window")
            user_input = "quit"

        # validate game settings
        title.setText(title_string)
        valid_inputs = True
        try:
            input_size_input = int(input_size.getText())
            input_color_input = int(input_color.getText())
            if input_size_input < MINSIZE or input_size_input > MAXSIZE:
                valid_inputs = False
            if input_color_input < MINCOLORS or input_color_input > MAXCOLORS:
                valid_inputs = False 
        except:
            valid_inputs = False

        if valid_inputs and user_input == "start":
            user_input += f",{int(input_size.getText())}"
            user_input += f",{int(input_color.getText())}"
        elif user_input == "quit":
            user_input += f",{MINSIZE}"
            user_input += f",{MINCOLORS}"
        elif not valid_inputs:
            title.setText("Invalid Input(s)!")
            user_input = None

    # Undraw all elements
    for element in graphic_collection:
        element.undraw()

    return user_input


if __name__ == "__main__":
    # Variables:
    size = 8
    colors = 8
    turns = 0
    max_turns = 0
    boxes = []
    playing = True
    background = None
    location = STARTPOINT
    start_time = time.time()

    # Create window
    window = graphics.GraphWin(f"Flood Fill Game\t(Rocco Michel)", WIDTH, HEIGHT)
    window.setBackground(BACKGROUNDCOLOR)

    # Main Menu
    title = graphics.Text(graphics.Point(WIDTH/2, 20), "Flood fill")   
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor(TEXTCOLOR)
    title.setFace("times roman")

    status = graphics.Text(graphics.Point(WIDTH/2, 40), "")
    status.setFace("times roman")    
    status.setTextColor(TEXTCOLOR)

    title.draw(window)
    status.draw(window)

    gameover = True

    while playing:  
        if gameover:
            # Try clear old grid
            for row in boxes:
                for box in row:
                    box.undraw()
            boxes = []
            try: background.undraw()
            except: background = None

            # Main Menu
            user_input = main_menu(size, colors).split(',')
            if user_input[0] == 'quit':
                playing = False            
            size = int(user_input[1])
            colors = int(user_input[2])
            max_turns = getMaxTurns(size, colors) + MAXTURNMODIFIER

            # Draw Grid
            title.setText("Flood fill")
            grid = generateGrid(size, colors)
            if user_input[0] != 'quit':
                background = draw_grid(size)
            status.setText(get_status())
            gameover = False    

            if STARTPOINTBYPLAYER:
                location = None
            previous_input = grid[0][0]
            player_input = previous_input 
            turns = 0

        # Game Loop
        else: 
            # Mouse Input     
            try:
                mouse_input = window.getMouse()
                grid_p1 = boxes[0][0].p1
                grid_p2 = boxes[size-1][size-1].p2
        
                if mouse_input.x > grid_p1.x and mouse_input.x < grid_p2.x and mouse_input.y > grid_p1.y and mouse_input.y < grid_p2.y:
                    player_input = getBoxValue(mouse_input, grid, boxes)
            except: 
                print("Player closed window")
                playing = False

            if player_input == None:
                player_input = previous_input

            # Set startpoint by player (based on STARTPOINTBYPLAYER bool)
            if location == None:
                location = getBoxLocation(mouse_input, boxes)
                player_input = previous_input
                turns -= 1

            # Handle Input
            if previous_input != player_input:
                # Update grid
                color_fill(grid, boxes, location, player_input)
                colors_remaining = getValuesLeft(grid)

                # check game state
                if turns >= max_turns: # lose state
                    title.setText("YOU LOST")
                    gameover = True
                elif colors_remaining <= 1: # win state
                    title.setText("YOU WON")
                    # Save Highscore
                    saveHighscore(turns, time.time() - start_time, size)

                    window.getMouse()
                    gameover = True            
                else: # playing state
                    turns += 1
                    status.setText(get_status())
                    previous_input = player_input

    # End
    window.close()


# TO-DO:
# calculate poitns
# highscore list on main menu
# fix recursion limit?

# DELETE LATER
COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'oldlace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque','peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue','lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slategray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy','cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue','royal blue', 'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steelblue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'mediumturquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine','dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green','pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green','yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod','light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'darkgoldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deeppink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple','medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1','AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4','PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3','NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2','cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3','honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2','MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2','SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4','blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3','DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1','LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2','SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3','LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1','PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2','CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4','cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3','DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2','DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1','PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3','SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3','chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1','DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3','khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3','LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3','yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3','goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1','IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4','burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3','wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1','firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4','salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4','orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3','DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4','OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2','DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2','pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1','maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3','VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3','orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2','MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3','DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1','MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3','thistle4','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8','gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17','gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26','gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35','gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45','gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54','gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63','gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72','gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81','gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90','gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
