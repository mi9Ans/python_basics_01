def simple_interest(p, r, t):
    return p * r * t / 100

a = int(input("Principal is :"))
b = int(input("Simple Interest % :"))
c = int(input("Time (in years) :"))

result = simple_interest(a, b, c)
print("Amount is :", result)
print("Total Amount is :", a + result)