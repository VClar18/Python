#ask for age
age=input("how old are you ")

#by default if empty falsy
if age:
    #turning age into a number
    age=int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wrist band")
    elif age >= 21:
        print("You are good to enter and can drink")
    else:
        print("you can't come in")
else:
    print("Please enter an age")