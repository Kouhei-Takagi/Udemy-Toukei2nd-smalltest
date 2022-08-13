sample = (58, 66, 69, 71, 75, 77, 78, 80, 80, 83, 84, 86, 87, 87, 88, 90, 91, 93, 93, 94, 94, 96, 97)

standardRange = max(sample) - min(sample)
print(standardRange)

first4BuniNum = round(len(sample) / 4)
first4Buni = sample[first4BuniNum - 1]
print(first4Buni)

third4BuniNum = round(len(sample) / 4)
third4Buni = sample[len(sample) - third4BuniNum]
print(third4Buni)

fourBuniRange = third4Buni - first4Buni
print(fourBuniRange)