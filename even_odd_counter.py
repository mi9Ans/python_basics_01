start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

even_count = 0
odd_count = 0

current = start

while current <= end:
    if current % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    current += 1
print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
