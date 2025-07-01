def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("Your BMI is:", round(bmi, 2))
    
    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

# Taking input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Call the function
calculate_bmi(weight, height)
