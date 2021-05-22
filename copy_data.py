import numpy


def normalize(array: numpy.ndarray):
    low = array.min()
    high = array.max()
    array -= low
    array /= high

    return array
