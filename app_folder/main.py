from spreadsheet import *
from calculateScore import*
from data import *
from radixsort import *
from flask import Flask, render_template, url_for


SeperateObj()               #Sets up data and creates little and big list       
rankedLittle = newList()    #Radix sort

#WEB GUI (FLASK)
app = Flask(__name__)
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
