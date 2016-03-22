import Variables
import User
import AI
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

# Takes user response and saves username
Variables.userName = input("Alright! To start us off, please can you tell me your name?")
print("It's nice to meet you, " + User.Username(Variables.userName))

Variables.questionAnswer = input("Would you say that you have had a good day today?")
print("Baseline level:", User.BaseAnalyse(Variables.questionAnswer))

AI.TopicQuestions(Variables.topic)

AI.GenerateFortune()