import requests
from lxml import html
import operator

###PNG FINDER###

print("")
print(str(requests.get("http://www.banno.com").content).count('.png')) #3 : A simple count, one could do an xpath for all the images, however this is the most "slick"
print("pngs found\n")


###TWITTER HANDLE###

r = requests.get("https://banno.com/")
dasbaum = html.fromstring(r.content.decode("utf-8"))
twitterHandle = dasbaum.xpath("//meta[contains(@content, '@')]/@content")
print(twitterHandle) #4 : An XPATH - By simply identifying the '@' sign, the twitter handle can be found
print("")


### # OF "FINANCIAL INSTITUTION" ###

print(str(requests.get("http://www.banno.com").content).count('financial institution')) #5
print("results for the term: 'financial institution'\n")


### # OF PRODUCTS ###

print(str(requests.get("http://www.banno.com").content).count('h3 class')) #1
print("results per the h3 tag, determined to be best fit for the identification of products\n")


### TOP THREE ALPHANUMERIC CHARACTERS ###

def topThree():

    letters = list(r.content.decode("utf-8"))
    holder = {}

    for letter in letters:
        if letter not in holder.keys():
            holder.update({letter: 1})
        else:
            holder[letter] +=  1
    #print(holder)

    try:
        del holder[' ']
    except KeyError:
        pass

    topThree = dict(sorted(holder.items(), key=operator.itemgetter(1), reverse=True)[:3])
    print(topThree) #2
    print("First three occuring alphanumeric characters appearing in the HTML\n")

topThree()
