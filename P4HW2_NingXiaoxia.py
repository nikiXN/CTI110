# Xiaoxia Ning
# 4/5/2024
# P4HW2
# The program is designed to calculate employee's total pay

# Initialize totals
total_overtime_pay = 0  
total_regular_pay = 0  
total_gross_pay = 0  
employee_count = 0

# Start a loop to collect employee data
while True:
    user_input = input('Enter employee\'s name or "Done" to terminate: ')
    employee_name = user_input
    
    # Check if the user wants to terminate the input process
    if user_input.lower() == 'done':
        break  # Exit the loop if user enters "Done".
    
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    
    # Evaluate if employee has worked overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
    else:
        overtime_hours = 0
        overtime_pay = 0
    
    # Calculate pay for regular hours worked
    regular_pay = min(hours_worked, 40) * pay_rate
    
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    # Display the results for the current employee
    print("\nEmployee Name:   ", employee_name)
    print()
    print("Hours Worked   Pay Rate       OverTime       OverTime Pay    RegHour Pay      Gross Pay")
    print("------------------------------------------------------------------------------------------------------")
    print(f'{hours_worked:<15.1f}{pay_rate:<15.1f}{overtime_hours:<15.1f}{overtime_pay:<16.2f}{regular_pay:<20.2f}{gross_pay:<15.2f}')
    print()

# After exiting the loop, print the totals
print()
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

