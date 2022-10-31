phrase = "How old are you?"
phrase += "\nEnter 'quit' when you are finished. "

while True:
    age = input(phrase)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")