change = (input("Either choose 1(Celcius to Fahrenhite) or 2(Fahrenhite to Celcius) :"))

if change == "1":
    celcius = float(input("Temperature(in celcius) :"))
    print("Temerature is (in Fahrenhite) :", round(celcius * 9 / 5 + 32, 2))

elif change == "2":
    fahr = float(input("Temperatuere is (in fahrenhite) :"))
    print("Temperature is (in celcius) :", round((fahr - 32) * 5 / 9, 2 ))
