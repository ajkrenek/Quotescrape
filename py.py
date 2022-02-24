import re

inFile = open("quotescrape.txt","r")
text = inFile.read()
quotes = re.findall(r'“(.*?)”', text)
outFile = open("example.txt", "a")
with outFile as f:
    for line in quotes:
        f.write(line)
        f.write('\n')
#print(quotes)

inFile.close()
outFile.close()
