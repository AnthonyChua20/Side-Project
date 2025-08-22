GrossIncome = float(input("Enter your gross income: "))
monthlyGrossincome = GrossIncome / 12
cpf = monthlyGrossincome * 0.2
loanPayment = 1500
MonthlyIncome = monthlyGrossincome - cpf - loanPayment
print("Your monthly Income after CPF deduction is:", MonthlyIncome)

