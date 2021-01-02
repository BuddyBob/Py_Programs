from flask import Flask, render_template, Response, request, redirect, url_for
import string
import random
app = Flask(__name__)
#background process happening without any refreshing
ButtonPressed = 0        
@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        return render_template("button.html", ButtonPressed = ButtonPressed)
        ButtonPressed += 1
    return render_template("button.html", ButtonPressed = ButtonPressed)
if __name__ == "__main__":
    app.run(debug = True)
