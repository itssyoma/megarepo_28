#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math, sys


def circle(radius):
    return math.pi * radius**2


def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    if radius <= 0 or height <= 0:
        print('Значения должны быть положительными', file=sys.stderr)
        exit(1)

    side_area = 2 * math.pi * radius * height
    full_area = side_area + 2 * circle(radius)
    
    choice = input("Площадь боковой поверхности (введите 'боковая') или полная площадь цилиндра (введите 'полная')? ")
    if choice == 'боковая':
        print("Площадь боковой поверхности цилиндра:", side_area)
    elif choice == 'полная':
        print("Полная площадь цилиндра:", full_area)
    else:
        print("Некорректный выбор", file=sys.stderr)
        exit(1)


if __name__ == "__main__": 
    cylinder()
