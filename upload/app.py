import os, docx2txt, sqlite3, re, io, sys, pdfminer.high_level
from flask import Flask, render_template, request, session, redirect, url_for, g

__author__ = 'artem'

app = Flask(__name__)
app.secret_key = os.urandom(24)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def getAdmin():
	conn = sqlite3.connect('login.db')
	c = conn.cursor()
	c.execute("SELECT login, password FROM users")
	admin = c.fetchall()
	conn.commit()
	c.close()
	conn.close()
	return admin
	
def uploadToDb(text):
	conn = sqlite3.connect('login.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT)")
	c.execute("CREATE TABLE IF NOT EXISTS labs(id INTEGER PRIMARY KEY AUTOINCREMENT, lab_text TEXT)")

	c.execute(f"INSERT INTO labs(content) VALUES ('{text}')")
	conn.commit()
	c.close()
	conn.close()

def replaceAll(text):
	text = text.lower();
	all = ['_','>','<','/','|','\\','+','=',':',';','.',',','!','?','//','(',')','–','-','\n']
	for i in all:
		text = text.replace( i , ' ')
	
	text = re.sub(r'\s+', ' ', text)
	return text
		

def normalize(text):		
	text = replaceAll(text)
	
	result = []
	for char in text:
		if char.isalnum():
			result.append(char)
		elif char.isspace() and (not result or not result[-1].isspace()):
			result.append(' ')
			result.append(char)
	
	text = ''.join(result)
	text = text.split(' ')

	result = []
	for i in text:
		if len(i) > 1:
			result.append(i)
	
	text = ' '.join(result)
	
	return text

@app.route('/', methods = ['POST', 'GET'])
def index():
	if g.user:
		return render_template('upload.html')
		
	if request.method == 'POST':
		session.pop('user', None)
		
		admin = getAdmin()
		
		if request.form['username'] == 'joke':
			return render_template('joke.html')
			
		if request.form['password'] == admin[0][1] and request.form['username'] == admin[0][0]:
			session['user'] = request.form['username']
			return render_template('upload.html')


	return render_template('login.html')	


@app.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']	

		
@app.route('/upload', methods=['POST', 'GET'])
def upload():
	if g.user:
		target = os.path.join(APP_ROOT, 'downloads/')
		print(target)
		
		if not os.path.isdir(target):
			os.mkdir(target)
			
		for file in request.files.getlist("file"):
			print('******************')
			ex = str(file.filename)
			ex = ex[-4:]
			if ex == 'docx':
				filename = 'file.docx'
			elif ex == '.pdf':
				filename = 'file.pdf'
			
			destination = "/".join([target, filename])
			print(destination)
			file.save(destination)
			
			if ex == 'docx':
				text = docx2txt.process('../upload/downloads/file.docx')
			
			if ex == '.pdf':
				orig_stdout = sys.stdout
				sys.stdout = open('somefile.txt', 'w') 
				with open('../upload/downloads/file.pdf', 'rb') as file:
					pdfminer.high_level.extract_text_to_fp(file, sys.stdout)
				sys.stdout.close()
				sys.stdout	= orig_stdout
				text = open('somefile.txt', 'r') 
				text = text.read()
				
			text = normalize(text)
			uploadToDb(text)
		
			return render_template("complete.html", text = text)	

	return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.run(port=6317, debug=True)