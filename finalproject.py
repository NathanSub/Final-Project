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

class Pong(App):
    def __init__(self):
        super().__init__()
        bg_asset = ImageAsset("images/starfield.jpg")
        bg = Sprite(bg_asset, (0, 0))
        bg.scale = 2