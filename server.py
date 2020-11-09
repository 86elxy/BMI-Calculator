import flask
from flask import render_template
from flask import request
app = flask.Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/calcbmi')
def calcbmi():
    BMI = float(request.args['weight'])/float(request.args['height'])**2
    result = request.args['name']+'\'s BMI is '+str(BMI)
    return result

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('custom404.html')

app.run(debug=True)
