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

# Loads saved responses Fai  can use
saveResponses = open("SavedResponses.txt", "r")
Save = saveResponses.read()
Save = Save.replace("\n", ".")
Save = Save.split(".")

# Loads the list of names and splits them between spaces
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

# Loads the list of topic questions
topicList = open("Topic_Questions.txt", "r")
t = topicList.read()
t = t.replace("\n", ".")
t = t.split(".")
t.reverse()

