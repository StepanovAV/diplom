# n = int(input("Enter n"))
# buf = 1
# count_row = 0
# count_col = n*2-1
# f = open('word.docx', 'w')

# while count_row < n:
        # while count_col >= buf:
            # print(' '*((count_col - buf)//2), '*'*buf)
            # f.write(' '*((count_col - buf)//2)+ '*'*buf +'\n')
            # buf+=2
        # count_row +=1
# f.close()
# n = int(input("Enter n"))
##import docx2txt
##text = docx2txt.process('C:/Users/Artem/Desktop/PZ.do
import docx2txt
text = docx2txt.process('C:/Users/Artem/Desktop/PZ.docx')
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
