age = int(input("Enter your age: "))

if age == 100:
    print("kudos you oldtimer")
elif age >= 18:
    print("you are now signed up!")
elif age <= 0:
    print("stop playing games now")
else:
    print("you must be 18 or older to sign up.")