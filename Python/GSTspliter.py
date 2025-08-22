gst = float(109/100)
serviceCharge = float(110/100)
people = int(input("How many people to split the bill? "))
bill = float(input("What is the total bill amount? $"))
if people == 0:
    print("Number of people cannot be zero.")
else:
    eachPay = bill / people
    match people:
        case 2:
            cost = input("Do you want to split the bill equally? (yes/no) ").lower()
            if cost == "yes":
                print("Each person should pay: ${:.2f}".format(eachPay))
            elif cost == "no":
                serviceChargetrue = input("Does this amount have service charge included? (yes/no) ").lower()
                person1 = float(input("Enter the amount for person 1: $"))
                
                if serviceChargetrue == "yes":
                    person1 = person1 * gst * serviceCharge
                elif serviceChargetrue == "no":
                    person1 = person1 * gst
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    exit()
                person2 = bill - person1
                print("Person 1 should pay: ${:.2f}".format(person1))
                print("Person 2 should pay: ${:.2f}".format(person2))
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        case 3:
            cost = input("Do you want to split the bill equally? (yes/no) ").lower()
            if cost == "yes":
                print("Each person should pay: ${:.2f}".format(eachPay))
            elif cost == "no":
                serviceChargetrue = input("Does this amount have service charge included? (yes/no) ").lower()
                person1 = float(input("Enter the amount for person 1: $"))
                
                if serviceChargetrue == "yes":
                    person1 = person1 * gst * serviceCharge
                elif serviceChargetrue == "no":
                    person1 = person1 * gst
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    exit()
                person2 = float(input("Enter the amount for person 2: $"))
                if serviceChargetrue == "yes":
                    person2 = person2 * gst * serviceCharge
                elif serviceChargetrue == "no":
                    person2 = person2 * gst
                person3 = bill - person1 - person2
                print("Person 1 should pay: ${:.2f}".format(person1))
                print("Person 2 should pay: ${:.2f}".format(person2))
                print("Person 3 should pay: ${:.2f}".format(person3))
            else:
                exit()
                print("Invalid input. Please enter 'yes' or 'no'.")
        case 4:
                    cost = input("Do you want to split the bill equally? (yes/no)").lower()
                    if cost == "yes":
                        print("Each person should pay: ${:.2f}".format(eachPay))
                        exit()
                    elif cost == "no":
                        serviceChargetrue = input("Does the total amount have service charge included? (yes/no) ").lower()  
                        person1 = float(input("Enter the amount for person 1: $"))
                    
                    if serviceChargetrue == "yes":
                        person1 = person1 * gst * serviceCharge
                    elif serviceChargetrue == "no":
                        person1 = person1 * gst
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        exit()
                    person2 = float(input("Enter the amount for person 2: $"))
                    if serviceChargetrue == "yes":
                        person2 = person2 * gst * serviceCharge
                    elif serviceChargetrue == "no":
                        person2 = person2 * gst
                    person3 = bill - person1 - person2
                    person3 = float(input("Enter the amount for person 3: $"))
                    if serviceChargetrue == "yes":
                        person3 = person3 * gst * serviceCharge
                    elif serviceChargetrue == "no":
                        person3 = person3 * gst
                    person4 = bill - person1 - person2 - person3
                    print("Person 1 should pay: ${:.2f}".format(person1))
                    print("Person 2 should pay: ${:.2f}".format(person2))
                    print("Person 3 should pay: ${:.2f}".format(person3))
                    print("Person 4 should pay: ${:.2f}".format(person4))    
                        #29.15 * 3 = 87.45
                        #87.45 + 35.55 = 123.00
                    
                
                
                
               