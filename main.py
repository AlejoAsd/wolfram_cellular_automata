from generator import Generator
from random import randint

from image import Image


def random_line(size):
    return [randint(0, 1) for i in range(size)]


def compile_rule(str_rule):
    return int(str_rule, 2)


if __name__ == '__main__':
    width = 6
    height = 5

    gen = Generator(3, compile_rule('01010101'))
    values = gen.generate([1, 0, 0, 0, 1, 1], height)

    image = Image(6, height)
    values = image.process_values(values)
    image.save('./test.png')