import math


def circle_area(radius):
    if radius <= 0:
        return "error"
    return math.pi * (radius * radius)


def circle_perimeter(radius):
    if radius <= 0:
        return "error"
    return 2 * math.pi * (radius)


def rectangle_area(width, height):
    if width <= 0 or height <= 0:
        return "error"
    return width * height


def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return "error"
    return base * height / 2
