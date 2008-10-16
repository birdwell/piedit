"""Class to access information about piet colors"""
import sys
import gtk

__author__ = "Steven Anderson"
__copyright__ = "None, it's yours"
__credits__ = ["Steven Anderson"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Steven Anderson"
__email__ = "steven.james.anderson@googlemail.com"
__status__ = "Production"

colors = (
    "#FFC0C0",
    "#FF0000",
    "#C00000",
    "#FFFFC0",
    "#FFFF00",
    "#C0C000",
    "#C0FFC0",
    "#00FF00",
    "#00C000",
    "#C0FFFF",
    "#00FFFF",
    "#00C0C0",
    "#C0C0FF",
    "#0000FF",
    "#0000C0",
    "#FFC0FF",
    "#FF00FF",
    "#C000C0",
    "#FFFFFF",
    "#000000",
)

color_mappings = {}
for index,color in enumerate(colors):
    color_mappings[color] = index

white = (255,255,255)
white_hex = "#FFFFFF"
black = (0,0,0)
black_hex = "#000000"

num_hues = 6
num_lights = 3

def all_colors():
    for color in colors:
        yield color
        
def rgb_to_hex(rgb):
    #print rgb
    return '#%02x%02x%02x'.upper() % rgb

def hex_to_rgb(hex):
    return (int(hex[1:3],16),int(hex[3:5],16),int(hex[5:7],16))

def hue_light_diff(from_color,to_color):
    from_hue, from_light = divmod(color_mappings[rgb_to_hex(from_color)],num_lights)
    to_hue, to_light = divmod(color_mappings[rgb_to_hex(to_color)],num_lights)
    
    #print "From Hue Light: %s,%s,%s, To Hue Light: %s,%s,%s" % (from_color,from_hue,from_light,to_color,to_hue,to_light)
    
    hue_diff, light_diff = to_hue - from_hue, to_light - from_light
    if hue_diff <0:
        hue_diff = hue_diff + num_hues
    if light_diff <0:
        light_diff = light_diff + num_lights
    
    return (hue_diff, light_diff)