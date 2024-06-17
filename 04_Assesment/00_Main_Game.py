import random


# ask if player wants to read instructions and display if yes
def instructions_yes_no():
    while True:
        instructions = input("do you want to read the instructions? ").lower().strip()

        # Lists of valid responses
        yes = ["yes", "y", "yea", "yeah", "ya"]
        no = ["no", "n", "nope", "na", "never"]

        # display instructions
        if instructions in yes:
            print('''
**** Instructions ****

Objective:
answer as many of the questions right as you can

How to Play:
Pick how many questions you want 

It will come up in the format what is(A (+ or -) B)
You must find the answer to the question!
you can round your answer to the nearest whole number
or give the exact number
            ''')
            return "yes"

        # does not display if the player responds no
        elif instructions in no:
            print()
            return "no"

        # error if they don't enter a valid response
        else:
            print("please enter yes / no")


# ask player for how many questions they want to answer
def find_questions():
    # loop so it continues to ask until you get
    while True:
        game = " "
        while game == " ":
            # find number of rounds to set
            scores = input("how many questions do you want to answer? ").lower()


            try:
                # check if they entered an integer
                score = int(scores)

                # only allow them to do an number between 1 and 100
                if 1 <= score <= 100:
                    return score

                else:
                    print()

            # if they did not enter a number give an error statement
            except ValueError:
                print()

            print("Please enter a whole integer 1 - 100 ")
            print()


# ask the question
def ask_question():
    # Create the question
    number_1 = int(random.randint(1, 20))
    number_2 = int(random.randint(1, 20))
    pick_sign = random.randint(1, 4)

    # set the type of equation
    if pick_sign == 1:
        sign = "+"
        correct_answer_round = number_1 + number_2
        correct_answer = number_1 + number_2

    elif pick_sign == 2:
        sign = "-"
        correct_answer_round = number_1 - number_2
        correct_answer = number_1 - number_2

    elif pick_sign == 3:
        sign = "x"
        correct_answer_round = number_1 * number_2
        correct_answer = number_1 * number_2

    else:
        sign = "/"
        correct_answer_round = round(number_1 / number_2)
        correct_answer = number_1 / number_2

    # loop so it asks the question again if you dont input a float
    while True:

        # if it is division run this code
        if sign == "/":
            # ask question
            answer = input(f"What is {number_1} {sign} {number_2}? (the answer is rounded to the nearest whole number)")

            try:
                # check if they entered a float
                answer = float(answer)

                # if they got the right number rounded tell them they are right
                if answer == correct_answer_round:
                    print("correct")
                    return "correct"

                # if they got the right number tell them they are right
                elif answer == correct_answer:
                    print("correct")
                    return "correct"

                # if they are wrong tell them they are wrong
                else:
                    print("wrong")
                    print()
                    print(f"the correct answer was {correct_answer}")
                    return "wrong"

            # display error if they did not enter a number
            except ValueError:
                print("please enter a number")

        # if it is not division run this code
        else:
            # ask question
            answer = input(f"What is {number_1} {sign} {number_2}? ")

            try:
                # check if they entered a float
                answer = float(answer)

                # if they got the right number tell them they are right
                if answer == correct_answer:
                    print("correct")
                    return "correct"

                # if they are wrong tell them they are wrong
                else:
                    print("wrong")
                    print()
                    print(f"the correct answer was {correct_answer}")
                    return "wrong"

            # display error if they did not enter a number
            except ValueError:
                print("please enter a number")


# show results if person what's to see them
def results(question):
    # loop so it repeats the question if you dont answer with a valid input
    while True:
        # asks question
        results_yn = input(question)

        # lists of valid answers
        yes = ["yes", "y", "yea", "yeah", "ya"]
        no = ["no", "n", "nope", "na", "never"]

        # if they say yes show the results
        if results_yn in yes:
            print()
            print(f"You answered {questions_asked} questions")
            print(f"you got {questions_correct} questions correct")

            percent = questions_correct / questions_asked * 100

            print(f"you got {percent}% of the Questions right")
            return "yes"

        # if they say no do not show the results and continue the code
        elif results_yn in no:
            print()
            return "no"

        # if they put in an invalid input display error message
        else:
            print("please enter yes/no")


# main code
# show title
print()
print("+-+- Welcome To Math Quiz -+-+")
print()

# ask to show instructions and show if they want to see them
instructions_yn = instructions_yes_no()

# set the number of questions that will be asked
number_of_questions = find_questions()

# reset the number of questions asked variable and the number of correct answers they have got to 0
questions_asked = 0
questions_correct = 0

# make them press enter to start the game
print()
start = input("press <enter> to start ")
print()

# loop so it asks different question over and over until the user has got the number of questions they wanted
while number_of_questions >= 1:

    # every time a question is asked minus 1 of the total number of questions they need to be asked
    number_of_questions = number_of_questions - 1

    # ask the question
    response = ask_question()

    # add 1 to the variable counting how many question have been asked
    questions_asked = questions_asked + 1

    # if they answered the question right add to the variable counting how many questions they have got right
    if response == "correct":
        questions_correct = questions_correct + 1
        print()

    # if they didn't answer the question right dont add to the variable counting how many questions they have got right
    else:
        print()

# if they want to see the results display them
show_results = results("your quiz is finished do you want to read the results? ")

# thank them for playing and indicate the end of the code
print("thank you for doing the Math Quiz")
