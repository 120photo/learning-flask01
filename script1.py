from flask import Flask, render_template
from random import randint
import datetime

app = Flask(__name__)

def the_number():
    target = randint(1,100)
    return str(target)

def get_date():
    now = datetime.datetime.now()
    return str("{} {}, {} - {}:{}::{}".format(now.strftime("%B"),now.day,now.year, now.time().hour, now.time().minute, now.time().second))

@app.route('/')
def home():
    num = the_number()
    date = get_date()
    return render_template("home.html", num = num, date = date)

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
