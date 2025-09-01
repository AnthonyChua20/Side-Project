try:
    height=  float(input("Enter your height in cm: "))/100
    maxWeight = 22.9 * (height ** 2)
    minWeight = 18.5 * (height ** 2)
    print("Your ideal weight is between ", round(minWeight,2), "kg and ", round(maxWeight,2), "kg")
except ValueError:
    print("Invalid input for height. Please enter a number.")
    exit()


# bmi = weight / (height * height) # BMI formula

