from flask import Flask, request
import joke_data
import random

server_port = 5000
app = Flask(__name__)

@app.route('/joke-api')

def joke():
    language = request.args.get('language', 'de')
    if(language not in joke_data.joke):
        language = 'de'
    return random.choice(joke_data.joke[language])

if __name__ == "__main__":
    app.run('0.0.0.0',port=server_port)