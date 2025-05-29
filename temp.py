from flask import Flask,render_template


app = Flask(__name__)


@app.route("/templates")

def hello():

    return render_template('index.html')


#run custom flask app
# flask --app filename.py run