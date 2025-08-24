name = input("Enter your name: ")
age=int(input("Enter your age: "))
gender = input("Enter gender (Male/Female): ")
weight= float(input("enter your weight in kg: "))
height = float(input("enter your height in cm: "))
height = height / 100  # Convert height from cm to m
bmi = weight / (height * height)

print("Hello! " + name, "\n your age is: ",age, "\n your gender is:", gender,
      "\n your weight is: ", weight, "kg", "\n your height is: ", height, "m",
      "\n your BMI is: ", round(bmi, 2))