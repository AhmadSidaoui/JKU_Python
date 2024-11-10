Value = 1
output = 1
counter = 0

while Value > 0:
    Value = input("Enter a value (or 'x' to stop): ")
    if Value == "x" and counter != 0:
        output = f"Result: {output}"
        break
    elif Value == "x" and counter == 0:
        output = f"Empty sequence"
        break
    else:
        Value = int(Value)
        output *= Value
        if output > 1000:
            output = f"Result has exceeded the value 1000: {output}"
            break
    counter += 1

print(output)

