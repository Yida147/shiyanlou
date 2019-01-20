from flask import Flask
from flask import url_for
from flask import redirect
from flask import request
from flask import session
from flask import render_template
from flask import make_response
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
        return render_template('user_index.html', username=username)
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username', username)
    print('User-Agent:', request.headers.get('User-Agent'))
    print('time:',request.args.get('time'))
    print('q:',request.args.get('q'))
    print('Q:',request.args.getlist('Q'))
    return resp

@app.errorhandler(404)
def not_fond(error):
    return  render_template('404.html') , 404

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.route('/test')
def test():
	print(url_for('index'))
	print(url_for('user_index',username='shiyanlou'))
	print(url_for('show_post',post_id=1,_external=True))
	print(url_for('show_post',post_id=2,q='python 03'))
	print(url_for('show_post',post_id=2,q='keyi'))
	print(url_for('show_post',post_id=2,_anchor='a'))
	return 'test'

@app.route('/<username>')
def hello(username):
	if username == 'shixiaolou':
		return 'hello {}'.format(username)
	else:
		return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
    print('method:', request.method)
    print('name:', request.form['name'])
    print('password:', request.form.get('password'))
    print('hobbies:',request.form.getlist('hobbies'))
    print('age:',request.form.get('age', default=18))
    return ' register successed! '

@app.route('/set_session')
def set_session():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    session['username'] = 'shixiaolou'
    return  'chenggongshezhi session'

@app.route('/get_session')
def get_session():
    value = session.get('username')
    return 'huoqude session zhiwei{}'.format(value)

@app.route('/del_session')
def del_session():
    value = session.pop('username')
    return 'chenggongyichu session, qizhiwei{}'.format(value)


if __name__ == 'main':
    app.run()
