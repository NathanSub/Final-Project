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
    paddle1 = RectangleAsset(100, 500, thinline, red)
    
    def __init__(self, position):
        super().__init__(Paddle1.paddle1, position)
        self.vx = 1
        self.vy = 1
        self.center = (0.5, 0.5)
        self.scale = 0.2

        Pong.listenKeyEvent("keydown", "right arrow", self.rightarrowKey)
        Pong.listenKeyEvent('keydown', "left arrow", self.leftarrowKey)
        Pong.listenKeyEvent('keydown', "up arrow", self.uparrowKey)
        Pong.listenKeyEvent('keydown', "down arrow", self.downarrowKey)
        
                
    def rightarrowKey(self, event):
        self.vx+=.2
        
    def leftarrowKey(self, event):
        self.vx+=-.2
        
    def uparrowKey(self, event):
        self.vy+=-.2
        
    def downarrowKey(self, event):
        self.vy+=.2


    def step(self):
        self.x += self.vx
        self.y += self.vy

class Pong(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/tenniscourt1.jpg")
        bg = Sprite(bg_asset, (-100, -115))
        bg.scale = 2
        
        self.paddle1 = Paddle1((100, 300))
        
        self.paddle2 = Paddle2((600, 300)
    
myapp = Pong()

myapp.run()