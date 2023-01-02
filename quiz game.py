question = {"In school, Albert Einstein failed most of the subjects, except for physics and math.": "Yes",
     "The first song ever sung in the space was Happy Birthday.": "Yes",
     " A male canary tends to have a better singing voice than a female canary.": "Yes",
     "Tea contains more caffeine than coffee and soda": "No",
     "Dogs have an appendix.": "No",
     "Bill Gates is the founder of Amazon.": "No",
     "Mice have more bones than humans.": "Yes",
     "The first product with a bar code was chewing gum": "Yes",
     "The Beatles is a famous rock band from Manchester, the United Kingdom": "No",
     "The star is the most common symbol used in all national flags around the world.": "Yes"}  # Pool of questions
import random

questionlist = []
while (len(questionlist) != 5):  # list of 5 questions
    i = random.choice(list(question.keys()))  # Choose Random question from question pool and make a list of it
    if (i not in questionlist):
        questionlist.append(i)  # make a list of random qustions
score = 0
print("""                                     
0    0 e   e e  000000   00000 00000 " 00000 0 0000000
0    0 8   8 8     0    00     0   8 8  80  00 8    
0    0 00  0 00 00000   00     00000 00 00  00 00000 
0 ___0 00  0 00 00      00   0 00  0 00 00  00 00   
000000 00000 00 00000   000000 00  0 00 00  00 0000000 

                                                   """)
for i in questionlist:
    print("\n" + i)
    a = input("\nEnter Yes or No: ")
    if (a == question[i]):
        print("\nRight answer! +5 points")
        score += 5
    else:
        print("\nWrong answer!")
print("\nTotal Score is :", score)
