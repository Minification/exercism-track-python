def flatten(iterable):
    accumulator = []
    for i in iterable:
        if type(i) is list:
            accumulator.extend(flatten(i))
        else:
            if i == None:
                continue
            accumulator.append(i)
    return accumulator
