import math

print("math.pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("2 to the power 5:", math.pow(2, 5))
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"sin({angle_deg}°):", math.sin(angle_rad))
print("Factorial of 5:", math.factorial(5))


import os

print("Current working directory:", os.getcwd())
print("List of files:", os.listdir())

test_dir = "my_test_dir"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"Created folder {test_dir}")

if os.path.exists(test_dir):
    os.rmdir(test_dir)
    print(f"Removed folder {test_dir}")