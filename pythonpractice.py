from Questions import Question

question_prompt =[
    "What is the tallest building in the world?\n(a)The Burj khalifa\n(b)The Royal court hotel\n(c)The dynasty\n",
    "\n\nWho died for our sins?\n(a)Mohammed\n(b)Jesus\n(c)Ghandi\n",
    "\n\nWhich continents do people with dark skin dominate?\n(a)Europe\n(b)Africa\n(c)Antartica\n"
]

QnA = [
      Question(question_prompt[0], "a"),
      Question(question_prompt[1], "b"),
      Question(question_prompt[2], "b")
]

def quizrun(QnA):
    score = 0
    noofq = 0
    for question in QnA:
         answer = input(question.prompt + "Enter your answer: ")
         noofq += 1
         if answer == question.answer:
            score += 1
    if noofq == 3:
         print("You got " + str(score) + "/" + str(len(QnA)) + " correct")
    else:
         print("You got " + str(score) + "/" + str(len(QnA)) + " correct")
         
    

quizrun(QnA)