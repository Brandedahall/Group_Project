import Variables
import User
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

Variables.UserName = input("Alright! To start us off, please can you tell me your name?")

print("It's nice to meet you, " + User.username(Variables.UserName) + ". To start us off, please would you answer "

                                                      "this short question?")
Variables.QuestionAnswer = input("Would you say that you have had a good day today?")
# We need to ask the first question here. I have added in a sample question to get us started (To be changed later!)

# Now, with the splitting part out of the way, the process of reading each word is made easier. We want to be able to
# read the emotional level.

print("Emotional level:", User.analyse(Variables.QuestionAnswer, Variables.Topics[Variables.Topic]))
Variables.baseline = Variables.baseline + Variables.Emotion



