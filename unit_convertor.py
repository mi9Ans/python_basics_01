unit=input("What would you like to convert? Type 1 for KM to Miles, 2 for Miles to KM :")

if unit == "1":
    km = int(input("Enter distance in KM :"))
    print("Distance in Miles :", round(km * 0.621371, 2),"Miles")

elif unit == "2":
    miles = int(input("Enter distance in Miles :"))
    print("Distance in KM :", round(miles / 0.621371, 2),"KM")

else:
    print("Invalid Choice!")




