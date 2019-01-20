from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    course = {
        'python': 'lou+ python',
        'java': 'java base',
        'bigdata': 'spark sql',
        'teacher': 'shixiaolou',
        'is_unique': False,
        'has_tag': True,
        'tags': ['c', 'c++', 'docker']
    }
    return render_template('index.html',course=course)

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html',username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/courses/<name>')
def courses(name):
    return render_template('courses.html',coursename=name)

@app.route('/test')
def test():
	print(url_for('courses',name='java'))
	return redirect(url_for('index'))

@app.route('/httptest',methods=['GET','POST'])
def httptest():
    if request.method == 'GET':
        print('t: ', request.args.get('t'))
        print('t: ', request.args['t'])
        print('q: ', request.args.get('q'))
        return 'It is a get request! '
    elif request.method == 'POST':
        print('Q: ', request.form.getlist('Q'))
        return 'It is a post request! '
    else:
        return 'Method error!'

if __name__ == 'main':
    app.run()
