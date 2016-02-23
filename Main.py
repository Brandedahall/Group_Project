import string
import Variables
import Dictionary
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

Variables.UserName = input("Alright! To start us off, please can you tell me your name?")
# Stores the username in UserName, in the Variables file.

print("It's nice to meet you, " + Variables.UserName + " To start us off, please would you answer this short question?")

Variables.QuestionAnswerOne = input("Would you say that you have had a good day today?")
# We need to ask the first question here. I have added in a sample question to get us started (To be changed later!)


# This is where the user's reply is processed and split up to make each subsequent part easier to manage.

exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

Variables.QuestionAnswerOne = ''.join(ch for ch in Variables.QuestionAnswerOne if ch not in exclude)
Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.lower()  # This turns all uppercase characters into lower case
Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.split(" ")  # This splits the string into a list of words.

print(Variables.QuestionAnswerOne)  # Prints the list of the words from the user's reply.

for Word in Variables.QuestionAnswerOne:
    if Word in Dictionary.ThingsList_General:
        Variables.Word_General = Word

print(Variables.Word_General)
# Now, with the splitting part out of the way, the process of reading each word is made easier. We want to be able to
# read the emotional level.
