from math import ceil, floor
from collections import Counter
def mean(numLS):
    """
    Finds the sum of a list of numbers and divided by the
    length of the list leaving the mean.
    """
    result = sum(numLS) / float(len(numLS))
    return result

def median(numLS):
    """
    The middle value of a set of ordered data.
    """
    def medFormula(numLS):
        result = (len(numLS) + 1) / 2 - 1
        return result

    numLS.sort()

    if (len(numLS) % 2) == 0:
        belMed = numLS[int(floor(medFormula(numLS)))]
        aboMed = numLS[int(ceil(medFormula(numLS)))]
        return (belMed + aboMed) / 2
    else:
        return numLS[int(medFormula(numLS))]

def mode(numLS):
    """
    Finds the most occurring number
    """
    moCom = Counter(numLS).most_common(1)
    mode = moCom[0]
    return mode[0]

def range(numLS):
    numLS.sort()
    return numLS[len(numLS) - 1] - numLS[0]
numlist = [34, 34, 132, 45, 576, -67, 67, 67, 67, 67]
print(range(numlist))
