from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie', methods= ['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('read_cookie.html'))
        resp.set_cookie('userID', user)
        return resp
    else:
        return 'error'

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1> Welcome, ' + name + '</h1>'

if __name__ == 'main':
    app.run()