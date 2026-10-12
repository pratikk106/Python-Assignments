
questions = [
    "1. What is the capital of India? ",
    "2. How many days are in a week? ",
    "3. Which language is used for web page styling? ",
    "4. What is 5 + 5? ",
    "5. Which planet is known as the Red Planet? ",
    "6. What is the largest ocean on Earth? "
]

answers = ["delhi", "7", "css", "10", "mars", "pacific"]

score = 0

for i in range(6):
    user_answer = input(questions[i]).lower()

    if user_answer == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

percentage = (score / 6) * 100

print("\nScore:", score, "out of 6")
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent")
elif percentage >= 60:
    print("Good")
else:
    print("Keep Practicing")
