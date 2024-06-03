import random


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
hi = ask_question()
