import sys, os
from flask import Flask, render_template

sys.path.append(os.environ["HOME"] + "/puma/lib")
import puma
p = puma.Puma()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/instances/')
def instances():
    return render_template('instances.html', p=p)

if __name__ == '__main__':
    app.run()

