# Get the diamond size from the user
size = int(input("Diamond size: "))

# Check if the input size is less than 2
# If size is less than 2, print "Invalid size" and stop the program
if size < 2:
    print("Invalid size")
else:
    # Ensure the size is an odd number
    # If the user enters an even number, increment it by one to make it odd
    if size % 2 == 0:
        size += 1

    # Determine the midpoint of the diamond (the widest row in the center)
    # This helps us build the top and bottom halves of the diamond separately
    midpoint = size // 2

    # Build the top half of the diamond (including the center row)
    # We loop from 0 to midpoint, creating each row one by one
    for i in range(midpoint + 1):
        # Calculate the number of leading spaces needed for alignment
        # As we go down each row in the top half, the spaces decrease
        spaces = ' ' * (midpoint - i)

        # Special case for the topmost row (i == 0)
        # Only print one '*' at the top point of the diamond
        if i == 0:
            print(spaces + '*')
        else:
            # For all other rows, we need to print a '*' at the start and end
            # The middle part is filled with spaces to create the hollow effect
            # The number of middle spaces is (2 * i - 1)
            print(spaces + '*' + ' ' * (2 * i - 1) + '*')

    # Build the bottom half of the diamond (excluding the center row)
    # We loop from midpoint - 1 down to 0 to reverse the rows for the bottom half
    for i in range(midpoint - 1, -1, -1):
        # Calculate the number of leading spaces for alignment
        # This time, spaces increase as we move down each row in the bottom half
        spaces = ' ' * (midpoint - i)

        # Special case for the bottommost row (i == 0)
        # Only print one '*' at the bottom point of the diamond
        if i == 0:
            print(spaces + '*')
        else:
            # For all other rows in the bottom half, we print a '*' at the start and end
            # The middle part is filled with spaces to create the hollow effect
            # The number of middle spaces is (2 * i - 1)
            print(spaces + '*' + ' ' * (2 * i - 1) + '*')
