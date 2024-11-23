import cv2, imageio, av, os, subprocess, time
import imageio.v3 as iio
import imageio.plugins.pyav as pyav
import numpy as np
from pathlib import Path
from PIL import Image, ImageChops

def compressor_HEVCVS(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["../../bin/ffmpeg", "-framerate", "120", "-i", input_file, "-crf", "18", "-c:v", "libx265", output_file])
    
    # compress ratio evaluation
    size = 0
    folderpath = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
            
    endTime = time.time()
    
    videosize = os.stat(os.path.abspath(output_path)).st_size   
    print(f"encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    print("compression ratio: " + str(size/videosize))      
            
            

def compressor_AV1VS(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["../../bin/ffmpeg", "-framerate", "120", "-i", input_file, "-crf", "3", "-c:v", "libaom-av1", output_file])
    
    # compress ratio evaluation
    size = 0
    folderpath = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
            
    endTime = time.time()

    videosize = os.stat(os.path.abspath(output_path)).st_size  
    print(f"encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    print("compression ratio: " + str(size/videosize))    


def compressor_VP9VS(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["../../bin/ffmpeg", "-framerate", "120", "-i", input_file, "-crf", "3", "-c:v", "libvpx-vp9", output_file])
    
    # compress ratio evaluation
    size = 0
    folderpath = os.path.abspath(os.path.dirname(input_path))
    for path, dirs, files in os.walk(folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
            
    endTime = time.time()
            
    videosize = os.stat(os.path.abspath(output_path)).st_size   
    print(f"encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    print("compression ratio: " + str(size/videosize))    