from flask import Flask, render_template
app = Flask(__name__)
@app.route("/play")
def playblue():
    return render_template("index.html", times = 3, color = "#9fc5f8")


@app.route("/play/<int:x>")
def playtimes(x):
    return render_template("index.html", times = x,color="#9fc5f8")

@app.route("/play/<int:x>/<color>")
def playtimescolor(x,color):
    return render_template("index.html", times = x, color = color)



if __name__=="__main__":
    app.run(debug=True)