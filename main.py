from spreadsheet import *
from dataclasses import dataclass
from operator import itemgetter
import eel


@dataclass
class User:
    fname: str
    lname: str
    role: str
    sports: str
    hiking: str
    fashion: str 
    gaming: str
    singing: str
    dancing: str
    makeup: str
    religion_faith: str
    traveling: str
    thrifting: str
    photography: str
    concerts: str
    leadership: str
    volunteering: str
    staying_at_home: str
    foodie: str
    memes: str
    cooking_baking: str 
    family_time: str
    playing_instruments: str
    vlogging_making_videos: str
    working_out: str

#TAKES EACH VALUE OF THE DICTIONARY AND PUTS IT INTO A LIST
PBig = []
PLittle = []   
for i in range(len(interests)):                                             #Goes through each dictionary in the list 
    person = User( *([value for key, value in interests[i].items()][1:]))   #Takes each dictionary and takes the value and puts into each object named person
    if person.role == "Big":                                                #Categorize each user into a little or big list
        PBig.append(person)
    elif person.role == "Little":
        PLittle.append(person)


#FUNCTION TO ADD POINTS BASED ON LITTLE AND BIG INPUT (REFER TO POINT SYSTEM)
def eachScoreCompatibility(littleInput, bigInput):
    points = 0
    if littleInput == "Love" and bigInput == "Love":
        points += 30
    elif littleInput == "Love" and bigInput == "Like":
        points += 20
    elif littleInput == "Love" and bigInput == "Want to get into":
        points += 10
    elif littleInput == "Like" and bigInput == "Love":
        points += 20
    elif littleInput == "Like" and bigInput == "Like":
        points += 20
    elif littleInput == "Like" and bigInput == "Want to get into":
        points += 10
    elif littleInput == "Want to get into" and bigInput == "Love":
        points += 40
    elif littleInput == "Want to get into" and bigInput == "Like":
        points += 30
    elif littleInput == "Want to get into" and bigInput == "Want to get into":
        points += 30
    elif littleInput =="N/A" and bigInput =="N/A":
        points += 30
    elif littleInput =="N/A" and bigInput =="Love":
        points += 2
    elif littleInput =="N/A" and bigInput =="Like":
        points += 4
    elif littleInput =="N/A" and bigInput =="Want to get into":
        points += 8
    
    return points
   

#TEST eachScoreComptability Function     
#print(eachScoreCompatibility(PLittle[0].sports, PBig[0].sports))
 

#FUNCTION TO FIND COMPATIBILITY SCORE BETWEEN A LITTLE AND BIG
def ScoreCompatibility(little,big):
    totalScore = 0
    totalScore += eachScoreCompatibility(little.sports, big.sports)
    totalScore += eachScoreCompatibility(little.hiking, big.hiking)
    totalScore += eachScoreCompatibility(little.fashion, big.fashion)
    totalScore += eachScoreCompatibility(little.gaming, big.gaming)
    totalScore += eachScoreCompatibility(little.singing, big.singing)
    totalScore += eachScoreCompatibility(little.dancing, big.dancing)
    totalScore += eachScoreCompatibility(little.makeup, big.makeup)
    totalScore += eachScoreCompatibility(little.religion_faith, big.religion_faith)
    totalScore += eachScoreCompatibility(little.traveling, big.traveling)
    totalScore += eachScoreCompatibility(little.thrifting, big.thrifting)
    totalScore += eachScoreCompatibility(little.photography, big.photography)
    totalScore += eachScoreCompatibility(little.concerts, big.concerts)
    totalScore += eachScoreCompatibility(little.leadership, big.leadership)
    totalScore += eachScoreCompatibility(little.volunteering, big.volunteering)
    totalScore += eachScoreCompatibility(little.staying_at_home, big.staying_at_home)
    totalScore += eachScoreCompatibility(little.foodie, big.foodie)
    totalScore += eachScoreCompatibility(little.memes, big.memes)
    totalScore += eachScoreCompatibility(little.cooking_baking, big.cooking_baking)
    totalScore += eachScoreCompatibility(little.family_time, big.family_time)
    totalScore += eachScoreCompatibility(little.playing_instruments, big.playing_instruments)
    totalScore += eachScoreCompatibility(little.vlogging_making_videos, big.vlogging_making_videos)
    totalScore += eachScoreCompatibility(little.working_out, big.working_out)
    return totalScore

def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    count = [0]*(10)

    for i in range(0, n):
        index = (9-arr[i][1]//exp1)
        count[ (index)%10 ] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = (9-arr[i][1]//exp1)
        output[ count[ (index)%10 ] -1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr, key=itemgetter(1))

    exp = 1
    while max1[1]/exp > 0:
        countingSort(arr, exp)
        exp *= 10

def compatPerc(ScoreCompatibility):
    return ((ScoreCompatibility/88) * 100)

#CREATING A NEW LIST FOR RANKED SORTING
rankedLittle = [[0 for x in range(2)] for y in range(len(PLittle))]

for i in range(0, len(PLittle)):            # Inputs little's name for first index
    rankedLittle[i][0] = PLittle[i].fname
#print(rankedLittle)

#CREATING A NEW LIST FOR RANKING BIGS
for i in range(0, len(PLittle)):
    rankedBigs = []                 # Used to store bigs with name and score
    for x in range(0, len(PBig)):
        percent = compatPerc(ScoreCompatibility(PLittle[i], PBig[x]))
        big = (PBig[x].fname + ' ' + PBig[x].lname, int(percent)) # Creating big pairs with their score
        rankedBigs.append(big)
    radixSort(rankedBigs)
    rankedLittle[i][1] = rankedBigs # Inserts list of unsorted Bigs into rankedLittle list


# TEMP CONSOLE GUI
z = -1

def littlePrint(z):
    print('------------------------------------------------------------')
    print("Little: " + PLittle[z-1].fname + ' ' + PLittle[z-1].lname)
    for i in range(0, 5):
        print(rankedLittle[z-1][1][i])
    print('------------------------------------------------------------')

while (True):
    print('==== Enter the corresponding number to view the top 5 bigs for each little ====')

    for i in range(len(PLittle)):
        print(str(i+1) +'. ' + PLittle[i].fname + ' ' + PLittle[i].lname)
    print('0. Exit program')
    z = int(input())
    if (z < 1):
        break
    elif (z > len(PLittle)):
        break
    else:
        littlePrint(z)
