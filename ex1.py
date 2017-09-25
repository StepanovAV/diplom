import sqlite3
import docx2txt

text = docx2txt.process('C:/Users/Àðòåì/Desktop/curva.docx')
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
text = text.replace(" Ð° ", ' ')
text = text.replace(" Ñƒ ", ' ')
text = text.replace(" Ñ– ", ' ')
text = text.replace(" Ð² ", ' ')
text = text.replace(" Ð· ", ' ')
text = text.replace(" Ð¶ ", ' ')
text = text.replace(" Ñ” ", ' ')
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
conn = sqlite3.connect('login.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS labs(id INTEGER PRIMARY KEY AUTOINCREMENT, lab_text TEXT)")

def data_entry():

		c.execute("INSERT INTO users(login, password) VALUES('admin2', 2222)")
		c.execute(f"INSERT INTO labs(content) VALUES ('{text}')")
		conn.commit()
		c.close()
		conn.close()
    
create_table()
data_entry()

