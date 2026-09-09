# Write a program that calculates and displays the grade based on the following grading scale:
# Grade ranges: A: 90-100; B: 80-89; C: 70-79; D: 60-69; F: 0-59;
# input: score = 89;  output: B

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
elif score >= 0 and score < 60:
    print("Grade: F")
else:
    print("Invalid input")
