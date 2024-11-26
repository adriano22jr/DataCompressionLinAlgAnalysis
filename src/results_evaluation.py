import sys, os, cv2
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr

input_name = ""
compression_algorithm = ""
if(len(sys.argv[1:]) == 2):
    input_name = sys.argv[1]
    compression_algorithm = sys.argv[2]
else:
    print("Specify those parameters:\n\t-Dataset name (es. ArtGallery, Blob, ecc...)\n\t-Compression algorithm (HEVC, AV1, VP9)")
    exit()


starter_path = "../datasets/" + input_name + "/"
videopath = "../results/compression/" + input_name.lower() + "-" + compression_algorithm.lower()
match compression_algorithm.lower():
    case "hevc":
        videopath = videopath + ".mp4"
    case "av1":
        videopath += ".mkv"
    case "vp9":
        videopath += ".webm"
uncompressed_path = "../results/decompression/" + compression_algorithm + "/" + input_name + "/"

number_of_files = len(next(os.walk(starter_path))[2])

# Calculate the SSIM
ssim_percentages = []
for number in range(number_of_files):
    num = str(number).zfill(3)
    
    # Open both images    
    image1 = cv2.imread(starter_path + "Frame_" + num + ".png", 0)
    image2 = cv2.imread(uncompressed_path + "Frame_" + num + ".png", 0)
    
    # Check if the images have the same size
    if image1.shape != image2.shape:
        print("Error: Images have different sizes")
    else:
        ssim_score, dif = ssim(image1, image2, full=True)
        ssim_percentages.append(ssim_score * 100)
        # print(f"Percentage of equality on frame {num}: {ssim_score * 100}%")
    
# Calculate the average percentage of equality
average_percentage = sum(ssim_percentages) / len(ssim_percentages)
print("Average percentage of equality: {}%".format(average_percentage))


# Calculate the PSNR
psnr_values = []
for number in range(number_of_files):
    num = str(number).zfill(3)
    
    # Open both images    
    image1 = cv2.imread(starter_path + "Frame_" + num + ".png", 0)
    image2 = cv2.imread(uncompressed_path + "Frame_" + num + ".png", 0)
    
    # Check if the images have the same size
    if image1.shape != image2.shape:
        print("Error: Images have different sizes")
    else:
        psnr_score = psnr(image1, image2)
        psnr_values.append(psnr_score)
        # print(f"Amount of noise on frame {num}: {psnr_score} db")

#Calculate the average number of noise
average_noise = sum(psnr_values) / len(psnr_values)
print("Average amount of noise: {} db".format(average_noise))


# Calculate the compression ratio
size = 0
folderpath = os.path.abspath(os.path.dirname(starter_path))
for path, dirs, files in os.walk(folderpath):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)

videosize = os.stat(os.path.abspath(videopath)).st_size  
print("Initial size of dataset: {} MB".format(size/1000000))
print("Final size of dataset: {} MB".format(videosize/1000000))
print("Compression ratio: " + str(size/videosize)) 