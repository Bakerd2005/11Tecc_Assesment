def results(question):

    results_yn = input(question)
    yes = ["yes", "y", "yea", "yeah", "ya"]
    no = ["no", "n", "nope", "na", "never"]

    if results_yn in yes:
        print()
        print(f"You answered {questions_asked} questions")
        print(f"you got {questions_correct} questions correct")

        percent = questions_correct / questions_asked * 100

        print(f"you got {percent}% of the Questions right")

    elif results_yn in no:
        print()

    else:
        print("please enter yes/no")

results_yn = results("your quiz is finished do you want to read the results? ")