f = open('flowers_of_evil.txt', 'r')
outfile = open('vb1.txt','w')

def wordCount(file):
    s = file.read()
    file.close()

    dict = {}
    delimiters = ['\n', ' ', ',', '.', '?', '!', ':', '(', '\'', '"']

    wordList = s.split()
    for delimiter in delimiters:
        new_words = []
        for w in wordList:
            new_words += w.split(delimiter)
        wordList = new_words

    for word in wordList:
        times = wordList.count(word)
        temp = {word: times}
        dict.update(temp)
    return dict

def writeTable(dict):
    for i, j in dict.items():
        outfile.write("{:<15} {:^4}\n".format(str(i),str(j)))
    return

testDict = wordCount(f)
writeTable(testDict)

for key in testDict:
    print(key, testDict[key])

print(testDict['a'])
print(testDict['I'])
