import Variables
import User
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

# Takes user response and saves username
Variables.userName = input("Alright! To start us off, please can you tell me your name?")
print("It's nice to meet you, " + User.Username(Variables.userName))

#
Variables.QuestionAnswer = input("Would you say that you have had a good day today?")
print("Baseline level:", User.BaseAnalyse(Variables.questionAnswer))


Variables.QuestionAnswer = input("Hmm... okay then! Would you say that work has been on your mind recently?")
print("Current emotional level:", + User.analyse(Variables.questionAnswer, Variables.topics[Variables.topic]))

