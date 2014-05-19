#!/usr/bin/env python

from flask import Flask, render_template, flash, g, abort
import os

app = Flask(__name__) 
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='foo that bar',
    DATABASE=os.path.join(app.root_path, 'Database/example.db'),
    HOST='0.0.0.0'
))

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    "Opens a new db connection if there isn't one established"
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# app.route is called a decorator. don't worry about it too much right
# now.
@app.route('/')
def hell_world():
    # do work
    flash('UNDER DEVELOMENT')

    db = get_db()
    cur = db.execute('title, link from links order by id desc')
    entries = cur.fetchall()

    return render_template('app.html', entries=entries)

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
