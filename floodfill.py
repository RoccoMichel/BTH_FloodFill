import graphics
import methods

# Game Settings:
SIZE = 8
COLORS = 8 # max support for 8      ----------------- add more
MAXTURNS = 30
STARTPOINT = [0, 0]

# Visual Settings:
WIDTH = 450
HEIGHT = 650
BOXSIZE = 30
BOXMARGIN = 2
BOXOUTLINE = 2
BACKGROUNDOUTLINE = 10
BACKGROUNDCOLOR = "DarkOrchid3"
TEXTCOLOR = "white"

def get_status():
    return f"{turns}/{MAXTURNS}  |  {SIZE}x{SIZE}  |  Colors: {COLORS}"

if __name__ == "__main__":
    # Variables:
    turns = MAXTURNS
    grid = methods.generateGrid(SIZE, COLORS)
    boxes = []

    # Create window
    window = graphics.GraphWin(f"Flood Fill Game\t(Rocco Michel)", WIDTH, HEIGHT)
    window.setBackground(BACKGROUNDCOLOR)

    # Main Menu
    title = graphics.Text(graphics.Point(WIDTH/2, 20), "Flood fill")   
    title.setSize(20)
    title.setStyle("bold")
    title.setTextColor(TEXTCOLOR)
    title.setFace("times roman")

    status = graphics.Text(graphics.Point(WIDTH/2, 40), get_status())
    status.setFace("times roman")    
    status.setTextColor(TEXTCOLOR)

    title.draw(window)
    status.draw(window)

    # Draw Grid
    grid_length = BOXSIZE * SIZE + BOXMARGIN * (SIZE-1)
    grid_start = graphics.Point(WIDTH/2 - grid_length/2, HEIGHT/7)

    background = graphics.Rectangle(grid_start, graphics.Point(grid_start.x + grid_length, grid_start.y + grid_length + (1 * SIZE)))
    background.setFill(BACKGROUNDCOLOR)
    background.setWidth(BACKGROUNDOUTLINE)
    background.draw(window)
    
    for i in range(SIZE):
        squres_row = []
        for j in range(SIZE):            
            p1 = graphics.Point(grid_start.x + (BOXSIZE * j) + (BOXMARGIN * j), grid_start.y + (BOXSIZE * i) + ((BOXMARGIN+1) * i))
            p2 = graphics.Point(grid_start.x + (BOXSIZE * (j+1)) + (BOXMARGIN * j), grid_start.y + BOXSIZE + (BOXSIZE * i+1) + ((BOXMARGIN+1) * i))
            square = graphics.Rectangle(p1, p2)
            square.setFill(methods.getColor(grid[i][j])) 
            square.setWidth(BOXOUTLINE)
            square.draw(window)

            squres_row.append(square)
        boxes.append(squres_row)
       
    #input_box = graphics.Entry(graphics.Point(30, 40), 5)
    #input_box.draw(window)

    # Game Loop
    player_input = ""
    previous_input = grid[STARTPOINT[0]][int(STARTPOINT[1])]

    while turns > 0:   
        # Mouse Input     
        mouse_input = window.getMouse()
        grid_p1 = boxes[0][0].p1
        grid_p2 = boxes[SIZE-1][SIZE-1].p2
        
        if mouse_input.x > grid_p1.x and mouse_input.x < grid_p2.x and mouse_input.y > grid_p1.y and mouse_input.y < grid_p2.y:
            player_input = methods.getSquareValue(mouse_input, grid, boxes)

        if player_input == None:
            player_input = previous_input

        # Handle Input
        if previous_input != player_input:

            # Update grid
            methods.color_fill(grid, boxes, STARTPOINT, player_input)

            print(methods.getValuesLeft(grid, COLORS))
            if methods.getValuesLeft(grid, COLORS) <= 1:
                title.setText("YOU WIN")

            
            turns -= 1
            status.setText(get_status())
            previous_input = player_input

    # WIN / LOSE
    title.setText("YOU LOSE")

    window.getMouse()

    # Save Highscore
    file = open("highscores.txt", 'w')
    file.write(f"Highscore: {MAXTURNS - turns}")
    file.close()

    # End
    window.close() # Should never trigger? User should close program manually.

# TO-DO:
# fix methods.getValuesLeft()
# win/lose condition
# new game settings
# save time with highscore

# 1. Spelet ska hålla reda på antalet drag som spelaren har gjort.
# 2. Om spelaren väljer samma färg som redan används ska det inte räknas som ett nytt drag.
# 3. Spelet avslutas när hela spelplanen har samma färg.
# 4. När spelet avslutas ska spelaren tilldelas en poäng baserad på antalet drag.
# 5. Poängen ska sparas i en high score-lista som lagras i en fil.
# Extrauppgifter:
#  - Låt spelaren välja spelplanens storlek inom ett givet minimi- och maxintervall.
#  - Låt spelaren välja antal färger inom ett givet minimi- och maxintervall.
#  - Mät tiden för en spelomgång och låt den påverka poängen. Färre drag ska dock alltid ge bättre resultat än fler drag.