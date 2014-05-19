#!/usr/bin/env python

from flask import Flask
app = Flask(__name__) 

# app.route is called a decorator. don't worry about it too much right
# now.
@app.route('/')
def hell_world():
    return 'Top Reddit Links!'

# a few example pages
@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
