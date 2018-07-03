# question 1
f 1= open("excerpt.txt")
last = f.readlines()
f.close()
n = input("Enter number of last lines to be read: ")
c = n
print "The last lines are: "
while c > 0:
print last[-c]
c-=

#question2
import re
import string
frequency = {}
results = []
f = open("excerpt.txt", 'r')
words = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
for word in match_pattern:
count = frequency.get(word,0)
frequency[word] = count + 1
#you can directly print the dictionary or save it in list of tuples and print it in
#ascending order
frequency_list = frequency.keys()
for word in frequency_list:
tuple = (word, frequency[word])
results.append(tuple)
byFreq=sorted(results, key=lambda word: word[1], reverse = True)
for (word, freq) in byFreq:
print word, freq

#question3
with open ( "excerpt.txt" ) as f:
with open ( "out.txt" , "w" ) as f1:
for line in f:
f1. write( line )


# question 4

with open ( “excerpt.txt” ) as fh1 , open ( “out.txt” ) as fh2 :
for line1 , line2 in zip ( fh1 , fh2 ):
# line1 from abc.txt, line2 from test.txtg
print ( line1 + line2 )

#question 5
import random
with open("random.txt", "w") as f:
for i in range(int(input('How many random numbers? '))):
line = str(random.randint(1, 100))
f.writelines(line + '\n')
print(line)
with open("random.txt") as f1 ,open("random1.txt", "w") as f2:
lines = f1.read().splitlines()
lines.sort()
for l in lines:
f2.write(str(l) + '\n')

