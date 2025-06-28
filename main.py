from question_model import Question
from question_data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    # Every 5 questions, ask the user if they want to continue
    if quiz.question_number % 5 == 0 and quiz.question_number != len(quiz.question_list) and quiz.still_has_questions():

        user_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if user_choice != "yes":
            print("Thank you for playing!")
            break  # Exit the loop if the user says no

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")