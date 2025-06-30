age=int(input("Type your age :"))
def age_checker(age):
    print("My age is :", age)
age_checker(age)
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
