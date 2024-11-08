years = input("Enter employment years (> 0): ")
department = input("Enter department (10-99): ")

# input variable
years = int(years)
department = int(department)

# initialize values
bonus = 0.0
remainder = department % 10

# Calculate the bonus
if years <= 0 or department < 10 or department > 99:
    bonus = "Invalid input"
elif years > 3:
    if remainder >= 1 and remainder <= 5:
        bonus = 400 + 0.1*400
    elif remainder >= 6 and remainder <= 9:
        bonus = 400 + 0.2*400
    else:
        bonus = 400
elif years < 2:
    bonus  = 200
elif years >=2 and years <=3:
    bonus = 300

# check the bonus variable if it is a number or an invalid input
if isinstance(bonus, str):
    print(bonus)
else:
    print(f"Bonus for {years} years of employment in department {department}: {bonus:.2f}")
