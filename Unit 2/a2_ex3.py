start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

output_even = 0
output_odd = 0

the_range = range(start, stop + 1, step)

for index, value in enumerate(the_range):
    if (len(the_range) > 5 and len(the_range) <= 10) or (index <= 4) or (index >= 96):
        print(f"Index: {index}, Value: {value}")
    if value % 2 == 0:
        output_even += value
    else:
        output_odd = output_odd + (value * index) 


print(f"Sum of even values: {output_even}")
print(f"Sum of odd multiplied values: {output_odd}")