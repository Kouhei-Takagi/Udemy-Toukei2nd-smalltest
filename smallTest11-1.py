populationA = (13458, 13433, 13390, 13385, 13359, 13324)
populationB = (159824, 159857, 159855, 159730, 158988, 158232)

def populationChange4to5(x, y):
    return y / x

a = 100 * populationChange4to5(populationA[4], populationA[5])
b = 100 * populationChange4to5(populationB[4], populationB[5])

print(a - 100)
print(b - 100)