import graphics
import methods

# Game Settings:
SIZE = 6
COLORS = 8 # max support for 8
MAXTURNS = 5

# Visual Settings:
WIDTH = 500
HEIGHT = 750
BACKGROUNDCOLOR = "DarkOrchid3"

def colorfill():
    pass

def get_status():
    return f"{turns}/{MAXTURNS}  |  {SIZE}x{SIZE}  |  Colors: {COLORS}"

if __name__ == "__main__":
    # Variables:
    turns = MAXTURNS
    grid = methods.generateGrid(SIZE, COLORS)

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

    # Grid
    box_size = 45
    box_margin = 2
    box_outline = 0
    grid_length = box_size * SIZE + box_margin * (SIZE-1)
    grid_start = graphics.Point(WIDTH/2 - grid_length/2, HEIGHT/8)
    
    for i in range(SIZE):
        for j in range(SIZE):
            p1 = graphics.Point(grid_start.x + (box_size * j) + (box_margin * j), grid_start.y + (box_size * i) + ((box_margin+1) * i))
            p2 = graphics.Point(grid_start.x + (box_size * (j+1)) + (box_margin * j), grid_start.y + box_size + (box_size * i+1) + ((box_margin+1) * i))
            square = graphics.Rectangle(p1, p2)
            square.setFill(methods.getColor(grid[j][i])) 
            square.setWidth(box_outline)
            square.draw(window)
    
    # Test Circle
    circle_center = graphics.Point(window.width/2, window.height/2)
    circle = graphics.Circle(circle_center, 25)
    circle.setFill("red")
    circle.setWidth(7)
    circle.draw(window)
    #input_box = graphics.Entry(graphics.Point(30, 40), 5)
    #input_box.draw(window)

    # Loop
    while turns > 0:
        point = window.getMouse()
        # change grind based on player input send as parameter?

        turns -= 1
        status.setText(get_status())
        circle.move(-circle.getP1().x, -circle.getP1().y)
        circle.move(point.x, point.y)


    # Save Highscore
    file = open("highscores.txt", 'w')
    file.write(f"Highscore: {MAXTURNS - turns}")
    file.close()



# 1. Spelet ska hålla reda på antalet drag som spelaren har gjort.
# 2. Om spelaren väljer samma färg som redan används ska det inte räknas som ett nytt drag.
# 3. Spelet avslutas när hela spelplanen har samma färg.
# 4. När spelet avslutas ska spelaren tilldelas en poäng baserad på antalet drag.
# 5. Poängen ska sparas i en high score-lista som lagras i en fil.
# Extrauppgifter:
#  - Låt spelaren välja spelplanens storlek inom ett givet minimi- och maxintervall.
#  - Låt spelaren välja antal färger inom ett givet minimi- och maxintervall.
#  - Mät tiden för en spelomgång och låt den påverka poängen. Färre drag ska dock alltid ge bättre resultat än fler drag.