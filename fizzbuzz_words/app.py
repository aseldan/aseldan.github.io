from flask import Flask, render_template

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

