from base.seventeen_wallpaper_line import *


def draw_line(l, m, deg, source_image_path, save_image_path, is_show):

    # Generate the image with identifiers
    info1 = [l, 1]  # Square
    point1 = Point(info=info1).run()

    info2 = [l, m, 2]  # Rectangle
    point2 = Point(info=info2).run()

    info3 = [l, m, deg, 3]  # Parallelogram
    point3 = Point(info=info3).run()

    info4 = [l, 60, 4]  # Rhombus
    point4 = Point(info=info4).run()

    info4_3 = [l, l, 60, 3]  # Parallelogram mimicking rhombus
    point4_3 = Point(info=info4_3).run()

    info5 = [l, 5]  # Hexagon
    point5 = Point(info=info5).run()

    y = int(l * np.cos(30 * np.pi / 180)) * 2
    info6_1 = [y, l, 30, 6]  # Isosceles triangle with 30 degrees angle
    point6_1 = Point(info=info6_1).run()

    info6_1_2 = [l, l, 90, 6]  # Right isosceles triangle
    point6_1_2 = Point(info=info6_1_2).run()

    x = int(l * np.cos(deg * np.pi / 180))
    info6_2 = [x, l, deg, 6]  # Right triangle
    point6_2 = Point(info=info6_2).run()

    x = int(l * np.cos(45 * np.pi / 180)) * 2
    info6_2_1 = [x, l, 45, 6]  # 45-degree isosceles right triangle
    point6_2_1 = Point(info=info6_2_1).run()

    x = int(l * np.cos(60 * np.pi / 180))
    info6_2_2 = [x, l, 60, 6]  # Right 60 triangle
    point6_2_2 = Point(info=info6_2_2).run()

    info6_3 = [l, l, 60, 6]  # Equilateral triangle
    point6_3 = Point(info=info6_3).run()
    print(point6_2_2)


    kwargs = {'source_image_path': source_image_path, 'save_image_path': save_image_path, 'is_show': is_show,
              'picture_width': width, 'picture_height': height}

    groups = {
            'P1_1':'P1(point=point1, info=info1, **kwargs).generate()',
            'P1-2':'P1(point=point2, info=info2, **kwargs).generate()',
            'P1-3':'P1(point=point3, info=info3, **kwargs).generate()',
            'P1-4':'P1(point=point4, info=info4, **kwargs).generate()',
            'P1-5':'P1(point=point5, info=info5, **kwargs).generate()',
            'P2-1':'P2(point=point2, info=info2, **kwargs).generate()',
            'P2-2':'P2(point=point3, info=info3, **kwargs).generate()',
            'P2-3':'P2(point=point6_1, info=info6_1, **kwargs).generate()',
            'P2Hexagonal':'P2Hexagonal(point=point6_3, info=info6_3, **kwargs).generate()',
            'Pm-1':'Pm(point=point1, info=info1, **kwargs).generate()',
            'Pm-2':'Pm(point=point2, info=info2, **kwargs).generate()',
            'Pg':'Pg(point=point2, info=info2, **kwargs).generate()',
            'Cm':'Cm(point=point6_1, info=info6_1, **kwargs).generate()',
            'Pmm-1':'Pmm(point=point1, info=info1, **kwargs).generate()',
            'Pmm-2':'Pmm(point=point2, info=info2, **kwargs).generate()',
            'Pmg':'Pmg(point=point2, info=info2, **kwargs).generate()',
            'Pgg':'Pgg(point=point6_1, info=info6_1, **kwargs).generate()',
            'Cmm-1':'Cmm(point=point6_2, info=info6_2, type="rhombic", **kwargs).generate()',
            'Cmm-2':'Cmm(point=point6_2_1, info=info6_2_1, type="square", **kwargs).generate()',
            'P4':'P4(point=point1, info=info1, **kwargs).generate()',
            'P4m':'P4m(point=point6_1_2, info=info6_1_2, **kwargs).generate()',
            'P4g':'P4g(point=point6_1_2, info=info6_1_2, **kwargs).generate()',
            'P3':'P3(point=point4_3, info=info4_3, **kwargs).generate()',
            'P3m1':'P3m1(point=point6_3, info=info6_3, **kwargs).generate()',
            'P31m':'P31m(point=point6_1, info=info6_1, **kwargs).generate()',
            'P6':'P6(point=point6_3, info=info6_3, **kwargs).generate()',
            'P6m':'P6m(point=point6_2_2, info=info6_2_2, **kwargs).generate()'
    }

    #for k, v in groups.items():
    for v in groups['P6m']:
        eval(v)
        eval(v.replace("(point=","Line(point="))





if __name__ == '__main__':
    """
        source_image_path: original image
        save_folder: save directory
    """
    source_image_path = './images/basic-L.jpg'
    save_folder = './outputs'

    # Final canvas size
    width, height = 1024, 1024

    # Parameters for the line: (l, m, deg)
    l = 160
    m = 160
    deg = 40

    # is_show: Whether to display while running
    draw_line(l, m, deg, source_image_path, save_folder, is_show=False)
