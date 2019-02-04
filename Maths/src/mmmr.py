from math import ceil, floor

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


numbers = [26.1, 25.0, 25.2, 25.6, 25.7]

print(median(numbers))
