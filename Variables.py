import Functions
import string
import random

topicRND = random.randint(2, 4)
fortuneRND = random.randint(8, 10)
# Index used to track the topic questions
topicIndexJob = 0
topicIndexFam = 0
topicIndexLove = 0
topicIndexFri = 0

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
# instance
instanceEmotion = 0
FAIanswer = ""
numberOfChats = 0

word = []
index = 0

# List of questions fai asks broken down into separate lists
# I have used separate lists rather than one list because its easier poping specific topics from separate lists
questionsJob = ["Tell me, what is it that you do for a living?",
                "Break down your emotions and feelings about your job into one word for me.",
                "Interesting, but what are your future career plans?"]
questionsFam = ["Who do you feel the most connected to within your family? Who understands you the most?",
                "It seems there was a significant family event that was meaningful to you. A recent holiday or family gathering?",
                "I see, Do you wish you could see your family more?"]
questionsLove = ["Do you believe you have found your soul mate? A boyfriend or girlfriend perhaps?",
"Which month did you meet your other half? There is great significance behind the joining of yourself and your partner",
"Do you feel like you need to surround yourself with more positive energy in your life"]
questionsFri = ["I can sense you have made a powerful bond with someone who is not of the same blood. Tell me the name of your closest friend.",
"How many years have you known this person?",
"It is important to surround yourself with people you have formed bonds with, Can you say that you do?"]

# List of keywords user has used broken down for the first two questions of each topic
userKeywordsJobQ1 = ["individual"]
userKeywordsJobQ2 = ["okay"]
userKeywordsFamQ1 = ["family"]
userKeywordsFamQ2 = ["family event"]
userKeywordsLoveQ1 = ["loved one"]
userKeywordsLoveQ2 = ["time"]
userKeywordsFriQ1 = ["your friend"]
userKeywordsFriQ2 = [""]
# Fais saved keywords
keywordsJobQ1 = ["teacher", "presenter", "unemployed", "student"]
keywordsJobQ2 = Functions.words
keywordsFamilyQ1 = ["mom", "mum", "dad", "brother", "sister", "dad", "father", "mother", "daddy", "mommy"]
keywordsFamilyQ2 = ["holiday", "party", "birthday", "christmas", "easter"]
keywordsLoveQ1 = ["wife", "husband", "girlfriend", "boyfriend"]
keywordsLoveQ2 = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
keywordsFriendsQ1 = Functions.names
keywordsFriendsQ2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                     "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                     "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                     "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                     "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                     "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
                     "61", "62", "63", "64", "65", "66", "67", "68", "69", "70"]
# These words are used to change the topic if the user mentions them
keywordsJob = ["teacher", "tv presenter", "unemployed", "student"]
keywordsFamily = ["mom", "dad", "brother", "sister"]
keywordsLove = ["wife", "husband", "girlfriend", "boyfriend"]
keywordsFriends = ["friend", "friends"]
# counts used to keep track with the number of keywords in users response. Once used to change
# the conversation the counts are assigned negative numbers to asure they do not trigger again
countJob = 0
countFamily = 0
countLove = 0
countFriends = 0

# value used to represent the current topic
topic = 0

# values used to store the value of the emotional value of each topic
emotionJob = 0
emotionFamily = 0
emotionLove = 0
emotionFriend = 0

exclude = set(string.punctuation)  # This strips all punctuation from the user's reply.

movingOn = [" ", " ", "Okay, I am gathering my thoughts, I can feel your fortune becoming clearer.",
            "Hmm I sense your future clouding. We shall discuss something else.",
            "We shall move on. To another topic",
            "Lets move on to another topic shall we."]