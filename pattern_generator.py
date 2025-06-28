## This program prints star or number triangles based on user choice

value = int(input("Type the length :"))
choice = (input("What pattern do you want-stars or numbers :"))
for i in range (1,value+1):
    for j in range(i):
        if choice.lower == "stars":
            print("*" ,end=" ")
        else:
            print(j+1 ,end=" ")
    print()





