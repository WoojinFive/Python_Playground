def age_program():
    user_age = input("Enter your age: ")
    age_seconds = int(user_age) * 365 * 24 * 60 * 60
    print("Your age in secondes is {}".format(age_seconds))

age_program()