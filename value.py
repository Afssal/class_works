from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def data_pass():

    return render_template('page.html',item_name='Phone')

ele = [2,4,6,8,10]

@app.route('/for')

def loop():

    return render_template('looping.html',elements=ele)