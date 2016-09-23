#!/usr/bin/env python
import sys
import PIL
from PIL import Image
filename = sys.argv[1]
im = Image.open(filename)
image = im.rotate(180)
image.save("ans2.png")
