<<<<<<< HEAD
import string
import Variables
import AI

# Takes user input and saves their username
def Username(userName):
    # split string into list
    Variables.Name = Variables.userName.split(" ")
    if 'I' in Variables.Name:
        Variables.Name.remove('I')
    # If user inout is larger than one word
    if len(Variables.Name) >= 2:
        # Search through the list of names and appends username
        for word in Variables.Name:
            for name in Variables.names:
                if word == name:
                    Variables.TrueName.append(word)
        # If user name has used a capital letter then it is appended
        for x in Variables.Name:
            if x.istitle():
                if x == "My":
                    print("")
                else:
                    Variables.TrueName.append(x)
        Variables.Name.clear()
        Variables.Name = Variables.TrueName.pop()
    # If user has entered jsut their name
    if len(Variables.Name) == 1:
        Variables.Name = Variables.Name.pop()
    # If user has entered nothing then their name is set to Anonymous
    if len(Variables.Name) == 0:
        print("I see... well, since you didn't enter a name, I'll call you Anonymous!")
        Variables.Name = "Anonymous"
    return Variables.Name

# analyses users response and updates current emotional level
def Analyse(response, topic):
    exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.
    # breaks down user response and returns emotional level
    Variables.questionAnswer = response
    Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in exclude)
    Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
    Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
    for x in Variables.questionAnswer:
        if x in Variables.words:
            Variables.index = Variables.words.index(x)
            # exception handling allows us to pop a values and then insert it back into the list to be used again
            try:
                #Variables.emotion += int(Variables.words.pop(Variables.index + 1))
               # Variables.words.insert(Variables.index+1, 0)
                Variables.instanceEmotion = int(Variables.words.pop(Variables.index + 1))
                Variables.emotion += Variables.instanceEmotion
                Variables.words.insert(Variables.index+1, Variables.instanceEmotion)
            except ValueError:

                Variables.instanceEmotion = int(Variables.words.pop(Variables.index))
                Variables.emotion += Variables.instanceEmotion
                Variables.words.insert(Variables.index-1, Variables.instanceEmotion)
        if x not in Variables.words:
            Variables.emotion += 0
    # update current emotional level from user response
    Variables.currentEmotion += Variables.emotion
    print(Variables.currentEmotion)
    Variables.topic = AI.nexttopic(Variables.currentEmotion, topic, Variables.baseline)
    Variables.emotion = 0
    return Variables.currentEmotion, Variables.topic

# analyses the baseline response and establishes the baseline emotional level
def BaseAnalyse(response):
    exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

    Variables.questionAnswer = response
    Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in exclude)
    Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
    Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
    for x in Variables.questionAnswer:
        if x in Variables.words:
            Variables.index = Variables.words.index(x)
            # exception handling allows us to pop a values and then insert it back into the list to be used again
            try:
                Variables.emotion += int(Variables.words.pop(Variables.index + 1))
                Variables.words.insert(Variables.index+1, 0)
            except ValueError:
                Variables.emotion += int(Variables.words.pop(Variables.index))
                Variables.words.insert(Variables.index-1, 0)
        if x not in Variables.words:
            Variables.emotion += 0
    # establishes emotional baseline
    Variables.baseline += Variables.emotion
=======
import string
import Variables
import AI

# Takes user input and saves their username
def Username(userName):
    # split string into list
    Variables.Name = Variables.userName.split(" ")
    if 'I' in Variables.Name:
        Variables.Name.remove('I')
    # If user inout is larger than one word
    if len(Variables.Name) >= 2:
        # Search through the list of names and appends username
        for word in Variables.Name:
            for name in Variables.names:
                if word == name:
                    Variables.TrueName.append(word)
        # If user name has used a capital letter then it is appended
        for x in Variables.Name:
            if x.istitle():
                if x == "My":
                    print("")
                else:
                    Variables.TrueName.append(x)
        Variables.Name.clear()
        Variables.Name = Variables.TrueName.pop()
    # If user has entered jsut their name
    if len(Variables.Name) == 1:
        Variables.Name = Variables.Name.pop()
    # If user has entered nothing then their name is set to Anonymous
    if len(Variables.Name) == 0:
        print("I see... well, since you didn't enter a name, I'll call you Anonymous!")
        Variables.Name = "Anonymous"
    return Variables.Name

# analyses users response and updates current emotional level
def Analyse(response, topic):
    exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.
    # breaks down user response and returns emotional level
    Variables.questionAnswer = response
    Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in exclude)
    Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
    Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
    for x in Variables.questionAnswer:
        if x in Variables.words:
            Variables.index = Variables.words.index(x)
            # exception handling allows us to pop a values and then insert it back into the list to be used again
            try:
                Variables.emotion += int(Variables.words.pop(Variables.index + 1))
                Variables.words.insert(Variables.index+1, 0)
            except ValueError:
                Variables.emotion += int(Variables.words.pop(Variables.index))
                Variables.words.insert(Variables.index-1, 0)
        if x not in Variables.words:
            Variables.emotion += 0
    # update current emotional level from user response
    Variables.currentEmotion += Variables.emotion
    print(Variables.currentEmotion)
    Variables.topic = AI.nexttopic(Variables.currentEmotion, topic, Variables.baseline)
    Variables.emotion = 0
    return Variables.currentEmotion, Variables.topic

# analyses the baseline response and establishes the baseline emotional level
def BaseAnalyse(response):
    exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

    Variables.questionAnswer = response
    Variables.questionAnswer = ''.join(ch for ch in Variables.questionAnswer if ch not in exclude)
    Variables.questionAnswer = Variables.questionAnswer.lower()  # This turns all uppercase characters into lower.
    Variables.questionAnswer = Variables.questionAnswer.split(" ")  # This splits the string into a list of words.
    for x in Variables.questionAnswer:
        if x in Variables.words:
            Variables.index = Variables.words.index(x)
            # exception handling allows us to pop a values and then insert it back into the list to be used again
            try:
                Variables.emotion += int(Variables.words.pop(Variables.index + 1))
                Variables.words.insert(Variables.index+1, 0)
            except ValueError:
                Variables.emotion += int(Variables.words.pop(Variables.index))
                Variables.words.insert(Variables.index-1, 0)
        if x not in Variables.words:
            Variables.emotion += 0
    # establishes emotional baseline
    Variables.baseline += Variables.emotion
>>>>>>> origin/master
    return Variables.baseline