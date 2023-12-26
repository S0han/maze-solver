from setup import Window, Point, Line

def main():
    win = Window(800, 600)
    
    point1 = Point(0, 0)
    point2 = Point(50, 50)

    point3 = Point(75, 100)
    point4 = Point(75, 150)

    line1 = Line(point1, point2)
    line2 = Line(point3, point4)

    win.draw_line(line1, "red")
    win.draw_line(line2, "red")

    win.wait_for_close()


main()
print("Code Ended")