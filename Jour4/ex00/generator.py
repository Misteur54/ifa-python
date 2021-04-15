#!/usr/bin/env python3

import writer
import sys

from random import randint


class Generator:
    def __init__(self, minlength=1, maxlength=3, filelength=1500):
        self.minlength = minlength
        self.maxlength = maxlength
        self.filelength = filelength
        self._test = 100

    def generateLength(self, lengthmin, lengthmax):
        min = 10 ** (lengthmin - 1)
        max = (10 ** lengthmax) - 1

        return randint(min, max)

    def _createGenerator(self, minlength, maxlength, filelength):
        result = []

        for i in range(0, filelength, 1):
            result.append(self.generateLength(minlength, maxlength))
        return result

    def defaultGenerator(self):
        return self._createGenerator(self.minlength, self.maxlength, self.filelength)


def check_argv(argv):
    if len(argv) != 4:
        sys.exit("pas le bon nb d'argv")
    datas = argv[1:4]
    for pos, data in enumerate(datas):
        if not data.isdigit():
            sys.exit("uniquement des nbs")
        datas[pos] = int(data)
    return datas


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) == 1:
        gen = Generator()
        datas = gen.defaultGenerator()
        writer = writer.Writer()
        writer.writerStr('nb.txt', 'w', datas)
    else:
        params = check_argv(sys.argv)
        gen = Generator(params[0], params[1], params[2])
        datas = gen.defaultGenerator()
        writer = writer.Writer()
        writer.writerStr('nb.txt', 'w', datas)
