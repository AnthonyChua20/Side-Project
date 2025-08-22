gst = 1.09   # 9% GST
serviceCharge = 1.10  # 10% service charge

def apply_charges(amount, has_service_charge):
    """Apply GST and optionally service charge to an amount."""
    if has_service_charge == "yes":
        return amount * gst * serviceCharge
    elif has_service_charge == "no":
        return amount * gst
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit()

people = int(input("How many people to split the bill? "))
if people <= 0:
    print("Number of people cannot be zero or negative.")
    exit()

bill = float(input("What is the total bill amount? $"))
equal_split = input("Do you want to split the bill equally? (yes/no) ").lower()

if equal_split == "yes":
    eachPay = bill / people
    print(f"Each person should pay: ${eachPay:.2f}")
else:
    has_service_charge = input("Does the entered amount have service charge included? (yes/no) ").lower()
    paid = []
    for i in range(people - 1):
        person_amount = float(input(f"Enter the amount for person {i+1}: $"))
        person_amount = apply_charges(person_amount, has_service_charge)
        paid.append(person_amount)

    # last person pays the remainder
    last_person = bill - sum(paid)
    paid.append(last_person)

    for i, amount in enumerate(paid, start=1):
        print(f"Person {i} should pay: ${amount:.2f}")
