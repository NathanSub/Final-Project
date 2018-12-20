'''
This is the code for Nathan Subrahmanian's Final Project!

Sources:

'''

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import ImageAsset, Frame, Sound, SoundAsset, TextAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
eye = Color(0xdee5ef, 1.0)
sand = Color(0xefe49b, 1.0)
meadowgreen = Color(0x8ed334, 1.0)
orange = Color(0xe59e19, 1.0)

thinline = LineStyle(1, black)
noline = LineStyle(0, black)


class Paddle1(Sprite):
    paddle1 = ImageAsset("pingpongpaddle1.jpg",
    Frame(227,0,65,125), 4, 'vertical')
    
    def __init__(self, position):
        super().__init__(Paddle1.paddle1, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        self.center = (0.5, 0.5)

        SpaceShooter.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        SpaceShooter.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        SpaceShooter.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        SpaceShooter.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        
                
    def rightarrowKey(self, event):
        self.vx+=.2
        '''print(ImageAsset("images/blast.png"))'''
        
    def leftarrowKey(self, event):
        self.vx+=-.2
        
    def uparrowKey(self, event):
        self.vy+=-.2
        
    def downarrowKey(self, event):
        self.vy+=.2


    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        collision = self.collidi


class Pong(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/tenniscourt1.jpg")
        bg = Sprite(bg_asset, (-100, -115))
        bg.scale = 2
        self.paddle1 = Paddle1((500, 30))
    
myapp = Pong()

myapp.run()