monthly_income = int(input("How much is your monthly income?"))

total_monthly_expenses = int(input("How much is your total monthly expenses?"))

simple_annual_interest = 0.05

monthly_savings = monthly_income - total_monthly_expenses

print(monthly_savings)

projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05

print("Projected savings after one year, with interest, is:", projected_savings)