#ask for age
#age = input("How old are you: ")
#if age:
#    age = int(age) #convert age it int to avoid errors
#    if age>=18 and age<21:
#        #18 - 21 wristband
#        print("You can enter, but you need a wristband!")
#    elif age>=21:
#        #21+ drinks, normal entry
#        print("You are good to enter and drink as well!")
#    else:
#        #too young, Sorry kid
#        print("You can't come in, little one!")
#else:
#    print("Please enter your age!")

#A different way to implement above code is as follows;

age = input("How old are you: ")
if age:
    age = int(age) #convert age it int
    if age >= 21:
        print("You are good to enter and drink as well!")
    elif age >= 18:
        print("You can enter, but you need a wristband!")
    else:
        print("You can't come in, little one!")
else:
    print("Please enter your age!")
