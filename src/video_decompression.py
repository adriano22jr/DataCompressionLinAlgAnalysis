import imageio as iio
import numpy as np
import imageio.plugins.pyav as pyav
import av, sys
from PIL import Image, ImageChops
from pathlib import Path

input_path = ""
output_path = ""
if(len(sys.argv[1:]) == 2):
    input_path = sys.argv[1]
    output_path = sys.argv[2]
else:
    print("Specify those parameters:\n\t-Input path (es. output.mp4)\n\t-Output path (es. result/Frame_%d.png)")
    exit()

imgDec = ""
container = av.open(input_path, mode = "r") 
stream = container.streams.video[0]
count = 0
for frame in container.decode(stream):
    if(count == 0):
        imgDec = frame.to_image()
    frame.to_image().save(output_path % count)
    count += 1