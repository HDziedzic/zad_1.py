txt = "My name is {name}, I'm {name}"
b = 3.74
c = hex(0X0F)

print(txt.format(name="Hubert"))
print("For only {price:.2f}".format(price=b*b))
print("{hex1} + 75 =".format(hex1=c), c + hex(75))
