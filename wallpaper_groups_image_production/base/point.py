import numpy as np
from base.cell import Cell


class Point:
    '''
        kind=1: Square  info[w]: One parameter --> side length of the square
        kind=2: Rectangular   info[w,h]: Two parameters --> width and height of the rectangle
        kind=3: Parallelogram  info[w_1,w_2,theta]: Three parameters --> long side, short side, angle
        kind=4: Rhombus   info[w,theta]: Two parameters --> side length, angle
        kind=5: Hexagon   info[w]: One parameter --> side length
        kind=6: Triangle    info[w_1,w_2,theta]: Three parameters --> two sides and the included angle
    '''

    def __init__(self, info):
        self.kind = info[-1]
        self.info = info[0:-1]

    @staticmethod
    def square(info):
        # Square
        length = info[0]

        # Redefine canvas size as the side length of the square
        # rectangle_width = length
        # rectangle_height = length
        point_for_cut = np.array([[0, 0], [0, length], [length, length], [length, 0]])

        return point_for_cut

    @staticmethod
    def rectangular(info):
        # Rectangular
        w = info[0]
        h = info[1]

        point_for_cut = np.array(
            [[0, 0], [0, h], [w, h], [w, 0]])

        return point_for_cut

    @staticmethod
    def oblique(info):
        # Parallelogram

        # long_side: long side
        # short_side: short side
        # long_side, short_side, theta = info[0], info[1], info[2]
        long_side, short_side, theta = info[:]

        if theta >= 90 or theta <= 0:
            print(theta)
            raise ValueError("The angle theta should be between 90 and 0")

        rectangle_height = int(long_side * np.sin(theta * np.pi / 180))
        temp_w = int(long_side * np.cos(theta * np.pi / 180))

        rectangle_width = temp_w + short_side

        # print('point.py', short_side, long_side, rectangle_width, rectangle_height)
        point_for_cut = np.array(
            [[temp_w, 0], [0, rectangle_height], [short_side, rectangle_height],
             [temp_w + short_side, 0]])

        return point_for_cut

    @staticmethod
    def rhombic(info):
        # Rhombus

        # length, theta = info[0],info[1]
        length, theta = info[:]

        if theta >= 180 or theta <= 0:
            raise ValueError("The angle theta should be between 180 and 0")

        temp_theta = theta / 2

        temp_h = int(length * np.sin(temp_theta * np.pi / 180))
        temp_w = int(length * np.cos(temp_theta * np.pi / 180))

        rectangle_height = temp_h * 2
        rectangle_width = temp_w * 2
        point_for_cut = np.array([[temp_w, 0], [0, temp_h], [temp_w, rectangle_height], [rectangle_width, temp_h]])

        return point_for_cut

    @staticmethod
    def hexagon(info):
        # Hexagon

        length = info[0]

        temp_h = int(length * np.sin(np.pi / 3))
        # temp_w = int(length * np.cos(np.pi / 3))
        temp_w = int(length // 2)

        rectangle_height = temp_h * 2
        rectangle_width = temp_w * 2 + length

        # print(rectangle_width, rectangle_height)
        point_for_cut = np.array([[temp_w, 0], [0, temp_h], [temp_w, rectangle_height],
                                  [temp_w + length, temp_h * 2], [temp_w * 2 + length, temp_h],
                                  [temp_w + length, 0]])
        # print('point:', point_for_cut)
        return point_for_cut

    @staticmethod
    def triangle(info):
        # Triangle
        long_side, short_side, theta = info[:]
        if theta == 90:
            # Right angle
            rectangle_width = long_side
            rectangle_height = short_side
            point_for_cut = np.array([[0, 0], [0, rectangle_height], [rectangle_width, rectangle_height]])

        elif theta > 0 and theta < 90:
            # Acute angle
            rectangle_width = long_side
            rectangle_height = int(short_side * np.sin(theta * np.pi / 180))
            temp_w = int(short_side * np.cos(theta * np.pi / 180))
            # print(temp_w, rectangle_height, rectangle_width)
            point_for_cut = np.array([[temp_w, 0], [0, rectangle_height], [rectangle_width, rectangle_height]])

        elif theta > 90 and theta < 180:
            # Obtuse angle
            rectangle_height = int(short_side * np.sin((theta) * np.pi / 180))
            temp_w = int(short_side * np.cos((180 - theta) * np.pi / 180))
            rectangle_width = long_side + temp_w

            # print(temp_w, rectangle_height, rectangle_width)
            point_for_cut = np.array([[0, 0], [temp_w, rectangle_height], [rectangle_width, rectangle_height]])

        else:
            raise ValueError("The angle theta should be between 180 and 0")

        return point_for_cut

    def run(self):
        if self.kind == 1:
            # return None
            return self.square(self.info)
        elif self.kind == 2:
            # return None
            return self.rectangular(self.info)
        elif self.kind == 3:
            return self.oblique(self.info)
        elif self.kind == 4:
            return self.rhombic(self.info)
        elif self.kind == 5:
            return self.hexagon(self.info)
        elif self.kind == 6:
            return self.triangle(self.info)
        else:
            raise ValueError("Kind should be between 1 and 6")


# Test
if __name__ == '__main__':
    print('Start', np.cos(np.pi / 3))

    source_image_path = '../images/dataset/16.png'

    # info = [300, 200, 70, 3]
    # info = [50,50,120,6]

    x = 100
    theta = 30
    y = int(x * np.cos(theta * np.pi / 180)) * 2
    info = [x, y, theta, 6]
    print(info[-1], info[0:-1])
    # point, rectangle_width, rectangle_height  = Point().square(info=[100])  # Square
    # point, rectangle_width, rectangle_height = Point().rectangular(info=[100, 200])  # Rectangle
    point, rectangle_width, rectangle_height = Point(info=info).run()  # Parallelogram
    # point, rectangle_width, rectangle_height = Point().rhombic(info=[200, 60])  # Rhombus
    # point, rectangle_width, rectangle_height = Point().hexagon(info=[50])  # Hexagon
    # point, rectangle_width, rectangle_height = Point().triangle(info=[200, 100, 150])  # Triangle

    cell = Cell(rectangle_width=rectangle_width, rectangle_height=rectangle_height, point=point,
                source_image_path=source_image_path, kind=3, picture_width=600, picture_height=600)
    cell.paste_img((0, 0))
    cell.show()

    cell.over_spread(point[0])
