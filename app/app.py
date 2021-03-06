import os
from flask import Flask, request, render_template
from message import greet, retrieve_local_ip_address


app = Flask(__name__)
DEPLOY = os.getenv('DEPLOY')


@app.route('/')
def main():
    if DEPLOY == 'heroku':
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = retrieve_local_ip_address()
        
    return render_template('index.html',message=greet(ip_address))


if __name__ == '__main__':
    app.run(debug=True)
