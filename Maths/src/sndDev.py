from mmmr import mean
from math import sqrt

def sndDev(numLS):
    """
    The Standard Deviation is a measure of how spread out numbers are.
    """
    sqrdifls = []
    totalMean = mean(numLS)

    for number in numLS:
        sqrdif = (number - totalMean)**2
        sqrdifls.append(sqrdif)
    return sqrt(mean(sqrdifls))
