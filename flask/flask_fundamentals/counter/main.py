from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'majed'

@app.route('/')
def count():
    if 'counter'and 'refreshs' in session:
        session['counter'] +=1
        session['refreshs'] +=1
    else:
        session['counter'] = 1
        session['refreshs'] =1
    return render_template("index.html")


@app.route('/destroy_session', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/process', methods = ['POST'])
def addtwo():
    session['counter'] +=1
    return redirect('/')

@app.route('/incrementbyuser', methods = ['POST'])
def addbyuser():
    numbyuser = int(request.form['inputuser'])
    session['counter'] += (numbyuser - 1)
    return redirect ('/')




if __name__ == "__main__":
    app.run(debug=True)
