#!/usr/bin/python
#-*- coding:utf-8 -*-
from flask import Flask, url_for
from flask import render_template, flash, redirect, session, request, g, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jisung')
def jisung():
    return render_template('jisung.html')

if __name__ == '__main__':
    app.run(host='14.63.88.216',port=5999,debug=True,threaded=True)
