import math

rxy = 0.6794
rxz = 0.8207
ryz = 0.9305

prxyz = (rxy - rxz * ryz) / (math.sqrt(1 - rxz ** 2) * math.sqrt(1 - ryz ** 2))

print(prxyz)