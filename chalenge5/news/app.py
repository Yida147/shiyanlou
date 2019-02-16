from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Founder123@localhost/shiyanlou'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
mongo = MongoClient('127.0.0.1', 27017).shiyanlou


class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    update_at = db.Column(db.DateTime, default=datetime.utcnow())
    create_at = db.Column(db.DateTime, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref=db.backref('categories', lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self, title, create_at, category, content):
        self.title = title
        self.create_at = create_at
        self.category = category
        self.content = content

    def __repr__(self):
        return '%s' % self.title

    def add_tag(self, tag_name):
        mongo.file.update_one({'fileId': self.id}, {'$addToSet': {'tags': tag_name}})
        return self.__file['tags']

    def remove_tag(self, tag_name):
        mongo.file.tags.update_one({'fileId': self.id}, {'$pull': tag_name})
        return self.__file['tags']

    @property
    def __file(self):
        return mongo.file.find_one({'fileId': self.id})

    @property
    def tags(self):
        return self.__file['tags']


@event.listens_for(File, 'after_insert')
def auto_create_mongodb_file(mapper, conn, file):
    mongo.file.insert_one({'fileId': file.id})


@event.listens_for(File, 'after_delete')
def auto_delete_mongodb_file(mapper, conn, file):
    mongo.file.delete_one({'fileId': file.id})


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%s' % self.name


@app.route('/')
@app.route('/files/')
def index():
    return render_template('index.html', files=File.query.all())


@app.route('/files/<int:file_id>')
def file(file_id):
    file = File.query.get_or_404(file_id)
    return render_template('file.html', file=file)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    db.create_all()
    java = Category(name='Java')
    python = Category(name='Python')
    file1 = File(title='Hello Java', create_at=datetime.utcnow(), category=java,
                 content='File Content - Java is cool!')
    file2 = File(title='Hello Python', create_at=datetime.utcnow(), category=python,
                 content='File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')
    file1.tags
