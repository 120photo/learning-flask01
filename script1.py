from flask import Flask, render_template
from random import randint

app = Flask(__name__)

def the_number():
    target = randint(1,100)
    return str(target)

@app.route('/')
def home():
    num = the_number()
    return render_template("home.html", num = num)

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
