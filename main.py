import sys, os
from flask import Flask, render_template

error=False

try:
    sys.path.append(os.environ["HOME"] + "/puma/lib")
    import puma
    p = puma.Puma()
except:
    error=True

app = Flask(__name__)

@app.route('/')
def index():
    if not error:
        return render_template("index.html")
    else:
        return "<h1>Puma isn't installed!</h1>"

@app.route('/info/')
@app.route('/info/<opt>')
def info(opt=None):
    if opt == None:
        # add template
        return "info page"

    try:
        return render_template(opt+'.html', p=p)
    except:
        return "<h1>404: Page not found</h1>"

if __name__ == '__main__':
    app.run()

