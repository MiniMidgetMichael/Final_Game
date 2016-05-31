import turtle

screen = turtle.Screen()
class tron(object):
    def __init__(self, color):
        assert type(color) is str,"color must be a string, not %s" % type(color)
        self.color = color
        Turtle = turtle.Turtle()
        self.turtle = Turtle
        Turtle.hideturtle()
        try:
            Turtle.color(color)
        except turtle.TurtleGraphicsError as e:
            print (e)
            return
            
blue = tron("blue")
orange = tron("orange")
#test = tron("test")