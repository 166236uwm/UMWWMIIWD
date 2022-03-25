def addToTuple(t, value):
    l = list(t)
    l.append(value)
    x = tuple(l)
    return x


def addToTupleOtherWay(t, value):
    tup = (value,)
    t += tup
    return t


def removeFromTuple(t, value):
    l = list(t)
    l.remove(value)
    return tuple(l)

def withoutRepetition(l):
    return list(set(l))


def withoutRepetition2(l):
    return list(dict.fromkeys(l))
