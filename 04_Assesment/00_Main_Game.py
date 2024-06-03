import random


# ask if player wants to read instructions and display if yes
def instructions_yes_no():
    while True:
        instructions = input("do you want to read the instructions? ").lower()

        # Lists of valid responses
        yes = ["yes", "y", "yea", "yeah", "ya"]
        no = ["no", "n", "nope", "na", "never"]

        if instructions in yes:
            print('''

**** Instructions ****

Objective:
answer as many of the questions right as you can

How to Play:
Pick how many questions you want 

It will come up in the format what is(A (+ or -) B)
You must find the answer to the question!
            ''')
            return "yes"

        # does not display if the player responds no
        elif instructions in no:
            print()
            return "no"

        # error if they dont enter a valid response
        else:
            print("please enter yes / no")


# ask player for how many questions they want to answer
def find_questions():
    while True:
        game = " "
        while game == " ":
            scores = input("how many questions do you want to answer? ").lower()

            try:
                score = int(scores)

                if 1 <= score <= 100:
                    return score

                else:
                    print()

            except ValueError:
                print()
            print("Please enter a whole integer 1 - 100 ")
            print()


def ask_question():
    number_1 = int(random.randint(1, 20))
    number_2 = int(random.randint(1, 20))
    pick_sign = random.randint(1, 2)

    if pick_sign == 1:
        sign = "+"

    else:
        sign = "-"

    while True:

        answer = input(f"what is {number_1} {sign} {number_2}? ")

        try:
            answer = int(answer)

            if sign == "+":

                if answer == number_1 + number_2:
                    print("correct")
                    return "correct"

                else:
                    print("wrong")
                    return "wrong"

            else:

                if answer == number_1 - number_2:
                    print("correct")
                    return "correct"

                else:
                    print("wrong")
                    return "wrong"

        except:
            print("please enter an integer")


# main code
print()
print("+-+- Welcome To Math Quiz -+-+")
print()

instructions_yn = instructions_yes_no()

number_of_questions = find_questions()

questions_asked = 0
questions_correct = 0

print()
start = input("press <enter> to start ")
print()

while number_of_questions >= 1:

    number_of_questions = number_of_questions - 1

    question = ask_question()

    questions_asked = questions_asked + 1

    if question == "correct":
        questions_correct = questions_correct + 1
        print()

    else:
        print()

results_yn = input("your quiz is finished do you want to read the results? ")

yes = ["yes", "y", "yea", "yeah", "ya"]
no = ["no", "n", "nope", "na", "never"]

if results_yn in yes:
    print()
    print(f"You answered {questions_asked} questions")
    print(f"you got {questions_correct} questions correct")

    percent = questions_correct / questions_asked * 100

    print(f"you got {percent}% of the Questions right")

else:
    print()

print("thank you for doing the Math Quiz")
