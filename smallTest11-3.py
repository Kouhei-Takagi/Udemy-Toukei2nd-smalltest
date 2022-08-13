import math

populationA = (13458, 13433, 13390, 13385, 13359, 13324)
populationB = (159824, 159857, 159855, 159730, 158988, 158232)

def populationChangeRate(y2, y5):
    return y5 / y2

a = populationChangeRate(populationA[2], populationA[5])
b = populationChangeRate(populationB[2], populationB[5])

print(a)
print(b)