from spreadsheet import *
from operator import itemgetter
from calculateScore import*
from data import*
from flask import Flask, render_template, url_for

SeperateObj()           #CREATES DATA CLASS AND OBJECT FOR EACH USER THEN SEPERATES INTO LITTLE AND BIG LIST         

app = Flask(__name__)

#USED IN RADIX SORT
#CREATES THE BUCKETS NEEDED FOR RADIX SORT AND REVERSE BUCKET ORDER
#CAUSES THE HIGHEST NUMBER TO BE SHOWN FIRST RATHER THAN THE OTHER WAY
def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)

    count = [0]*(10)

    for i in range(0, n):
        index = (9-arr[i][1]//exp1)     #9-ARR[I] NEEDED TO REVERSE BUCKET ORDER
        count[ (index)%10 ] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = (9-arr[i][1]//exp1)     #9-ARR[I] NEEDED TO REVERSE BUCKET ORDER
        output[ count[ (index)%10 ] -1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]


#RADIX SORT USED TO SORT THE BIGS BASED ON COMPATIBILITY SCORE
def radixSort(arr):
    max1 = max(arr, key=itemgetter(1))

    exp = 1
    while max1[1]/exp > 0:
        countingSort(arr, exp)
        exp *= 10

#CREATES A PERCENTAGE SCORE
def compatPerc(ScoreCompatibility):
    return ((ScoreCompatibility/880) * 100)

#CREATING A NEW LIST FOR RANKED SORTING
rankedLittle = [[0 for x in range(2)] for y in range(len(PLittle))]
for i in range(0, len(PLittle)):            # Inputs little's name for first index
    rankedLittle[i][0] = PLittle[i].fname + ' ' + PLittle[i].lname

#CREATING A NEW LIST FOR RANKING BIGS
for i in range(0, len(PLittle)):
    rankedBigs = []                 # Used to store bigs with name and score
    for x in range(0, len(PBig)):
        percent = compatPerc(ScoreCompatibility(PLittle[i], PBig[x]))
        big = (PBig[x].fname + ' ' + PBig[x].lname, int(percent)) # Creating big pairs with their score
        rankedBigs.append(big)
    radixSort(rankedBigs)
    rankedLittle[i][1] = rankedBigs # Inserts list of unsorted Bigs into rankedLittle list

#print(rankedBigs)



# BELOW IS USED FOR THE WEB GUI (FLASK)

#HOMEPAGE
@app.route("/")
def home():
    return render_template('home.html')

#LIST OF LITTLES PAGE
@app.route("/littles")
def littles():
    return render_template('littles.html', littles=rankedLittle, title="Little List")

#LIST OF BIGS PAGE
@app.route("/bigs")
def bigs():
    return render_template('bigs.html', bigs=PBig, title="Bigs List")

#AUTOGENERATING TOP 5 BIGS PAGE FOR SELECTED LITTLES
@app.route("/littles/<little>")
def littleMatch(little):
    return render_template('littleMatch.html', littles=rankedLittle, title=little, selected=little)


#REQUIRED TO START FLASK THROUGH PYTHON BY JUST RUNNING THE MAIN FILE
if __name__ == '__main__':
    app.run(debug=True)
