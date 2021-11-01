# function to count the number of words in term-paper.tex
f  = open("term-paper.tex", 'r')
# read the file
text = f.read()
# split the text into words
words = text.split()
# count the number of words
count = len(words)
# print the result
print("The number of words in term-paper.tex is:", count)
# close the file
f.close()

