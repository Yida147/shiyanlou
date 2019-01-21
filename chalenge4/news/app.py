import JSON
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	

@app.route('/files/<filename>')
def file(filename):
	