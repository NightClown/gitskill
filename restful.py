from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')

def api_root():
    return 'Welcome'

@app.route('/articles')

def api_articles():
    return 'List of' + url_for('api_articles')

@app.route('/articles/<articleid>')

def api_article(ariticleid):
    return 'You are reading' + ariticleid

if __name__ == '__main__':
    app.run()