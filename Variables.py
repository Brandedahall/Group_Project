UserName = ""
Name = ""
TrueName = []
# The user's name is stored here.

QuestionAnswer = ""
Answer = ""
# The user's answers will be stored here.

Emotion = 0

FAIanswer = ""
numberOfChats = 3

Word = []
Index = 0

keywords = []

keywords_Job = []
keywords_Family = []
keywords_Love = []
keywords_Friends = []
keywords_Hobbies = []
keywords_Issues = []
keywords_Achievements = []

firstpart = ""
secondpart = ""
thirdpart = ""
fourthpart = ""

keywordsUsed = []


baseline = 0
Tempnexttopic = ""
Topic = 0
Topics = ["Baseline", "Job", "Family", "Love", "Friends", "Hobbies", "Issues", "Achievements"]
# We want some variables relating to a 3d graph here. The graph will need to store the plotted points for each question.

Open = open("AFINN-111.txt", "r")
Words = Open.read()
Words = Words.replace(" ", " ")
Words = Words.split(" ")
