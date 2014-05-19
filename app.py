#!/usr/bin/env python

from flask import Flask
app = Flask(__name__) 

# app.route is called a decorator. don't worry about it too much right
# now.
def hell_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
