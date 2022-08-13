import math

populationA = (13458, 13433, 13390, 13385, 13359, 13324)
populationB = (159824, 159857, 159855, 159730, 158988, 158232)

def populationChangeRate(y0, yt, t):
    return math.pow(yt / y0, 1 / t)

a = populationChangeRate(populationA[0], populationA[5], 5)
b = populationChangeRate(populationB[0], populationB[5], 5)

print(a)
print(b)