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
Pick how many questions you want (there is only 50 questions so some may be repeated)

It will come up in the format (A (+ or -) B = X)>
You must find x
on the next line it will display (X =) and you have to enter your answer there

            ''')
            return "yes"

        # does not display if the player responds no
        elif instructions in no:
            print()
            return "no"

        # error if they dont enter a valid response
        else:
            print("please enter yes / no")
