sandwich_orders = [
    'pastrami', 'vegetable', 'cheese', 'Chicken', 'beef', 'pastrami']
finished_sandwiches = []

print("I'm soo sorry, we are all out of pastrami for today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

    

