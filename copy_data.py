import numpy

# memory: 3a


def normalize(array: numpy.ndarray):
    low = array.min()
    high = array.max()

    return (array - low) / (high - low)
    # memory: (a) -> original array, (a) -> array - low, (a) -> return array


# memory: a: in-place replacement


def normalize(array: numpy.ndarray):
    low = array.min()
    high = array.max()
    array -= low
    array /= high

    return array
    # memory: (a) -> original array


# memory: 2a: hidden mutation


def normalize3(array: numpy.ndarray):
    low = array.min()
    high = array.max()
    result = array.copy()
    result -= low
    result /= high - low

    return result
    # memory: (a) -> original array (a) -> result array
