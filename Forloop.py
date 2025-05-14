# List of employee salaries
salaries = [2500, 1800, 6000, 3200]

# Loop through each salary
for salary in salaries:
    # Apply a 10% tax
    tax = salary * 0.10
    net_salary = salary - tax

    # Display the net salary for each employee
    print(f"Gross Salary: ${salary:.2f}, Net Salary: ${net_salary:.2f}")
