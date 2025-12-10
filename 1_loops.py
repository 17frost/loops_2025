# # Example Practice:
# # Given this list of fruits:
# fruits = ["apple", "banana", "cherry", "date"]
# print(len(fruits))
# # Challenge:
# # Use a for loop to print each fruit on a new line.
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# for fruit in fruits:
#     print(fruit)
# # i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)
    if subject == "History":
        break
    print(subject)

for subject in subjects:
    print(subjects)
    if subject == "Science":
        continue # prints out each list item and skips science.
    print(subject)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"

# list600 = list(range(1, 601))
# for number in list600:
#     if 300 <= int(number) <= 500:
#         continue
#     print(number)
# # Given:
# numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.


# applicants_for_credit = ["Alice", "Bob", "Charlie", "David", "Eve"]
# credit_scores = [720, 680, 590, 610, 750]
# for applicant, score in zip(applicants_for_credit, credit_scores): # Alice = 720, Bob = 680, and so on
#     if score <= 600:
#         continue
#     print(applicant + " approved for credit with score: " + str(score))

for index in range(len(subjects)):
    print("Subject " + str(index) + ": " + subjects[index])

list_to_sum = [1, 2, 3, 4, 5]
total = 0
for sums in list_to_sum:
    total = total + sums
print("Total: ", total)

new_numbers = list(range(1,261))
total1 = 0
for addend in new_numbers:
    print(total1)
    total1 = total1 + addend
print("Total1 = ", total1)