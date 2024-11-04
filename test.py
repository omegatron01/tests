test = ("What is the full meaning of CPU?" ,
        'What year did Nigeria get her independence?' ,
        'What is the capital of Nigeria?' ,
        'Who is Lebron James?',
        'How many continents are there in the world?')

options = (("A. Central Processing Unit", "B. Central Programming Unit" , "C. Central Prop Unison") ,
          ("A. 1960" , "B.1963" ,"C.1769") ,
          ('A. Abuja', 'B. Lagos', 'C. Port Harcourt'),
          ('A. Footballer', 'B. Basketballer', 'C. Actor'),
          ('A. 7', 'B. 6', 'C. 9'))

count = 0
quest_num = 0
answers = []
corrects = ("A" , "A" , "A" , "B" , "A")

for question in test:
    print(question)
    for option in options[quest_num]:
        print(option)
    answer = input('ENTER CORRECT OPTION: ').upper()
    answers.append(answer)
    if answer == corrects[quest_num]:
        count += 1
        print("CORRECT!!!")
    else:
        print("INCORRECT!!!")
    quest_num += 1


score = 100 * (count / 5)
print(f"Your score is:  {score}")
if score < 50:
    print("OLODO!!!")
elif score < 90:
    print("GOOD!\nSTRIVE FOR MORE!!!")
else:
    print("EXCELLENT!!!!")


