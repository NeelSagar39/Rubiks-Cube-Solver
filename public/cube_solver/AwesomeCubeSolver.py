from collections import Counter

import cv2
import os
import numpy as np
import DominantColor  

from Cube.cube import Cube
from Cube.Solver import kociemba 


def get_state_from_images(images):
    
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
        newCubiesWithColor = []
        for cubieSide in newCubies:
            newCubiesWithColor.append(DominantColor.get_dominant_color(cubieSide))  # Make sure DominantColor.getDominantColor() is defined
        image["state"] = ''.join(newCubiesWithColor)
    
    return images

def get_state_in_sequence(images):
    expectedColorStructure =[ "white_side", "orange_side", "green_side", "red_side", "blue_side", "yellow_side"]
    state=""
    for color in expectedColorStructure: 
        desired_dict = None
        for img_dict in images:
            if img_dict["name"] == color:
                desired_dict = img_dict
        print(color)
        state = state+desired_dict["state"] 
    return state

if __name__ == "__main__":
    expectedColorStructure = ["blue_side", "yellow_side","orange_side", "white_side", "red_side", "green_side"]
    images = [{"convertedFile": cv2.imread(os.getcwd() + f"/cube_images/{name}.jpg"), "name": name} for name in expectedColorStructure]
    images = get_state_from_images(images)
    state = get_state_in_sequence(images)
    character_counts = Counter(state)
    for char, count in character_counts.items():
        print(f"'{char}' appears {count} times.")
    c = Cube(state)
    print(c)
    solution = kociemba.solve(c)
    solution = solution.replace("D`", "R L F2 B2 R` L` U` R L F2 B2 R` L`")
    solution = solution.replace("D", "R L F2 B2 R` L` U R L F2 B2 R` L`")
    print(solution)