n_chairs = int(input("Input the number of ordered chairs: "))
n_tables = int(input("Input the number of ordered tables: "))
n_lamps = int(input("Input the number of ordered lamps: "))

cost_chair = 49.99
cost_table = 199.99
cost_lamp = 29.99

total_chairs_cost = n_chairs * cost_chair
total_tables_cost = n_tables * cost_table
total_lamps_cost = n_lamps * cost_lamp
total_cost = total_chairs_cost + total_tables_cost + total_lamps_cost

print("\nOrder Form:")
print("-"*33)
print(f"Chairs: {n_chairs:3d} x {cost_chair:6.2f} = {total_chairs_cost:10.2f}")
print(f"Tables: {n_tables:3d} x {cost_table:6.2f} = {total_tables_cost:10.2f}")
print(f"Lamps: {n_lamps:4d} x {cost_lamp:6.2f} = {total_lamps_cost:10.2f}")
print("-"*33)
print(f"Total: {total_cost:26.2f}")
print("="*33)
