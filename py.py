import re

inFile = open("quotescrape.txt","r")
text = inFile.read()
#inFile.close()
#pattern1 = “([^"]*)”
#pattern2 = "([^"]*)"
quotes = re.findall(r'''
“(.*?)”



''', text, re.VERBOSE)
outFile = open("example.txt", "a")
with outFile as f:
    for line in quotes:
        f.write(line)
        f.write('\n')
#print(quotes)



inFile.close()
outFile.close()
