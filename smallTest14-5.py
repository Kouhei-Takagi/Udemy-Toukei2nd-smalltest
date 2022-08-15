c1Product = 1 / 10
c2Product = 2 / 10
c3Product = 7 / 10

c1Error = 4 / 100
c2Error = 3 / 100
c3Error = 1 / 100

c3RatioOfError = c3Product * c3Error / (c1Error * c1Product + c2Error * c2Product + c3Error * c3Product)
print(c3RatioOfError)