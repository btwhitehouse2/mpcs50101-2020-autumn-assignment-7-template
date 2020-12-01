import random as r
import problem3 as p3

def play_math_game():
    """ Confirms the parameters of the game
    beginning with a while Loop
     we set the attempts and score to 0 outside of the while loop meaning they will 
     store their values unless you restart the game
     """
    #attempts will increase regardless of getting the question right!
    attempts = 0
    #score will increase only if the answer is correct!
    score = 0

    while True:
        try:
            #here the player will input if they want to play
            play_game =input("Do you want to play the math game? [y/n]")
            #converts the letter response to lower to avoid in Y or N issues
            play_game = play_game.lower()
            
            #the game begins
            if play_game == 'y':
                #using randint to assign a number that will correspond to the type of problem the player will recieve
                math = r.randint(1,4)
                #assigning numerator1
                n1 = r.randint(0,9)
                #assigning denominator1
                d1 = r.randint(1,9)
                #assigning numerator2
                n2 = r.randint(0,9)
                #assigning denominator2
                d2 = r.randint(1,9)
                f1 = p3.Fraction(n1,d1)
                f2 = p3.Fraction(n2,d2)
                #fraction addition
                if math == 1:
                    guess = input(print(r"What is ",n1,"/",d1, "+", n2,"/",d2, " equal to: ",'\n','Please return your value if able as an interger then mixed fraction (ie. 9/8 = 1-1/8) and finally fraction if required: '))
                    answer = f1+f2
                    #in this case the player answered the question correctly
                    if guess == answer:
                        attempts += 1
                        score +=1
                        print("Congrats you got it right! You are",score,"of",attempts,"so far.")
                    #any answer other than the correct answer
                    else:
                        attempts += 1
                        print("Sorry, the correct answer is ", answer,"You are",score,"of",attempts,"so far.")
        

                #fraction subtraction
                elif math == 2:
                    guess = input(print("What is ",n1,"/",d1,"-", n2,"/",d2, " equal to: ",'\n','Please return your value if able as an interger then mixed fraction (ie. 9/8 = 1-1/8) and finally fraction if required'))
                    answer = f1-f2
                    if guess == answer:
                        attempts += 1
                        score +=1
                        print("Congrats you got it right! You are",score,"of",attempts,"so far.")

                    else:
                        attempts += 1
                        print("Sorry, the correct answer is ", answer,"You are",score,"of",attempts,"so far.")

                #fraction multiplication
                elif math == 3:
                    guess = input(print("What is ",n1,"/",d1,"*", n2,"/",d2, " equal to: ",'\n','Please return your value if able as an interger then mixed fraction (ie. 9/8 = 1-1/8) and finally fraction if required'))
                    answer = f1*f2
                    if guess == answer:
                        attempts += 1
                        score +=1
                        print("Congrats you got it right! You are",score,"of",attempts,"so far.")

                    else:
                        attempts += 1
                        print("Sorry, the correct answer is ", answer,"You are",score,"of",attempts,"so far.")

                #fraction division
                else:
                    guess = input(print("What is ",n1,"/",d1,"/", n2,"/",d2, " equal to: ",'\n','Please return your value if able as an interger then mixed fraction (ie. 9/8 = 1-1/8) and finally fraction if required'))
                    answer = f1/f2
                    if guess == answer:
                        attempts += 1
                        score +=1
                        print("Congrats you got it right! You are",score,"of",attempts,"so far.")
                    else:
                        attempts += 1
                        print("Sorry, the correct answer is ", answer,"You are",score,"of",attempts,"so far.")
            elif play_game == 'n':
                print("Come back soon, you answered",score,"of",attempts,",correctly")
                score = 0
                attempts = 0
                break
            else:
                print("Please input a y or n")


        except:
            print("Please enter y or n ")

def main():
    play_math_game()

if __name__ == "__main__":
    main()