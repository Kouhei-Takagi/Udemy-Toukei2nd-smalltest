b1Product = 1 / 6
b2Product = 2 / 6
b3Product = 3 / 6

b1Error = 7 / 100
b2Error = 5 / 100
b3Error = 9 / 100

b1RatioOfError = b1Product * b1Error / (b1Error * b1Product + b2Error * b2Product + b3Error * b3Product)
print(b1RatioOfError)