#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def get_input():
    return input("Введите значение: ")


def test_input(value):
    if value.isdigit():
        return True
    else:
        return False


def str_to_int(value):
    return int(value)


def print_int(value):
    print(value)


if __name__ == "__main__":
    input_value = get_input()
    if test_input(input_value):
        int_value = str_to_int(input_value)
        print_int(int_value)
    else:
        print("Введенное значение нельзя преобразовать в целое число.", file=sys.stderr)
        exit(1)
