age = int(input("Please enter the age: "))

if age < 13:
    print("This user is a child")
elif age >= 13 and age < 18:
    print("This user is teenager")
elif age >=18 and age < 65:
    print("This user is adult")
elif age >=65 and age < 100:
    print("This user is elder")
else:
    print("Please enter the correct age")