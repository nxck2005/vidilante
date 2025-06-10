from flask import request, send_file, jsonify, render_template, redirect, url_for, request, flash
from src import app
from procLogic import processVideoOperation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procVideo')
def processVideo():
    return processVideoOperation(request)