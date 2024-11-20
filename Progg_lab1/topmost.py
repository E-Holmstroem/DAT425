import wordfreq as wf
import sys
import urllib.request

def main():
    stop = sys.argv[1]
    text = sys.argv[2]
    antal = sys.argv[3]
    if text[0:7] == "http://" or text[0:8] == "https://": #If the text source is from the web, with a more specific if-statement.
        response = urllib.request.urlopen(text)
        txtF = response.read().decode("utf8").splitlines()
    else:
        txtF = open(text, encoding="utf-8")
    stopF = open(stop, encoding="utf-8")
    result = wf.printTopMost(wf.countWords(txtF, stopF),antal)
    stopF.close()
    if text[0:7] != "http://" and text[0:8] != "https://":
        txtF.close()
    return result
main()