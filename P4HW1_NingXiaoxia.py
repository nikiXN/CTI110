# Xiaoxia Ning
# 4/5/2024
# P4HW1
# This project collects user-entered scores, calculates and displays the average after dropping the lowest score, and then presents a letter grade based on the calculated average.


# Ask the user for the number of scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))
print()
# Initialize an empty list to store the scores
scores = []

# Create a loop to collect the scores
for i in range(num_scores):
    # Ask the user for a score
    score = int(input(f"Enter score #{i + 1}: "))
    
    # Check if the score is valid (between 0 and 100)
    if 0 <= score <= 100:
        scores.append(score)
         
    else:
        print()
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        score = int(input(f"Enter score #{i + 1} again: "))
        scores.append(score)

print()
print()
# Calculate the lowest score
lowest_score = min(scores)

# Create a modified list by removing the lowest score
modified_scores = []
for s in scores:
    if s !=lowest_score:
        modified_scores.append(float(s))

# Calculate the average of the modified list
average = sum(modified_scores) / len(modified_scores)
# Determine the letter grade based on the average
if 90 <= average <= 100:
    letter_grade = "A"
elif 80 <= average < 90:
    letter_grade = "B"
elif 70 <= average < 80:
    letter_grade = "C"
elif 60 <= average < 70:
    letter_grade = "D"
else:
    letter_grade = "F"                       
                               
# Print the collected scores
print("-------------Results--------------")
print(f"Lowest Score  : {lowest_score:.1f}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {letter_grade}")
print("-----------------------------------")
