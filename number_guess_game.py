#Lucky Number
lucky_number = 7
#Enter lucky number
n = None
#Assign Counter
attempt = 0

#Create Loop/Condition
while n != lucky_number:
    n = int(input("Guess Lucky Number :"))
    attempt+=1
    if n > lucky_number:
        print("Wrong Guess!, TOO LARGE")
    elif n < lucky_number:
        print("Wrong Guess, TOO SMALL")

print("Lucky Guess, YOU WON!")
print("Total Attempts :", attempt)

