def maximum(data):
    """
    Finds the maximum value in a list.
    Returns: {'result': maximum value, 'index': [index of maximum value]}

    If a value is a list, only the last value of the list is
    considered. If a value appears multiple times, all of its indexes
    are returned in the list of indexes.
    """
    max_val = float('-inf')
    index = []

    for i in range(len(data)):
        value = data[i]
        while isinstance(value, list):
            value = value[-1]
        if value == max_val:
            index.append(i)
        elif value > max_val:
            max_val = value
            index = [i]

    return {'result': max_val, 'index': index}

def minimum(data):
    """
    Finds the minimum value in a list.
    Returns: {'result': minimum value, 'index': [index of minimum value]}

    If a value is a list, only the last value of the list is
    considered. If a value appears multiple times, all of its indexes
    are returned in the list of indexes.
    """
    min_val = float('inf')
    index = []

    for i in range(len(data)):
        value = data[i]
        if isinstance(value, list):
            value = maximum(data[i])['result']
        if value == min_val:
            index.append(i)
        elif value < min_val:
            min_val = value
            index = [i]

    return {'result': min_val, 'index': index}

def long(data):
    """
    Finds the longest list or string in a list.

    Returns: {'result': length of list or string, 'index': [index]}

    Non-list and Non-string values are given a length of 1. If multiple
    values share the longest length, all values' indexes are included in the
    list of indexes.
    """
    longest = 0
    index = []

    for i in range(len(data)):
        if not isinstance(data[i], list) and not isinstance(data[i], str):
            length = 1
        else:
            length = len(data[i])
        if length == longest:
            index.append(i)
        if length > longest:
            longest = length
            index = [i]

    return {'result': longest, 'index': index}

def short(data):
    """
    Finds the shortest list or string in a list.

    Returns: {'result': length of list or string, 'index': [index]}

    Non-list and Non-string values are given a length of 1. If multiple
    values share the shortest length, all values' indexes are included in the
    list of indexes.
    """
    shortest = float('inf')
    index = []

    for i in range(len(data)):
        if not isinstance(data[i], list) and not isinstance(data[i], str):
            length = 1
        else:
            length = len(data[i])
        if length == shortest:
            index.append(i)
        if length > shortest:
            shortest = length
            index = [i]

    return {'result': shortest, 'index': index}

def threshold(data, threshold):
    """
    Finds the number of values in a list that meet or exceed
    a given threshold.

    Returns: {'count': number of values => threshold, 'percent': percent of values => threshold}

    If a value is a list, only the last value in the list is considered.
    The percent is rounded to 2 decimal points.
    """
    count = 0

    for i in range(len(data)):
        value = data[i]
        while isinstance(value, list):
            value = value[-1]
        if isinstance(value, str):
            value = len(value)
        if value >= threshold:
            count += 1

    percent = round((count / len(data) * 100), 2)
    return {'result': count, 'percent': percent}