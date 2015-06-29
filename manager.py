#encoding:utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html')

def login():
	return render_template('login.html')
	

if __name__ == '__main__':
	app.run()