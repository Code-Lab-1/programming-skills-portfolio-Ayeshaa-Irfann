Persons_age= int(input("Your age is="))
if Persons_age<2:
    print("The person is a Baby")
elif Persons_age==2 and Persons_age<4:
    print("The person is a Toddler")
elif Persons_age==4 and Persons_age>13:
    print("The person is a Kid")
elif Persons_age==13 and Persons_age<20:
    print("The person is a Teenager")
elif Persons_age==20 and Persons_age>65:
    print("The person is a Adult")
else:
    print("The person is Elder")