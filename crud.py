from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('crud.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"POST: Hello, {name}!"
    else:
        name = request.args.get('name')
        return f"GET: Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
