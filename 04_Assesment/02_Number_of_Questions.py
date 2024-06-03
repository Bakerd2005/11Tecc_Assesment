def find_questions(question):
    while True:
        game = " "
        while game == " ":
            scores = input(question).lower()

            try:
                score = int(scores)

                if 1 <= score <= 100:
                    return score

            except ValueError:
                if scores == "infinite" or scores == "i":
                    return "infinite"
            print()
            print("Please enter a integer 1 - 100 or 'infinite' ")
            print()
