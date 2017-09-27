import os, docx2txt, sqlite3
from flask import Flask, render_template, request, session, redirect, url_for, g

__author__ = 'artem'

app = Flask(__name__)
app.secret_key = os.urandom(24)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods = ['POST', 'GET'])
def index():
	if g.user:
		return render_template('upload.html')
		
	if request.method == 'POST':
		session.pop('user', None)
		
		conn = sqlite3.connect('login.db')
		c = conn.cursor()
		c.execute("SELECT login, password FROM users")
		you = c.fetchall()
		conn.commit()
		c.close()
		conn.close()
		
		if request.form['password'] == you[0][1] and request.form['username'] == you[0][0]:
			session['user'] = request.form['username']
			return redirect(url_for('upload'))


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
			print(file)
			filename = 'file.docx'
			destination = "/".join([target, filename])
			print(destination)
			file.save(destination)
			text = docx2txt.process('C:/xampp/htdocs/Diplom/upload/downloads/file.docx')
			text = text.lower();
			text = text.replace('{', ' ')
			text = text.replace('}', ' ')
			text = text.replace('[', ' ')
			text = text.replace(']', ' ')
			text = text.replace('\n',' ')
			text = text.replace(",", ' ')
			text = text.replace(".", ' ')
			text = text.replace("(", ' ')
			text = text.replace(")", ' ')
			text = text.replace(';', ' ')
			text = text.replace(":", ' ')
			text = text.replace('\"', '')
			text = text.replace("-", ' ')
			text = text.replace("_", ' ')
			text = text.replace("'", '')
			text = text.replace("%", '')
			text = text.replace(" а ", ' ')
			text = text.replace(" у ", ' ')
			text = text.replace(" і ", ' ')
			text = text.replace(" в ", ' ')
			text = text.replace(" з ", ' ')
			text = text.replace(" ж ", ' ')
			text = text.replace(" є ", ' ')
			text = text.replace(' 1 ', ' ')
			text = text.replace(' 2 ', ' ')
			text = text.replace(' 3 ', ' ')
			text = text.replace(' 4 ', ' ')
			text = text.replace(' 5 ', ' ')
			text = text.replace(' 6 ', ' ')
			text = text.replace(' 7 ', ' ')
			text = text.replace(' 8 ', ' ')
			text = text.replace(' 9 ', ' ')
			text = text.replace(' 0 ', ' ')
			text = text.replace("		", ' ')
			text = text.replace("	", ' ')
			text = text.replace("  ", ' ')
			text = text.replace("  ", ' ')
			text = text.replace("  ", ' ')
			text = text.split(' ')
			
			buf = 0
			text2 =[]
			while buf < len(text):
				if len(text[buf]) > 2:
					text2.append(text[buf])
				buf +=1
			buf = 0
			text = ''
			while buf < len(text2):
				text+= " "+ text2[buf]
				buf+=1

			f = open('word.txt', 'w')
			f.write(text)
			f.close()
			print("file uploaded!")
			
			conn = sqlite3.connect('login.db')
			c = conn.cursor()
			
			def create_table():
					c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT)")
					c.execute("CREATE TABLE IF NOT EXISTS labs(id INTEGER PRIMARY KEY AUTOINCREMENT, lab_text TEXT)")

			def data_entry():
					c.execute(f"INSERT INTO labs(content) VALUES ('{text}')")
					conn.commit()
					c.close()
					conn.close()
				
			create_table()
			data_entry()
		
			return render_template("complete.html", text = text)	

	return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.run(port=7777, debug=True)