
import time
import random
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

easy_questions=[
{
"question":"Which of the following is a programming language?",
"options":["a) HTML","b) Python","c) DNS","d) http"],
"answer":"b"
},

{
"question":"Which number system uses only 0 and 1?",
"options":["a) Octal","b) Hexadecimal","c) Binary","d) Decimal"],
"answer":"c"
},

{
"question":"What does CPU stand for?",
"options":["a) Central Process Unit","b) Central Processing Unit","c) Computer Personal Unit","d) Control Processing Unit"],
"answer":"b"
}
]

medium_questions = [
{
"question":"Which data structure uses LIFO principle?",
"options":["a) Queue","b) Stack","c) Array","d) Graph"],
"answer":"b"
},

{
"question":"Which keyword defines a function in Python?",
"options":["a) func","b) def","c) define","d) function"],
"answer":"b"
},

{
"question":"Which operator is used for exponent in Python?",
"options":["a) ^","b) **","c) //","d) %"],
"answer":"b"
}
]

hard_questions = [
{
"question":"Which data structure uses FIFO principle?",
"options":["a) Stack","b) Queue","c) Tree","d) Graph"],
"answer":"b"
},

{
"question":"Which sorting algorithm has average time complexity O(n log n)?",
"options":["a) Bubble Sort","b) Selection Sort","c) Merge Sort","d) Insertion Sort"],
"answer":"c"
},

{
"question":"Which of the following is NOT an operating system?",
"options":["a) Linux","b) Windows","c) Python","d) macOS"],
"answer":"c"
}
]

#QUIZ FUNCTION

def run_quiz(questions,player):

    score=0
    random.shuffle(questions)

    for q in questions:
        print(YELLOW+"\n"+q["question"]+RESET)

        for option in q["options"]:
            print(option)

        start=time.time()

        answer=input("Select a/b/c/d")

        end=time.time()

        if end-start>10:
            print(RED+"Time's over"+RESET)
            continue

        if answer.lower()==q["answer"]:
            print(GREEN+"Correct answer"+RESET)
            score+=1
        else:
            print(RED+"Wrong answer, Correct answer:",q["answer"], RESET)

    print(BLUE+"\nQUIZ FINISHED!" + RESET)
    print(player,"your score is:",score,"/",len(questions))
    save_score(player,score)

#SAVE SCORE FUNCTION
def save_score(name,score):
    file=open("leaderboard.txt","a")
    file.write(name+ ":"+ str(score)+ "\n")
    file.close()

    print(GREEN+"Score saved successfully"+RESET)

    #VIEW LEADERBOARD
def view_leaderboard():
    try:

        file=open("leaderboard.txt","r")

        print(BLUE+"\n ------LEADERBOARD------\n"+RESET)

        for line in file:
            print(line)

        file.close()

    except:

        print("No scores available yet")

    #DIFFICULTY LEVEL
def select_difficulty(player):

    print("\nSelect difficulty")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")

    choice=input("Enter your choice")

    if choice=="1":
        run_quiz(easy_questions,player)
    elif choice=="2":
        run_quiz(medium_questions,player)
    elif choice=="3":
        run_quiz(hard_questions,player)
    else:
        print("Invalid choice")

    #MAIN
def main():
    print(BLUE+"\n------QUIZ------\n"+RESET)

    player=input("Enter your name")
    while True:

        print("\nStart Quiz")
        print("1) Start quiz")
        print("2) View leaderboard")
        print("3) Exit")

        choice=input("Enter your choice")

        if choice=="1":
            select_difficulty(player)
        elif choice=="2":
            view_leaderboard()
        elif choice=="3":
            print("Exiting,Goodbye",player)
            break
        else:
            print("Invalid option")
#START PROGRAM

main()