# Ask for hours worked
hours_worked = float(input("Enter the hours worked: "))

# Repeat until a valid number of hours is entered
while hours_worked < 0:
    print("Hours worked cannot be negative. Please try again.")
    hours_worked = float(input("Enter the hours worked: "))

print(f"Hours worked: {hours_worked}")