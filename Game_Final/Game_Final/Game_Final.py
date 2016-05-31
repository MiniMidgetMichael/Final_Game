import turtle, functions

class tron(object):
    def __init__(self, color, is_AI = False):
        assert type(color) is str,"color must be a string, not %s" % type(color)
        assert type(is_AI) is bool,"is_AI must be a bool, not %s" % type(is_AI)
        self.color = color
        Turtle = turtle.Turtle()
        self.Turtle = Turtle
        Turtle.ht()
        Turtle.pu()
        ## hides turtle ('ht' = 'hideturtle')

        try:
            Turtle.color(color)
        except turtle.TurtleGraphicsError as e:
            print (e)
            return
        
        Turtle.pencolor(color)

def main_menu(scr):
    assert type(scr) is turtle._Screen,"scr must be turtle.Screen, not %s" % type(scr)
    players = screen.numinput("Number of players", "How many players? (1 or 2)", minval = 1, maxval = 2)
    if players == 1:
        p1_color = functions.good_input("What color do you want your bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p1 = tron(p1_color)
        p2_color = functions.good_input("What color do you want your enemy's bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p2 = tron(p2_color, is_AI = True)
        
        p1.Turtle.setx(200)
        p2.Turtle.setx(-200)
    else:
        p1_color = functions.good_input("Player 1: What color do you want your bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p1 = tron(p1_color)
        p2_color = functions.good_input("Player 2: What color do you want your bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p2 = tron(p2_color, is_AI = True)
        
        p1.Turtle.setx(200)
        p2.Turtle.setx(-200)

if __name__ == "__main__":
    screen = turtle.Screen()
    main_menu(screen)
    canvas = screen.getcanvas()
    screen.setup(900, 900)
    #sets screen size to 900x900 pixels