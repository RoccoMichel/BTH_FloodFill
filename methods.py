import random

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


def getValuesLeft(grid, total):
    left = 0
    for i in range(total):
        if i in grid:
            left += 1
    return left


def getSquareValue(location, grid, squares): # linear not exponential 
    grid_size = len(squares)
    x = -1
    y = -1

    for i in range(grid_size):
        if location.y >= squares[i][0].p1.y and location.y <= squares[i][0].p2.y:
            x = i
    for j in range(grid_size):
        if location.x >= squares[0][j].p1.x and location.x <= squares[0][j].p2.x:
            y = j

    if x == -1 or y == -1:
        return None
    else:
        return grid[x][y]


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
            print("LEFT")
            color_fill(grid, boxes, [startpoint[0], startpoint[1]-1], new_value)

    # Check East
    if startpoint[1]+1 < len(grid):
        if grid[startpoint[0]][startpoint[1]+1] == compare_value:
            print("RIGHT")
            color_fill(grid, boxes, [startpoint[0], startpoint[1]+1], new_value)  

    
def getColor(index): # index is int
    match index:
        case 0:
            return "blue"
        case 1:
            return "red"
        case 2:
            return "yellow"
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


COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'oldlace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque','peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue','lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slategray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy','cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue','royal blue', 'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steelblue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'mediumturquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine','dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green','pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green','yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod','light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'darkgoldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deeppink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple','medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1','AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4','PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3','NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2','cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3','honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2','MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2','SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4','blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3','DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1','LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2','SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3','LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1','PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2','CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4','cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3','DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2','DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1','PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3','SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3','chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1','DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3','khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3','LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3','yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3','goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1','IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4','burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3','wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1','firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4','salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4','orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3','DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4','OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2','DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2','pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1','maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3','VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3','orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2','MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3','DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1','MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3','thistle4','gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8','gray9', 'gray10','gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17','gray18', 'gray19','gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26','gray27', 'gray28','gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35','gray36', 'gray37','gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45','gray46', 'gray47','gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54','gray55', 'gray56','gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63','gray64', 'gray65','gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72','gray73', 'gray74','gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81','gray82', 'gray83','gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90','gray91', 'gray92','gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']