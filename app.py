# -*- coding: utf-8 -*-
"""
Created on Wed May 14 15:46:01 2025

@author: USER
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'development-key')

# Simple data storage (in a real app, you might use a database)
key_status = {
    "holder": None,
    "timestamp": None,
    "is_available": True
}

@app.route('/')
def index():
    return render_template('index.html', key_status=key_status)

@app.route('/take_key', methods=['POST'])
def take_key():
    name = request.form.get('name')
    if name:
        key_status["holder"] = name
        key_status["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        key_status["is_available"] = False
    return redirect(url_for('index'))

@app.route('/return_key', methods=['POST'])
def return_key():
    key_status["holder"] = None
    key_status["is_available"] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
