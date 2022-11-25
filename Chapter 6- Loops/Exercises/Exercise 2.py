while True:
    age=int(input("Your age is="))
    if age == 'quit':
        break
    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

        