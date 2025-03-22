questions = ("Which of them has the biggest boobs?",
            "Which of them is the greatest masochist?",
             "Hatsune Miku is known for holding what?",
             "What is an intellectual drink for chosen ones?")
answers = ((" A - Akeno", "B - Koneko", "C - Rias", "D - Irina"),
            (" A - Megumin", "B - Aqua", "C - Darkness", "D - Yunyun"),
            (" A - leek", "B - onion", "C - radish", "D - garlic"),
            (" A - Cola", "B - Sprite", "C - Pepsi", "D - Dr Pepper"))
points=0

def repeat(question, answer):
    global points
    print(questions[question])
    print(answers[question])
    user_answer=input("Input your answer: ")
    if answer==user_answer.upper():
        points+=1

repeat(0,"A")
print()
repeat(1,"C")
print()
repeat(2,"A")
print()
repeat(3,"D")

print(f"\nYou got {points} points")
print(f"\nCorrect answers are: \n{questions[0]} {answers[0][2]}\n{questions[1]} {answers[1][2]}\n{questions[2]} {answers[2][0]}\n{questions[3]} {answers[3][3]}")
