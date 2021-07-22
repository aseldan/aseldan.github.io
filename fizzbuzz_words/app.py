from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    title="Welcome to the Fizzbuzz challenge"
    return render_template('welcome.html', title=title)

@app.route("/fizzbuzz/<int:m>")
def fizzbuzz(m):
    l=[]
    i=1
    while i<=m:
        l.append(i)
        i += 1
    title="Results"
    return render_template('fizzbuzz.html', title=title, numbers=l)

@app.route("/words/<string:word>")
def anagrams(word):
    w=word.upper()
    f=open('words.txt')
    words=f.read().splitlines()
    anagrams=[]
    for i in words:
        if sorted(i) == sorted(w):
            anagrams.append(i)
    title="Anagrams"
    return render_template('words.html', title=title, anagrams=anagrams)

def startwith(word, prefix):
    if len(prefix)>len(word):
        return False
    for i in range(0, len(prefix)): ##len returns a number (int) i need to use range in order to compare from spot zero to the max length of the word 
        if prefix[i]==word[i]:
            pass  
        else:
            return False     
    return True 

@app.route("/dictionary/<string:prefix>")
def dictionary(prefix):
    f=open('words.txt')
    words=f.read().splitlines()
    dictionary={}
    alphabet= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numWords=0

    for letter in alphabet:   
        newprefix=prefix+letter 
        if newprefix not in dictionary:
            dictionary[newprefix]=[]
        for word in words:
            if startwith(word, newprefix):
                dictionary[newprefix].append(word) 
                numWords=numWords+1
    
    title="Dictionary"
    #print(dictionary)
    return render_template('dictionary.html', title=title, dictionary=dictionary, prefix=prefix, count=numWords)

@app.route("/dictionary/")
def landing():
    f=open('words.txt')
    words=f.read().splitlines()
    dictionary={}
    alphabet= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numWords=0

    for letter in alphabet:   
        if letter not in dictionary:
            dictionary[letter]=[]
        for word in words:
            if startwith(word, letter):
                dictionary[letter].append(word) 
                numWords=numWords+1

    
    title="Dictionary"
    subtitle='choose a letter/prefix'
    return render_template('dictionary.html', title=title, dictionary=dictionary, prefix='', count=numWords, subtitle=subtitle)