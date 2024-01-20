from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from utils import Database
import mysql.connector
import random
import string

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def initialize():
    Database.spawnAll()  # Create some dummy data
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def startSession():
    Database.startSession()

    return render_template('home.html')


if __name__ == '__main__':
    Database = Database('app_interacions')
    app.run(debug=True)
