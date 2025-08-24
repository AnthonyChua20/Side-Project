age= int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()
if day == "saturday" or day == "sunday":
    day = "2"
ticketPrice = float()
if age < 4 or age >= 130:
    print("Invalid age")
else:
    match age:
        case age if age < 16:
            ticketPrice = 7.50
        case age if age >= 16 and age < 65:
            ticketPrice = 10.00
        case age if age >= 65:
            ticketprice = 5.50
            ticketPrice = f"{ticketPrice:.2f}"  
    if day == "2":
        ticketPrice = 10.00
        ticketPrice = f"{ticketPrice:.2f}"
    print("You have to pay $", ticketPrice, "for the ticket.")

