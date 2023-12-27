from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Python Maze Solver")
        self.canvas = Canvas(self.__root, {"height": height, "width": width, "bg": "white"})
        self.canvas.pack(fill = BOTH, expand = 1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while (self.running == True):
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = fill_color, width = 2)
        canvas.pack(fill = BOTH, expand = 1)

    