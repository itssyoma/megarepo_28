#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def multiply():
    product = 1
    while True:
        num = float(input("Введите число (введите 0 для завершения): "))
        if num == 0:
            print("Итоговое произведение: ", product)
            break
        product *= num
        print("Промежуточное произведение: ", product)


if __name__ == "__main__":
    multiply()
