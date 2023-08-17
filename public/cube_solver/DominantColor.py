import cv2
import numpy as np


color_ranges = {
    'r1': ([0, 30, 20], [10, 255, 255]),         # Red is at both ends of the hue spectrum
    'r2': ([160,100,20], [179,255,255]), 
    'b': ([90, 100, 100], [130, 255, 255]),    # Blue is between 100 and 130 in hue
    'g': ([40, 100, 100], [80, 255, 255]),     # Green is between 40 and 80 in hue
    'y': ([25, 100, 100], [39, 255, 255]),   # Yellow is between 20 and 40 in hue
    'w': ([0, 0, 200], [255, 200, 255]),       # White is defined by lower saturation and value
    'o': ([10, 100, 20], [25, 255, 255])    # Orange is between 10 and 20 in hue
}

def detect_main_color(hsv_image):
    color_found = 'undefined'
    max_count = 0

    for color_name,(lower_val, upper_val) in color_ranges.items():
        # threshold the HSV image - any matching color will show up as white
        mask = cv2.inRange(hsv_image, np.array(lower_val), np.array(upper_val))
        # count white pixels on mask
        count = np.sum(mask)
        if count > max_count:
            color_found = color_name
            max_count = count
        if color_found in ["r1", "r2"]:
            color_found = "r"
        if color_found == 'undefined':
            color_found = "w" #temporary fix for now I dont know how will I work with this
    return color_found

def get_dominant_color(image):
    

   # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to create a mask of non-black pixels
    _, mask = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

    # Find the contours of the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (the center color region)
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding rectangle of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the original image to the bounding rectangle
    cropped_image = image[y:y+h, x:x+w]
    # print(cropped_image)
    cv2.imwrite("result.png", cropped_image)

    # # Display the color region
    # cv2.imshow('mask', cropped_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    detected_color = detect_main_color(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV))
    return detected_color