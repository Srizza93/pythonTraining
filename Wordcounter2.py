'''import operator
import sys
file = open(sys.argv[1], "r")
text = file.read()
file.close()
words = {}
for word in text.split():
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1
sortedwords = sorted(words.items(), key= operator.itemgetter(1), reverse=True)

file = open(sys.argv[1][:-4] + "-count" + sys.argv[1][-4:], "w")
file.write("Total words - {}\nUnique words - {}\n\n".format(len(text.split()), len(sortedwords)))
for wordinfo in sortedwords:
    file.write("{} - {}\n".format(wordinfo[0], wordinfo[1]))


file.close()
'''
