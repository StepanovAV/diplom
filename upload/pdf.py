import sys
import pdfminer.high_level

orig_stdout = sys.stdout

sys.stdout = open('somefile.txt', 'w') 

with open('file.pdf', 'rb') as file:
	pdfminer.high_level.extract_text_to_fp(file, sys.stdout)

sys.stdout.close()

sys.stdout	= orig_stdout

text = open('somefile.txt', 'r') 

text = text.read()
print (text) 