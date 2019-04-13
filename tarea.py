
from flask import Flask, render_template, redirect, url_for
import requests
import json
import unicodedata
import wikipedia



app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/search/<name>')
def search(name):
    info = requests.get('https://www.wikipedia.org/'+name)
    info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    info = json.loads(info)
    return render_template('home.html', info=info)


@app.route('/hello/<name>')
def hello(name):
    info = requests.get('home.html'+name)
    return info.text



if __name__ == '__main__':
    app.run(debug=True)
    pass