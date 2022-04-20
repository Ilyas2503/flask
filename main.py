from flask import Flask, render_template

app = Flask(__name__)

@app.route('/say_hello')
def say():
    return render_template('index.html')