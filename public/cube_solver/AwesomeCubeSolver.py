import json
import cv2
import os
import numpy as np
import DominantColor  # Make sure you have the DominantColor module or function available
from DatabaseBuilder import IDA_star, build_heuristic_db
from rubik.cube import Cube
from rubik.solve import Solver
def get_state_from_images(images):
    
    state = ""
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
        state = state + "".join(newCubiesWithColor)

    return state

if __name__ == "__main__":
    expectedColorStructure = ["blue_side", "yellow_side","orange_side", "white_side", "red_side", "green_side"]
    images = [{"convertedFile": cv2.imread(os.getcwd() + f"/public/cube_images/{name}.jpg"), "name": name} for name in expectedColorStructure]
    state = get_state_from_images(images)
    print(state)

    # # START TO SOLVE THE CUBE 
    # MAX_MOVES = 5
    # NEW_HEURISTICS = False
    # HEURISTIC_FILE = 'heuristic.json'

    # #--------------------------------
    # cube = RubiksCube(n=3, state=state)
    # cube.show()
    # print('-----------')
    # #--------------------------------

    # if os.path.exists(HEURISTIC_FILE):
    #     print("File exists")
    #     with open(HEURISTIC_FILE) as f:
    #         h_db = json.load(f)
    # else:
    #     h_db = None

    # if h_db is None or NEW_HEURISTICS is True:
    #     actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]
    #     h_db = build_heuristic_db(
    #         cube.stringify(),
    #         actions,
    #         max_moves = MAX_MOVES,
    #         heuristic = h_db
    #     )

    #     with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
    #         json.dump(
    #             h_db,
    #             f,
    #             ensure_ascii=False,
    #             indent=4
    #         )
    # # #--------------------------------
    # # cube.shuffle(
    # #     l_rot = MAX_MOVES if MAX_MOVES < 5 else 5,
    # #     u_rot = MAX_MOVES
    # # )
    # # cube.show()
    # # print('----------')
    # #--------------------------------
    # solver = IDA_star(h_db)
    # moves = solver.run(cube.stringify())
    # print(moves)

    # for m in moves:
    #     if m[0] == 'h':
    #         cube.horizontal_twist(m[1], m[2])
    #     elif m[0] == 'v':
    #         cube.vertical_twist(m[1], m[2])
    #     elif m[0] == 's':
    #         cube.side_twist(m[1], m[2])
    # cube.show()

    c = Cube("rbrybwoboyyyyyyyrwoooooobbbwwwwwwwryrrrrrrbbbggggggggg".upper())
    print(c)
    solver = Solver(c)
    solver.solve()

