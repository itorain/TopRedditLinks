#!/usr/bin/env python

from flask import Flask, render_template, flash
app = Flask(__name__) 
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='foo that bar',
    HOST='0.0.0.0'
))

# app.route is called a decorator. don't worry about it too much right
# now.
@app.route('/')
def hell_world():
    # do work
    flash('UNDER DEVELOMENT')
    return render_template('app.html')

# a few example pages
@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    flash('testing: %s was here!' % name)
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run()
