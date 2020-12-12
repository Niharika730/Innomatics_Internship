
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/info')
def Info():
    return render_template('Info.html')



if(__name__ == '__main__'):
    app.run(debug = True)
