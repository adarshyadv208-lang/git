# Simple Quiz Game
 
# List of questions
questions = [
    "Q1. What is 2 + 3 * 2?\n   a) 10   b) 8   c) 12 d)16",
    "Q2. Which symbol is used for comments in Python?\n   a) //   b) #   c) -- d)@",
    "Q3. What is [1, 2, 3] in Python?\n   a) tuple   b) dict   c) list d)Row",
    "Q4. Which keyword starts a loop over a sequence?\n   a) for   b) if   c) def d)while",
    "Q5. What does len('python') give?\n   a) 5   b) 7   c) 6 d)8",
]
 
# List of correct answers (same order as questions)
answers = ["b", "b", "c", "a", "c"]
 
score = 0
 
# Loop: show one question at a time
for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ").lower()
 
    # If statement: check the answer
    if user_answer == answers[i]:
        print("Correct!\n")
        score = score + 1
    else:
        print("Wrong! Correct answer is", answers[i], "\n")
 
# Show final score
print("Your final score is", score, "out of", len(questions))
 