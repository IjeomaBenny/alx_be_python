monthly_income = int(input("Enter your monthly income:"))

total_monthly_expenses = int(input("Enter your total monthly expenses:"))

simple_annual_interest = 0.05

monthly_savings = monthly_income - total_monthly_expenses

print("your monthly savings are: $",monthly_savings)

projected_savings = monthly_savings * 12 + monthly_savings * 12 * simple_annual_interest

print("Projected savings after one year, with interest, is: $", projected_savings)