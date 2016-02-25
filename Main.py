import string
import Variables
import Dictionary
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

Variables.UserName = input("Alright! To start us off, please can you tell me your name?")
# Stores the username in UserName, in the Variables file.

Variables.Name = Variables.UserName.split(" ")
if 'I' in Variables.Name:
    Variables.Name.remove('I')

if len(Variables.Name) > 2:
    for x in Variables.Name:
        if x.istitle():
            Variables.TrueName.append(x)
    Variables.Name.clear()
    Variables.Name = Variables.TrueName.pop()
if len(Variables.Name) == 1 and 2:
    Variables.Name = Variables.Name.pop()
if len(Variables.Name) == 0:
    print("I see... well, since you didn't enter a name, I'll call you Anonymous!")
    Variables.Name = "Anonymous"

    print()

print("It's nice to meet you, " + Variables.Name + ". To start us off, please would you answer this short question?")
Variables.QuestionAnswerOne = input("Would you say that you have had a good day today?")
# We need to ask the first question here. I have added in a sample question to get us started (To be changed later!)


# This is where the user's reply is processed and split up to make each subsequent part easier to manage.

exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

Variables.QuestionAnswerOne = ''.join(ch for ch in Variables.QuestionAnswerOne if ch not in exclude)
Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.lower()  # This turns all uppercase characters into lower case
Variables.QuestionAnswerOne = Variables.QuestionAnswerOne.split(" ")  # This splits the string into a list of words.


# This looks for any words that are in each of the dictionaries in Dictionary.py and increments.
for Word in Variables.QuestionAnswerOne:
    if Word in Dictionary.ThingsList_General:
        Variables.Word.append(Word)
        Variables.ThingsList_General += 1
    if Word in Dictionary.ThingsList_Picturable:
        Variables.Word.append(Word)
        Variables.ThingsList_Picturable += 1
    if Word in Dictionary.OperationList:
        Variables.Word.append(Word)
        Variables.OperationList += 1
    if Word in Dictionary.QualityList:
        Variables.Word.append(Word)
        Variables.QualityList += 1
    if Word in Dictionary.QualitiesList:
        Variables.Word.append(Word)
        Variables.QualitiesList += 1

print(Variables.Word)
print("Type of word:       : Amount:")
print("Things_General      :", Variables.ThingsList_General)
print("Things_Picturable   :", Variables.ThingsList_Picturable)
print("Operation           :", Variables.OperationList)
print("Quality             :", Variables.QualityList)
print("Qualities           :", Variables.QualitiesList)

# Now, with the splitting part out of the way, the process of reading each word is made easier. We want to be able to
# read the emotional level.

print(Dictionary.Words)
