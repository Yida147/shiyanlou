from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Founder123@localhost/shiyanlou'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)



class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    create_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('categories',lazy='dynamic'))
    content = db.Column(db.Text)
    
    def __repr__(self):
        return '%s' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __repr__(self):
        return '%s' % self.name



@app.route('/')
def index():
    return render_template('titles.html', raw_data=db.session.query(File).all())

@app.route('/files/<file_id>')
def file(file_id):
    files = db.session.query(File).all()

    def to_str(files):
        stred_files = []
        for element in files:
            element = str(element)
            stred_files.append(element)
        return stred_files

    def catch_data(file):
        id = file.id
        content = file.content
        create_time = file.create_time
        category = file.category
        raw_data = {
            "id": id,
            "content": content,
            "create_time": create_time,
            "category": category
        }
        return raw_data

    if file_id not in to_str(files):
        abort(404)
    elif file_id == to_str(files)[0]:
        raw_data = catch_data(files[0])
    else:
        raw_data = catch_data(files[1])

    return render_template('file.html', raw_data=raw_data)