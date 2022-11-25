guests= ["Saniya" , "Harera" , "Iman"]
print(guests)

message="Please be there for dinner this Friday"
print(guests[0], message)
print(guests[1], message)
print(guests[2], message)

print(guests[1]) 
guests[1]= ("Sana")
print(guests)
print(guests[0], message)
print(guests[1], message)
print(guests[2], message)
print('Sorry i can only invite 2 people for the dinner this friday')

name= guests.pop()
message2= "Sorry, can't invite you for dinner"
print(guests[0], message2)

