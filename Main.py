import Variables
import User
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

Variables.UserName = input("Alright! To start us off, please can you tell me your name?")

print("It's nice to meet you, " + User.username(Variables.UserName))

while Variables.Topic < 9:

    Variables.QuestionAnswer = input("Would you say that you have had a good day today?")

    print("Emotional level:", User.analyse(Variables.QuestionAnswer, Variables.Topics[0]))
    Variables.baseline = Variables.baseline + Variables.Emotion

    if Variables.keywords_Job == 1:
        Variables.QuestionAnswer = input("Hmm... okay then! Would you say that work has been on your mind recently?")

        print("Emotional level:", User.analyse(Variables.QuestionAnswer, Variables.Topics[Variables.Topic]))
        Variables.baseline = Variables.baseline + Variables.Emotion
    else:
        Variables.QuestionAnswer = input("Hmm... okay then! Would you say that work has been on your mind recently?")

        print("Emotional level:", User.analyse(Variables.QuestionAnswer, Variables.Topics[Variables.Topic]))
        Variables.baseline = Variables.baseline + Variables.Emotion