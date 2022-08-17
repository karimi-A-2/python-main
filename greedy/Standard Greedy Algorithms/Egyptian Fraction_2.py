import math


def getEgyptianFraction(numerator, denominator):
    str = ""
    output = getEgyptianFractionUtil(numerator, denominator, [])
    for denom in output:
        str += "1/{0} + ".format(denom)
    strCopy = str[:-3]  # removing the last + sign
    return strCopy


def getEgyptianFractionUtil(numerator, denominator, listOfDenoms):
    if numerator == 0:
        return listOfDenoms
    newDenom = math.ceil(denominator / numerator)
    # append in output list
    listOfDenoms.append(newDenom)
    listOfDenoms = getEgyptianFractionUtil(numerator * newDenom - denominator,
                                           newDenom * denominator, listOfDenoms)
    return listOfDenoms


print(getEgyptianFraction(6, 14))
# Code contributed by
# Mayur Sonowal
