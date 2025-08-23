Shares = int(2000)
SharePrice = float(0.40)
CommisionRate = float(0.03)

CommisionPayment = CommisionRate * Shares * SharePrice
print("The commission payment is: $", round(CommisionPayment, 2))
newSharePrice = float(input("Enter the new share price: "))
TotalCommision = CommisionRate * Shares * SharePrice + (newSharePrice * Shares * 0.02)
print("The total commission is: $", round(TotalCommision, 2))
ProfitOrLoss = Shares * (newSharePrice - SharePrice) - TotalCommision
if ProfitOrLoss > 0:
    print("You made a profit of: $", round(ProfitOrLoss, 2))
elif ProfitOrLoss < 0:
    print("You made a loss of: $", round(ProfitOrLoss, 2))
