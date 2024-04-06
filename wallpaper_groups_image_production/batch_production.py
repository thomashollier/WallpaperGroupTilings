import os
from base.seventeen_wallpaper import *
from base.point import Point
from base.cell import rotatedRectWithMaxArea
import numpy as np
import random
from PIL import Image

def batch_production(l, m, deg, img_num, source_folder, save_image_path, width, height, angle=0, is_show=False,
                     is_save=False):
    # Batch production of seventeen types of symmetric images
    # img_num: Number of each type of image to produce

    info1 = [l, 1]  # Square
    info2 = [l, m, 2]  # Rectangle
    info3 = [l, m, deg, 3]  # Parallelogram
    info4 = [l, deg, 4]  # Rhombus
    info4_3 = [l, l, 60, 3]  # Parallelogram equivalent to rhombus
    info5 = [l, 5]  # Regular hexagon

    # Triangles
    y = int(l * np.cos(deg * np.pi / 180)) * 2
    info6_1_1 = [y, l, deg, 6]  # Isosceles triangle

    y = int(l * np.cos(30 * np.pi / 180)) * 2
    info6_1 = [y, l, 30, 6]  # 30-degree isosceles triangle

    info6_1_2 = [l, l, 90, 6]  # Right-angled isosceles triangle

    x = int(l * np.cos(deg * np.pi / 180))
    info6_2 = [x, l, deg, 6]  # Right triangle

    x = int(l * np.cos(45 * np.pi / 180)) * 2
    info6_2_1 = [x, l, 45, 6]  # 45-degree right triangle

    x = int(l * np.cos(60 * np.pi / 180))
    info6_2_2 = [x, l, 60, 6]  # Right 60 triangle

    info6_3 = [l, l, 60, 6]  # Equilateral triangle

    # Generate points
    point1 = Point(info=info1).run()
    point2 = Point(info=info2).run()
    point3 = Point(info=info3).run()
    point4 = Point(info=info4).run()
    point4_3 = Point(info=info4_3).run()
    point5 = Point(info=info5).run()
    point6_1_1 = Point(info=info6_1_1).run()
    point6_1 = Point(info=info6_1).run()
    point6_1_2 = Point(info=info6_1_2).run()
    point6_2 = Point(info=info6_2).run()
    point6_2_1 = Point(info=info6_2_1).run()
    point6_2_2 = Point(info=info6_2_2).run()
    point6_3 = Point(info=info6_3).run()

    # Image data
    files = os.listdir(source_folder)
    random.shuffle(files)
    for filename in ['basic-L.jpg']:
        source_image_path = os.path.join(source_folder, filename)
        kwargs = {'source_image_path': source_image_path, 'is_show': is_show, 'is_save': is_save,
                  'save_image_path': save_image_path, 'picture_width': width, 'picture_height': height, 'angle': angle}

        P1(**kwargs, point=point1, info=info1).generate()
        #P1(**kwargs, point=point2, info=info2).generate()
        #P1(**kwargs, point=point3, info=info3).generate()
        #P1(**kwargs, point=point4, info=info4).generate()
        #P1(**kwargs, point=point5, info=info5).generate()

        P2(**kwargs, point=point1, info=info1).generate()
        #P2(**kwargs, point=point3, info=info3).generate()
        #P2(**kwargs, point=point6_1_1, info=info6_1_1).generate()
        #P2Hexagonal(**kwargs, point=point6_3, info=info6_3).generate()

        Pm(**kwargs, point=point1, info=info1).generate()
        #Pm(**kwargs, point=point2, info=info2).generate()

        Pg(**kwargs, point=point2, info=info2).generate()

        Cm(**kwargs, point=point6_1, info=info6_1).generate()

        Pmm(**kwargs, point=point1, info=info1).generate()
        Pmm(**kwargs, point=point2, info=info2).generate()

        Pmg(**kwargs, point=point2, info=info2).generate()

        Pgg(**kwargs, point=point6_1_1, info=info6_1_1).generate()

        #Cmm(**kwargs, point=point6_2, info=info6_2, type='rhombic').generate()
        Cmm(**kwargs, point=point6_2_1, info=info6_2_1, type='square').generate()

        P4(**kwargs, point=point1, info=info1).generate()
        P4m(**kwargs, point=point6_1_2, info=info6_1_2).generate()
        P4g(**kwargs, point=point6_1_2, info=info6_1_2).generate()

        P3(**kwargs, point=point4_3, info=info4_3).generate()
        P3m1(**kwargs, point=point6_3, info=info6_3).generate()
        P31m(**kwargs, point=point6_1, info=info6_1).generate()

        P6(**kwargs, point=point6_3, info=info6_3).generate()
        P6m(**kwargs, point=point6_2_2, info=info6_2_2).generate()



if __name__ == '__main__':
    """
        source_folder: Original file directory
        save_folder: Save file directory
    """
    source_folder = './images'
    save_folder = './outputs'

    # sum: epoch * img_num
    epoch = 1
    img_num = 1

    for i in range(epoch):
        width, height = [1024, 1024]  # Canvas size

        l=160
        m=160
        deg = 40

        angle = 80

        print('Random values,  [l:{} m:{}], deg:{}, angle:{}, [w:{},h:{}]'.format(l, m, deg, angle, width, height))
        batch_production(l, m, deg, img_num, source_folder, save_folder, width=width, height=height, angle=angle,
                         is_show=False, is_save=True)
