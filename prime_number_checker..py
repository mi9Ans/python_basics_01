# Ask user for input
num = int(input("Enter a number: "))

# Assume it's prime unless proven otherwise
is_prime = True

# Prime check loop
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Output result
if is_prime:
    print("Prime")
else:
    print("Not Prime")


               