r = float(input("Radius (in metres): "))
h = float(input("Height (in metres): "))
pi = 3.14159

circumference = 2*r*pi
area = ((pi*r**2)*2) + (h*circumference)
volume = (pi*r**2)*h
water = volume*0.9
paint = area*0.65
plates = int(area // 2) + bool(area % 2)

print(f"Surface area of the tank: {area:.2f}")
print(f"Volume of the tank: {volume:.2f}")
print(f"Amount of water needed: {water:.2f}")
print(f"Litres of paint needed: {paint:.2f}")
print(f"Number of plates needed: {plates}")
