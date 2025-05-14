gross_salary = float(input("Enter the employee's gross salary: "))

# Apply tax based on salary
if gross_salary < 2000:
    tax = 0
elif 2000 <= gross_salary <= 5000:
    tax = gross_salary * 0.10
else:
    tax = gross_salary * 0.20

# Display the calculated tax
print(f"The tax for a salary of ${gross_salary:.2f} is ${tax:.2f}.")
