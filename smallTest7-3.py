import math

rxy = 0.8051
rxz = 0.7930
ryz = 0.9883

prxyz = (rxy - rxz * ryz) / (math.sqrt(1 - rxz ** 2) * math.sqrt(1 - ryz ** 2))

print(prxyz)