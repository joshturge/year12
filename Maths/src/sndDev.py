from mmmr import mean
from math import sqrt

def sndDev(numls):
    """
    The Standard Deviation is a measure of how spread out numbers are.
    """
    sqrdifls = []
    # Gets the total mean from the list of numbers.
    totalMean = mean(numls)
    for number in numls:
        # Every number in the list of numbers is taken away
        # from the total mean, then the answer is squared.
        sqrdif = (number - totalMean)**2
        # 'squared differences' are added to a list
        sqrdifls.append(sqrdif)
    # Gets the mean from the 'squared differences list' and
    # stores it in a variable
    sqrdiflsMean = mean(sqrdifls)
    # The 'squared differences list' mean is then squarerooted
    # which leaves the standard deviation. 
    result = sqrt(sqrdiflsMean)
    return result 
