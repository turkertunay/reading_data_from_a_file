
print("1. print all lines")
print("2. print only first line")
print("3. print first two lines")
print("4. print all the lines by readlines method")
print("5. print only the third line")
print("6. print all the lines with for loop")

choice = int(input("Enter the operation you want to do with this file: "))

if choice == 1:
    footballer_nation = open("fn.txt", "r")
    print(footballer_nation.read())
    footballer_nation.close()

if choice == 2:
    footballer_nation = open("fn.txt", "r")
    print(footballer_nation.readline())
    footballer_nation.close()

if choice == 3:
    footballer_nation = open("fn.txt", "r")
    print(footballer_nation.readline())
    print(footballer_nation.readline())
    footballer_nation.close()

if choice == 4:
    footballer_nation = open("fn.txt", "r")
    print(footballer_nation.readlines())
    footballer_nation.close()

if choice == 5:
    footballer_nation = open("fn.txt", "r")
    print(footballer_nation.readlines()[2])
    footballer_nation.close()

if choice == 6:
    footballer_nation = open("fn.txt", "r")
    for footballer in footballer_nation.readlines():
        print(footballer)
    footballer_nation.close()