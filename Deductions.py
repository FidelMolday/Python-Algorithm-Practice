# Ask for employee details
hourly_wage = float(input("Enter the employee's hourly wage: "))
hours_worked = float(input("Enter the total hours worked in the week: "))

# Calculate regular and overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate total pay
regular_pay = regular_hours * hourly_wage
overtime_pay = overtime_hours * hourly_wage * 1.5
gross_salary = regular_pay + overtime_pay

# Deduct 10% tax
tax = gross_salary * 0.10
net_salary = gross_salary - tax

# Display the results
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Gross Salary: ${gross_salary:.2f}")
print(f"Tax Deduction: ${tax:.2f}")
print(f"Net Salary: ${net_salary:.2f}")
