import turtle, functions, time, tkinter


class tron(object):
    def __init__(self, color, screen, player, is_AI = False):
        assert type(color) is str,"color must be a string, not %s" % type(color)
        assert type(is_AI) is bool,"is_AI must be a bool, not %s" % type(is_AI)
        assert type(player) is int, "player must be an int, not %s" % type(player)
        self.color = color
        self.screen = screen
        self.is_AI = is_AI
        self.player = player
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

    def set_controls(self, ctrls):
        screen = self.screen
        Turtle = self.Turtle
        screen.listen()
        screen.onkeypress(screen.bye, "space")
        assert type(ctrls) is dict, "ctrls must be dict, {'key' : fun,  ...} not %s" % type(ctrls)
        for k, f in ctrls.items():
            screen.onkeypress(f, k)

    def cycle(self):
        is_AI = self.is_AI
        screen = self.screen
        Turtle = self.Turtle
        player = self.player
        if player == 1 and Turtle.xcor() == -20:
            print ("Player 1, you died!")
            screen.bye()
            return
        #elif player == 2 and Turtle.xcor() == 20:
        #    print ("Player 2, you died!")
        #    screen.bye()
        #    return
        Turtle.fd(2)
        time.sleep(0.0125)
        print (Turtle.pos())

def main_menu(scr):
    assert type(scr) is turtle._Screen,"scr must be turtle.Screen, not %s" % type(scr)
    players = screen.numinput("Number of players", "How many players? (1 or 2)", minval = 1, maxval = 2)
    if players == 1:
        p1_color = functions.good_input("What color do you want your bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p1 = tron(p1_color, scr, 1)
        p2_color = functions.good_input("What color do you want your enemy's bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p2 = tron(p2_color, scr, 2, is_AI = True)
        
        p1.Turtle.setx(-200)
        p2.Turtle.setx(200)
    else:
        p1_color = functions.good_input("Player 1: What color do you want your bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p1 = tron(p1_color, scr, 1)
        p2_color = functions.good_input("Player 2: What color do you want your bike to be?: \n", values = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'])
        p2 = tron(p2_color, scr, 2, is_AI = True)
        
        p1.Turtle.setx(-200)
        p2.Turtle.setx(200)
    p2.Turtle.rt(180)
    return p1, p2, int(players)

def play(p1, p2, num_players):
    p1_ready = functions.good_input("Player 1: Are you ready? [y or n] : \n", values = ['y', 'n']).casefold()
    while not(p1_ready == 'y'):
        print ("Waiting...")
        time.sleep(1)
        p1_ready = functions.good_input("Player 1: Are you ready? [y or n] : \n", values = ['y', 'n']).casefold()
    else:
        if num_players == 2:
            p2_ready = functions.good_input("Player 2: Are you ready? [y or n] : \n", values = ['y', 'n']).casefold()
            while not(p2_ready == 'y'):
                print ("Waiting...")
                time.sleep(1)
                p2_ready = functions.good_input("Player 2: Are you ready? [y or n] : \n", values = ['y', 'n']).casefold()
            all_ready = True
        else:
            all_ready = True

    if all_ready:
        p1.Turtle.st()
        p2.Turtle.st()
        p1.Turtle.pd()
        p2.Turtle.pd()
        print ("Press space to quit!")
        ## screen.ontimer(fun, int (in milliseconds))
        ##screen.listen()


if __name__ == "__main__":
    screen = turtle.Screen()
    p1, p2, players = main_menu(screen)
    canvas = screen.getcanvas()
    screen.bgpic("P:/Python/Final_Game/Game_Final/Resources/Grid.gif")
    screen.setup(900, 900)
    #screen.listen()
    def p1_left():
        p1.Turtle.lt(90)
    def p1_right():
        p1.Turtle.rt(90)
    def p2_left():
        p2.Turtle.lt(90)
    def p2_right():
        p2.Turtle.rt(90)

    p1_ctrls = {
        'a' : p1_left,
        'd' : p1_right
    }
    p2_ctrls = {
        'Left' : p2_left,
        'Right' : p2_right
    }
    if players == 1:
        p1.set_controls(p1_ctrls)
    else:
        p1.set_controls(p1_ctrls)
        p2.set_controls(p2_ctrls)

    play(p1, p2, players)

    
    while screen._RUNNING:
        p1.cycle()
        p2.cycle()
    #sets screen size to 900x900 pixels