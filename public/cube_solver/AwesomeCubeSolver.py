import glob
import cv2
import os
import numpy as np
import DominantColor  # Make sure you have the DominantColor module or function available

images = [{"convertedFile": cv2.imread(file), "name": file.split("\\")[-1].split(".")[0]} for file in glob.glob(os.getcwd() + "/public/cube_images/*.jpg")]

for image in images: 
    cubies = []
    img = image["convertedFile"]

    height, width, channels = img.shape
    # Number of pieces Horizontally 
    W_SIZE  = 3 
    # Number of pieces Vertically to each Horizontal  
    H_SIZE = 3

    for ih in range(H_SIZE ):
        for iw in range(W_SIZE ):
            x = width//W_SIZE * iw 
            y = height//H_SIZE * ih
            h = (height // H_SIZE)
            w = (width // W_SIZE )
            cubies.append(img[int(y):int(y+h), int(x):int(x+w)])
    
    newCubies = np.array(cubies)
    newCubies_1 = []
    for cubieSide in newCubies:
        newCubies_1.append(DominantColor.get_dominant_color(cubieSide))  # Make sure DominantColor.getDominantColor() is defined
    print(newCubies_1, image["name"])