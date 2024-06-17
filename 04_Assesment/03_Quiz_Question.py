import random


def ask_question():
    number_1 = int(random.randint(1, 20))
    number_2 = int(random.randint(1, 20))
    pick_sign = random.randint(1, 4)

    if pick_sign == 1:
        sign = "+"
        correct_answer = number_1 + number_2
        right_answer = number_1 + number_2

    elif pick_sign == 2:
        sign = "-"
        correct_answer = number_1 - number_2
        right_answer = number_1 - number_2

    elif pick_sign == 3:
        sign = "x"
        correct_answer = number_1 * number_2
        right_answer = number_1 * number_2

    else:
        sign = "/"
        correct_answer = round(number_1 / number_2)
        right_answer = number_1 / number_2

    while True:

        if sign == "/":
            answer = input(f"What is {number_1} {sign} {number_2}? (the answer is rounded to the nearest whole number)")

            try:
                answer = round(float(answer))

                if answer == correct_answer:
                    print("correct")
                    return "correct"

                else:
                    print("wrong")
                    print()
                    print(f"the correct answer was {right_answer}")
                    return "wrong"

            except ValueError:
                print("please enter an integer")

        else:
            answer = input(f"What is {number_1} {sign} {number_2}? ")

            try:
                answer = float(answer)

                if answer == correct_answer:
                    print("correct")
                    return "correct"

                else:
                    print("wrong")
                    print()
                    print(f"the correct answer was {right_answer}")
                    return "wrong"

            except ValueError:
                print("please enter an integer")


# main code
hi = ask_question()
