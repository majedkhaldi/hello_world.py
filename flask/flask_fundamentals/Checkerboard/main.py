from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/')                           
def check():
    return render_template('index.html', rows = 4, cols = 4, color1 = "aqua", color2 = "#ce6545")  

@app.route('/<int:x>')                           
def check4(x):
    return render_template('index.html', rows = int(x/2), cols = 4, color1 = "aqua", color2 = "#ce6545")  

@app.route('/<int:x>/<int:y>')                           
def checkxy(x,y):
    return render_template('index.html', rows = int(x/2) , cols = int(y/2), color1 = "aqua", color2 = "#ce6545")  


@app.route('/<int:x>/<int:y>/<c>/<cl>')                           
def checkxycolors(x,y,c,cl):
    return render_template('index.html', rows = int(x/2) , cols = int(y/2), color1 = c, color2 = cl) 


if __name__=="__main__":
    app.run(debug=True)                   