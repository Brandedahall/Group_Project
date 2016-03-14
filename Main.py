<<<<<<< HEAD
import Variables
import User
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

# Takes user response and saves username
Variables.userName = input("Alright! To start us off, please can you tell me your name?")
print("It's nice to meet you, " + User.Username(Variables.userName))

#
Variables.questionAnswer = input("Would you say that you have had a good day today?")
print("Baseline level:", User.BaseAnalyse(Variables.questionAnswer))

# Variables.questionAnswer = input("Hmm... okay then! Would you say that work has been on your mind recently?")
# print("Current emotional level:", + User.analyse(Variables.questionAnswer, Variables.topics[Variables.topic]))

# A way to navigate through the tpoic questions
# We will need to include a way of collecting keyword the user inputs for each topic. Hence the separate if statements
while Variables.topic < 5:
    if Variables.topic == 0:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexJob))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexJob -= 2
    if Variables.topic == 1:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexFam))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexFam -= 2
    if Variables.topic == 2:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexLove))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexLove -= 2
    if Variables.topic == 3:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexFnd))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexFnd -= 2


=======
import Variables
import User
# Imports the variables file.

print("Hello! I'm FAI, but please call me Fortune!")
# Simple greeting.

# Takes user response and saves username
Variables.userName = input("Alright! To start us off, please can you tell me your name?")
print("It's nice to meet you, " + User.Username(Variables.userName))

#
Variables.questionAnswer = input("Would you say that you have had a good day today?")
print("Baseline level:", User.BaseAnalyse(Variables.questionAnswer))

# Variables.questionAnswer = input("Hmm... okay then! Would you say that work has been on your mind recently?")
# print("Current emotional level:", + User.analyse(Variables.questionAnswer, Variables.topics[Variables.topic]))

# A way to navigate through the tpoic questions
# We will need to include a way of collecting keyword the user inputs for each topic. Hence the separate if statements
while Variables.topic < 5:
    if Variables.topic == 0:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexJob))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexJob -= 2
    if Variables.topic == 1:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexFam))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexFam -= 2
    if Variables.topic == 2:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexLove))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexLove -= 2
    if Variables.topic == 3:
        Variables.questionAnswer = input(Variables.t.pop(Variables.topicIndexFnd))
        User.Analyse(Variables.questionAnswer, Variables.topic)
        Variables.topicIndexFnd -= 2


>>>>>>> origin/master
