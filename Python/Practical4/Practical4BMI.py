weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))/100
BMI = weight/(height**2)
classification = str()
match BMI:
    case BMI if BMI < 18.5:
        classification= "Underweight"
    case BMI if BMI >= 18.5 and BMI <23.0:
        classification = "Normal"
    case BMI if BMI >= 23.0 and BMI <27.5:
        classification = "Overweight"
    case BMI if BMI >= 27.5:
        classification = "Obese"
print(f"Your BMI is {BMI:.2f} and you are {classification}")
