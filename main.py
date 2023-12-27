from setup import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    box = Cell(win)
    box.has_bottom_wall = False
    box.draw(50, 50, 100, 100)

    win.wait_for_close()

main()
print("Code Ended")