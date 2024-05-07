from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'majed' 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['username'] = request.form['name']
    session['dojolocation'] = request.form['location']
    session['favlang'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect ('/result')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug = True)
