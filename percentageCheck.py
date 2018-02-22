import os
import sys
from PIL import Image

def check(ima, imb, similarity):
    
    percentage = int(similarity) / 100

    ima2 = ima.resize((1,1), Image.ANTIALIAS)
    imb2 = imb.resize((1,1), Image.ANTIALIAS)
    
    colora = ima2.getpixel((0,0))
    colorb = imb2.getpixel((0,0))

    if((abs((colora[0] - colorb[0]) / colora[0])) <= percentage and (abs((colora[1] - colorb[1]) / colora[1])) <= percentage and (abs((colora[2] - colorb[2]) / colora[2])) <= percentage):
        return True
    else:
        return False 
