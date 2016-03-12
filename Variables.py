# Loads responses from text file
openLines = open("Responses.txt", "r")
lines = openLines.read()
lines = lines.replace("\n", ".")
lines = lines.split(".")

# Loads words used to find emotional level
wordList = open("AFINN-111.txt", "r")
words = wordList.read()
words = words.replace(" ", ".")
words = words.replace("\t", ".")
words = words.split(".")

# Loads saved reponses Fai  can use
SaveResponses = open("SavedResponses.txt", "r")
Save = SaveResponses.read()
Save = Save.replace("\n", ".")
Save = Save.split(".")

#Reads the list of names and splits them between spaces
namesList = open("Names.txt", "r")
names = namesList.read()
names = names.replace("            ", " ")
names = names.replace("           ", " ")
names = names.replace("          ", " ")
names = names.replace("         ", " ")
names = names.replace("        ", " ")
names = names.replace("       ", " ")
names = names.replace("      ", " ")
names = names.replace("     ", " ")
names = names.replace("    ", " ")
names = names.replace("   ", " ")
names = names.replace("  ", " ")
names = names.replace(" ", " ")
names = names.replace("\n", " ")
names = names.lower()
names = names.split(" ")

# Username of user
userName = ""
# string used to store users response
Name = ""
# Users real name
TrueName = []
# The user's name is stored here.

questionAnswer = ""
Answer = ""
# The user's answers will be stored here.


# Emotion is the emotional level of the instance
emotion = 0
# baseline is the users base emotional level
baseline = 0
# currentEmotion is used to track the emotional level through out the conversation
currentEmotion = 0

FAIanswer = ""
numberOfChats = 3

word = []
index = 0

keywords = []

keywords_Job = []
keywords_Family = []
keywords_Love = []
keywords_Friends = []
keywords_Hobbies = []
keywords_Issues = []
keywords_Achievements = []

firstPart = ""
secondPart = ""
thirdPart = ""
fourthPart = ""

keywordsUsed = []



tempNextTopic = ""
topic = 0
topics = ["Baseline", "Job", "Family", "Love", "Friends", "Hobbies", "Issues", "Achievements"]