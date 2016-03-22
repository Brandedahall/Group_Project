
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
questionsJob = ["Do you enjoy your job?", "Do you feel fulfilled with your work?",
                "Hmm, but what are your future career plans?"]
questionsFam = ["Are you close with your family?","That is comforting to know, Do you have a fond family memory, My I ask what it is?",
                "I see, Do you wish you could see your family more?"]
questionsLove = ["Do you believe you have found your soul mate?",
"Are you satisfied with amount of affection you get from your loved ones?",
"Do you feel like you need to surround yourself with more positive energy in your life"]
questionsFri = ["Do you feel like you have made close bonds with others you can call friends?",
"Would you say you have always been able to connect with people easily?",
"It is important to surround yourself with people you have formed bonds with, Can you say that you do?"]

# List of keywords user has used
userKeywordsJob = []
userKeywordsFam = []
userKeywordsLove = []
userKeywordsFri = []
# Fais saved keywords
keywordsJob = ["teacher", "tv presenter", "unemployed", "student"]
keywordsFamily = ["mom", "dad", "brother", "sister"]
keywordsLove = ["wife", "husband", "girlfriend", "boyfriend"]
keywordsFriends = ["best friend", "close", "friend", "friends"]
keywordsHobbies = []
keywordsIssues = []
keywordsAchievements = []
# counts used to keep track with the number of keywords in users response. Once used to change
# the conversation the counts are assigned negative numbers to asure they do not trigger again
countJob = 0
countFamily = 0
countLove = 0
countFriends = 0

firstPart = ""
secondPart = ""
thirdPart = ""
fourthPart = ""

tempNextTopic = ""
topic = 0
topics = ["Job", "Family", "Love", "Friends", "Hobbies", "Issues", "Achievements"]
