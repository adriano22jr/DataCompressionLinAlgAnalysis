import sys, os, cv2
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim

input_name = ""
compression_algorithm = ""
if(len(sys.argv[1:]) == 2):
    input_name = sys.argv[1]
    compression_algorithm = sys.argv[2]
else:
    print("Specify those parameters:\n\t-Dataset name (es. ArtGallery, Blob, ecc...)\n\t-Compression algorithm (HEVC, AV1, VP9)")
    exit()


starter_path = "../datasets/" + input_name + "/"
uncompressed_path = "../results/decompression/" + compression_algorithm + "/" + input_name + "/"

number_of_files = len(next(os.walk(starter_path))[2])

percentages = []
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
        percentages.append(ssim_score * 100)
        print(f"Percentage of equality on frame {num}: {ssim_score * 100}%")
    
# Calculate the average percentage of equality
average_percentage = sum(percentages) / len(percentages)
print("Average percentage of equality: {}%".format(average_percentage))