import graphics
import methods

# Game Settings:
SIZE = 8
COLORS = 7 # max support for 8
MAXTURNS = 15

# Visual Settings:
WIDTH = 500
HEIGHT = 750
BACKGROUNDCOLOR = "DarkOrchid3"
BOXSIZE = 25
BOXMARGIN = 0
BOXOUTLINE = 1

def colorfill():
    pass

def get_status():
    return f"{turns}/{MAXTURNS}  |  {SIZE}x{SIZE}  |  Colors: {COLORS}"

if __name__ == "__main__":
    # Variables:
    turns = MAXTURNS
    grid = methods.generateGrid(SIZE, COLORS)
    squares = []

    # Create window
    window = graphics.GraphWin(f"Flood Fill Game\t(Rocco Michel)", WIDTH, HEIGHT)
    window.setBackground(BACKGROUNDCOLOR)

    # Main Menu
    title = graphics.Text(graphics.Point(WIDTH/2, 20), "Flood fill")   
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor("white")
    title.setFace("times roman")

    status = graphics.Text(graphics.Point(WIDTH/2, 40), get_status())
    status.setFace("times roman")    

    title.draw(window)
    status.draw(window)

    # Draw Grid
    grid_length = BOXSIZE * SIZE + BOXMARGIN * (SIZE-1)
    grid_start = graphics.Point(WIDTH/2 - grid_length/2, HEIGHT/8)
    
    for i in range(SIZE):
        squres_row = []
        for j in range(SIZE):            
            p1 = graphics.Point(grid_start.x + (BOXSIZE * j) + (BOXMARGIN * j), grid_start.y + (BOXSIZE * i) + ((BOXMARGIN+1) * i))
            p2 = graphics.Point(grid_start.x + (BOXSIZE * (j+1)) + (BOXMARGIN * j), grid_start.y + BOXSIZE + (BOXSIZE * i+1) + ((BOXMARGIN+1) * i))
            square = graphics.Rectangle(p1, p2)
            square.setFill(methods.getColor(grid[j][i])) 
            square.setWidth(BOXOUTLINE)
            square.draw(window)

            squres_row.append(square)
        squares.append(squres_row)
    
    #input_box = graphics.Entry(graphics.Point(30, 40), 5)
    #input_box.draw(window)

    # Game Loop
    player_input = ""
    previous_input = ""
    while turns > 0:   
        # Mouse Input     
        mouse_input = window.getMouse()
        grid_p1 = squares[0][0].p1
        grid_p2 = squares[SIZE-1][SIZE-1].p2

        if mouse_input.x > grid_p1.x and mouse_input.x < grid_p2.x and mouse_input.y > grid_p1.y and mouse_input.y < grid_p2.y:
            player_input = methods.getSquareValue(mouse_input, grid, squares)

        if player_input == None:
            player_input = previous_input

        # Handle Input
        if previous_input != player_input:
            print(player_input, " | ", methods.getColor(player_input))

            # UPDATE GRID SOMEHOW ----------------------------------------------------
            
            turns -= 1
            status.setText(get_status())

            previous_input = player_input

    # Save Highscore
    file = open("highscores.txt", 'w')
    file.write(f"Highscore: {MAXTURNS - turns}")
    file.close()

    # End
    window.close()


# 1. Spelet ska hålla reda på antalet drag som spelaren har gjort.
# 2. Om spelaren väljer samma färg som redan används ska det inte räknas som ett nytt drag.
# 3. Spelet avslutas när hela spelplanen har samma färg.
# 4. När spelet avslutas ska spelaren tilldelas en poäng baserad på antalet drag.
# 5. Poängen ska sparas i en high score-lista som lagras i en fil.
# Extrauppgifter:
#  - Låt spelaren välja spelplanens storlek inom ett givet minimi- och maxintervall.
#  - Låt spelaren välja antal färger inom ett givet minimi- och maxintervall.
#  - Mät tiden för en spelomgång och låt den påverka poängen. Färre drag ska dock alltid ge bättre resultat än fler drag.