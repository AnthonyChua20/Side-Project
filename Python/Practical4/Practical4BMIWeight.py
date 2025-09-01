try:
    height=  float(input("Enter your height in cm: "))/100
    idealBmi = 22.9
    idealBmi2 = 18.5
    idealWeight = idealBmi * (height ** 2)
    idealWeight2 = idealBmi2 * (height ** 2)
    print("Your ideal weight is between ", round(idealWeight2,2), "kg and ", round(idealWeight,2), "kg")
except ValueError:
    print("Invalid input for height. Please enter a number.")
    exit()


# bmi = weight / (height * height) # BMI formula

