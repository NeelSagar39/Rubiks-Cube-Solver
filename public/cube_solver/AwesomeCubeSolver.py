from collections import Counter
from ancient.Cube import RubiksCube

import cv2
import os
import numpy as np
import DominantColor  

from twophase import solve_best

from Cube.cube import Cube
from Cube.Solver import beginners 


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
    expectedColorStructure = ["blue_side", "white_side", "orange_side","green_side","yellow_side", "red_side"]
    # expectedColorStructure =["blue_side", "yellow_side","orange_side", "white_side", "red_side", "green_side"]
    # expectedColorStructure =[ "white_side", "orange_side", "green_side", "red_side", "blue_side", "yellow_side"]
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

    #--------------------------------
    cube = RubiksCube(n=3, state=state) 
    cube.show()
    print('-----------')
    #--------------------------------

    state = state.replace('b', 'U')
    state = state.replace('o', 'F')
    state = state.replace('y', 'L')
    state = state.replace('r', 'B')
    state = state.replace('w', 'R')
    state = state.replace('g', 'D')
    print(state)
    character_counts = Counter(state)

    for char, count in character_counts.items():
        print(f"'{char}' appears {count} times.")
    moves = solve_best(state.upper())
    print(moves)
    # c = Cube(state)
    # # c.scramble()
    # print(c)
    # print(beginners.solve(c))