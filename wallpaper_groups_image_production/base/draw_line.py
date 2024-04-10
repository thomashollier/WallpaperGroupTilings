import cv2
import numpy as np
from PIL import Image

# Mirror
def refelection(img, point, color):
    cv2.line(img, point[0], point[1], color, 2)

def glide_refelection(img, point, color):
    cv2.line(img, point[0], point[1], color, 1)

# Rhombus points
def rhomb(img, point, color):
    # (x,y)->(x-1,y),(x+1,y),(x,y-2),(x,y+2) array[[],[]]
    points = np.array(
        [[[point[0] - 4, point[1]], [point[0], point[1] - 4], [point[0] + 4, point[1]], [point[0], point[1] + 4]]])
    # print(points)
    cv2.polylines(img, points, True, color)
    cv2.fillPoly(img, points, color)

# Square points
def square(img, point, color):
    cv2.rectangle(img, (point[0] - 4, point[1] - 4), (point[0] + 4, point[1] + 4), color, -1)

# Triangle points
def tri(img, point, color):
    points = np.array(
        [[[point[0], point[1] - 4], [point[0] - 4, point[1] + 4], [point[0] + 4, point[1] + 4]]])
    cv2.polylines(img, points, True, color)
    cv2.fillPoly(img, points, color)

# Hexagon
def hex(img, point, color):
    points = np.array(
        [[[point[0] - 2, point[1] - 3], [point[0] - 4, point[1]], [point[0] - 2, point[1] + 2],
          [point[0] + 2, point[1] + 2], [point[0] + 4, point[1]], [point[0] + 2, point[1] - 3]]])
    cv2.polylines(img, points, True, color)
    cv2.fillPoly(img, points, color)

def draw(img, draw_list):
    # Draw lines
    cv2.line(np.array(img),(0,0),(200,200),(255,0,0),5)
    # Draw rectangles
    cv2.rectangle(np.array(img),(0,0),(200,200),(255,0,0),-1) # Coordinates of upper left and lower right corners
    _, _, _, alpha = img.split()
    img = np.array(img.convert('RGB'))
    for func, *parameter in draw_list:
        eval(func)(img, *parameter)
    print("---\n")
    img = Image.fromarray(img)
    img.putalpha(alpha)
    return img
