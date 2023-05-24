tip = int(input("Enter the of tip percentage: % "))

if tip > 15 and tip < 18:
    print("That tip was ok, not impressed..")
elif tip >= 18 and tip < 20:
    print("That tip is alright, can be better")
elif tip == 20:
    print("Amazing")
elif tip > 20 and tip <=100 :
    print("Awesome, you are my hero")
else:
    print("Stop dreaming, try again")