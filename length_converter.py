#Enter Height 
cm = float(input("Height in cm :"))

#Convert cm to inches
inches = cm / 2.54

#Get feet and leftover inches
feet = int( inches // 12 )
remaining_inches = round(inches % 12 ,2)

print(f"{cm} cm is approximately {feet} feet and {remaining_inches} inches. ")

