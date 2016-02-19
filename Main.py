import Variables
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

Variables.UserName = input("Alright! To start us off, please can you tell me your name?")
# Stores the username in UserName, in the Variables file.

print("It's nice to meet you, " + Variables.UserName + " To start us off, please would you answer this short question?")

Variables.QuestionAnswerOne = input("Would you say that you have had a good day today?")
# We need to ask the first question here. I have added in a sample question to get us started (Will need to be changed
# later!)

Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.split("," " ")

print(Variables.QuestionAnswerOne)

# This is where the user's reply is processed and split up to make each subsequent part easier to manage.

# This is where the emotional level is read, at least primarily
