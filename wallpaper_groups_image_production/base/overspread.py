import abc
import numpy as np
import math

class FullBase(abc.ABC):
    '''
    Used to assemble small graphics into a large graphic.
    Approach: Just calculate the set of points where the five basic types of rectangles are placed 
    on the final generated graphic's top-left corner.
    '''

    def __init__(self, picture_width, picture_height, rectangle_width, rectangle_height):
        self.picture_width = picture_width
        self.picture_height = picture_height
        self.rectangle_width = rectangle_width
        self.rectangle_height = rectangle_height
        self.paste_points = []

    @abc.abstractmethod
    def get_paste_points(self):
        pass

class RectangleFull(FullBase):
    '''
    Used to assemble small graphics into a large graphic where the small canvas is a rectangle/square.

    picture_width, picture_height: The size of the final generated graphic.
    rectangle_width, rectangle_height: The size of the rectangles storing the five basic types.
    '''

    def __init__(self, picture_width, picture_height, rectangle_width, rectangle_height):
        super(RectangleFull, self).__init__(picture_width, picture_height, rectangle_width, rectangle_height)

    def get_paste_points(self):
        i = 0
        while i < self.picture_height:
            j = 0
            while j < self.picture_width:
                self.paste_points.append((j, i))
                j += self.rectangle_width
            i += self.rectangle_height
        return self.paste_points

class ObliqueFull(FullBase):
    '''
    Used to assemble small graphics into a large graphic where the small canvas is a parallelogram.

    picture_width, picture_height: The size of the final generated graphic.
    rectangle_width, rectangle_height: The size of the rectangles storing the five basic types.
    oblique_left: The x-coordinate of the top-left vertex of the parallelogram.
    oblique_width: The length of the side of the parallelogram that overlaps with the canvas edge.
    '''

    def __init__(self, picture_width, picture_height, rectangle_width, rectangle_height, oblique_leftop_point):
        super(ObliqueFull, self).__init__(picture_width, picture_height, rectangle_width, rectangle_height)
        self.oblique_left = oblique_leftop_point[0]
        self.oblique_width = self.rectangle_width - self.oblique_left

    def get_paste_points(self):
        i = -self.rectangle_height
        temp_y = 0
        while i < self.picture_height:
            j = temp_y
            while j < self.picture_width:
                self.paste_points.append((j, i))
                j += self.oblique_width
            i += self.rectangle_height
            temp_y += -self.oblique_left
        return self.paste_points

    def get_letfdown_theta(self, is_radian=True):
        '''
        Get the angle of the bottom-left corner of the parallelogram.
        '''
        res = math.atan(self.rectangle_height / self.oblique_left)
        if is_radian:
            return res
        else:
            return res * 180 / math.pi

class RhombicFull(FullBase):
    '''
    Used to assemble small graphics into a large graphic where the small canvas is a rhombus.

    picture_width, picture_height: The size of the final generated graphic.
    rectangle_width, rectangle_height: The size of the rectangles storing the five basic types.

    The top vertex of the rhombus is always at the midpoint of rectangle_width.
    The left vertex of the rhombus is always at the midpoint of rectangle_height.
    '''

    def __init__(self, picture_width, picture_height, rectangle_width, rectangle_height):
        super(RhombicFull, self).__init__(picture_width, picture_height, rectangle_width, rectangle_height)

    def get_paste_points(self):
        a = self.rectangle_width // 2
        b = self.rectangle_height // 2
        i = -self.rectangle_height
        while i < self.picture_height:
            j = -self.rectangle_width
            while j < self.picture_width:
                self.paste_points.append((j, i))
                self.paste_points.append((j + a, i + b))
                j += self.rectangle_width
            i += self.rectangle_height
        return self.paste_points

    def get_left_theta(self, is_radian=True):
        '''
        Get the size of the rhombus's left top angle.
        '''
        res = 2 * math.atan((self.rectangle_width / 2) / (self.rectangle_height / 2))
        if is_radian:
            return res
        else:
            return res * 180 / math.pi

class HexagonalFull(FullBase):
    '''
    Used to assemble small graphics into a large graphic where the small canvas is a hexagon.
    '''

    def __init__(self, picture_width, picture_height, rectangle_width, rectangle_height, length):
        super(HexagonalFull, self).__init__(picture_width, picture_height, rectangle_width, rectangle_height)
        temp_h = int(length * np.sin(np.pi / 3))
        temp_w = length // 2
        self.rightdown_shift_right = temp_w + length
        self.rightdown_shift_down = temp_h
        self.right_shift = temp_w * 2 + length + length

    def get_paste_points(self):
        i = -self.rectangle_height
        while i < self.picture_height:
            j = -self.rectangle_width
            while j < self.picture_width:
                self.paste_points.append((j, i))
                self.paste_points.append((j + self.rightdown_shift_right, i + self.rightdown_shift_down))
                j += self.right_shift
            i += self.rectangle_height
        return self.paste_points
