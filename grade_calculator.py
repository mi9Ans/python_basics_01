science_grade=int(input("Enter Science Grade :"))
math_grade=int(input("Enter Math Grade :"))
hindi_grade=int(input("Enter Hindi Grade :"))
english_grade=int(input("Enter English Grade :"))
computer_grade=int(input("Enter Computer Grade :"))

total=science_grade+math_grade+hindi_grade+english_grade+computer_grade
print("Total :",total)

percentage=total/500*100
print("Percentage % :",round(percentage,2))

if percentage >= 90:
    grade="A"
elif percentage >= 70:
    grade="B"
elif percentage >= 50:
    grade="C"
else:
    grade="Fail"
print(grade)
