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

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
                 

def compressor_AV1VS(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["../../bin/ffmpeg", "-framerate", "120", "-i", input_file, "-crf", "3", "-c:v", "libaom-av1", output_file])
    
    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video


def compressor_VP9VS(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["../../bin/ffmpeg", "-framerate", "120", "-i", input_file, "-crf", "3", "-c:v", "libvpx-vp9", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    
    
def compressor_HEVC(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["../../bin/ffmpeg", "-framerate", "120", "-i", input_file, "-crf", "3", "-c:v", "libvpx-vp9", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    
    
def compressor_VP9(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["./ffmpeg/bin/ffmpeg", "-framerate", "120", "-i", input_file, "-c:v", "libvpx-vp9", "-lossless", "1", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    
    
def compressor_AV1(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["./ffmpeg/bin/ffmpeg", "-framerate", "120", "-i", input_file, "-c:v", "libaom-av1", "-aom-params", "lossless=1", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    

def compressor_HUFFYUV(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["./ffmpeg/bin/ffmpeg", "-framerate", "120", "-i", input_file, "-c:v", "huffyuv", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    
    
def compressor_UTVIDEO(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["./ffmpeg/bin/ffmpeg", "-framerate", "120", "-i", input_file, "-c:v", "utvideo", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video
    
    
def compressor_FFV1(input_path, output_path):
    # set input and output paths
    input_file = input_path
    output_file = output_path
    
    startTime = time.time()
    
    # call ffmpeg to compress the video
    subprocess.run(["./ffmpeg/bin/ffmpeg", "-framerate", "120", "-i", input_file, "-level", "3", "-coder", "2", "-c:v", "ffv1", output_file])

    endTime = time.time()
    print(f"Encoded in {endTime - startTime} seconds.")  # print the time taken to encode the video