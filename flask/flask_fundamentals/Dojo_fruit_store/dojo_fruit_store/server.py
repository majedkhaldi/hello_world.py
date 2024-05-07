from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    numofstrawberries = int(request.form['strawberry'])
    numofberries = int(request.form['raspberry'])
    numofapples = int(request.form['apple'])
    fname = request.form['first_name']
    lname = request.form['last_name']
    snumber = request.form['student_id']
    return render_template("checkout.html", numofstrawberries = numofstrawberries, numofberries = numofberries, numofapples = numofapples, fname = fname, lname = lname, snumber = snumber, total = numofapples+numofberries+numofstrawberries)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    