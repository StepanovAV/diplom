import os, docx2txt
from flask import Flask, render_template, request

__author__ = 'artem'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	
@app.route('/')
def index():
	return render_template('upload.html')	

@app.route('/upload', methods=['POST'])
def upload():
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
		text = docx2txt.process('C:/Users/Артем/Desktop/upload/downloads/file.docx')
		text = text.lower();
		text = text.replace('\n', ' ')
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
		print(text)
		print(len(text))
	
	return render_template("complete.html", text = text)	
	
if __name__ == '__main__':
	app.run(port=7777, debug=True)