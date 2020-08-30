from flask import Flask, render_template, Response, request, redirect, url_for
import string
import random
app = Flask(__name__)
@app.route('/')
@app.route('/json')
def json():
    return render_template('json.html',password)

#background process happening without any refreshing
@app.route('/pwdGen')
def get_password():
    total = False
    while total == False:
        letters_Count = 0
        numbers_Count = 0
        spec_Count = 0
        password_characters = string.digits + string.ascii_letters + '!@#$%&*'
        password = ''.join(random.choice(password_characters)for i in range(8))
        for i in password:
            if i in 'abcdefghijklmnopqrstuvlxyz':
                letters_Count = 1
            if i in string.digits:
                numbers_Count = 1
            if i in '!@#$%&*':
                spec_Count = 1
            if spec_Count == 1 and numbers_Count == 1 and spec_Count == 1:
                total = True
    return password
if __name__ == "__main__":
    app.run(debug = True)
