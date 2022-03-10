# zadanie 4

import numpy
import math

# oblicz e^10

print("oblicz e^10")
from math import e
print(pow(e, 10))

# Oblicz pierwiastek stopnia 6 z ln(5+sin^28)

print("Oblicz pierwiastek stopnia 6 z ln(5+sin^28)")
y = (5+pow(math.sin(8), 2))
x = numpy.log(y)
result = math.pow(x, 1.0/6)
print(result)

# zaokrąglenia
print("zaokrąglanie: ")
print(numpy.floor(3.55))
print(numpy.ceil(3.55))