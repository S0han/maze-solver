from setup import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    a = Cell(win)
    a.has_bottom_wall = False
    a.draw(50, 50, 100, 100)

    b = Cell(win)
    b.has_left_wall = False
    b.has_right_wall = False
    b.draw(150, 150, 200, 200)


    win.wait_for_close()

main()
print("Code Ended")