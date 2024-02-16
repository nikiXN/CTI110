# Xiaoxia Ning

# 2/15/2024

# P1HW2

# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print()
# Ask user to enter their budget
budget = int(input("Enter Budget: "))
print()
# Ask user to enter travel destination
destination = input("Enter your travel destination: ")
print()
# Ask user for amount they will spend on gas
gas = int(input("How much do you think you will spend on gas? "))
print()
# Ask user for amount they will spend on accommodation
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
print()
# Ask user for amount they will spend on food
food = int(input("Last, how much do you need for food? "))
print()
# Add expenses
expenses = gas + accommodation + food

# Subtract expenses from budget
remaining = budget - expenses
               
# Display results
print("\n--------------Travel Expenses--------------")
print("Location: ",destination)
print("Initial Budget: ",budget)
print()
print("Fuel: ",gas)
print("Accomodation: ",accommodation)
print("Food: ",food)
print()
print("Remaining Balance: ",remaining)
