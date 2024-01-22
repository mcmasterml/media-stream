from flask import Flask, render_template
from utils import Database


def create_app():
    app = Flask(__name__)

    with app.app_context():
        db_instance = Database('app_interactions')
        db_instance.spawnAll()

    @app.route('/', methods=['GET'])
    def renderLoginPage():
        return render_template('login.html')

    @app.route('/login', methods=['POST'])
    def startSession():
        db_instance.startSession()
        return render_template('home.html')

    @app.route('/browse', methods=['POST'])
    def browse():
        db_instance.browse()
        # TODO: anything. currently doing nothing.
        return render_template('home.html')

    @app.route('/watch-show', methods=['POST'])
    def watchShow():
        db_instance.spawnShow()
        db_instance.watchShow()
        return render_template('home.html')

    @app.route('/watch-ad', methods=['POST'])
    def watchAd():
        db_instance.spawnAdvertisement()
        db_instance.watchAdvertisement()
        return render_template('home.html')

    @app.route('/logout', methods=['POST'])
    def logout():
        db_instance.endSession()
        return render_template('login.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


'''
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from utils import Database
import mysql.connector
import random
import string


def create_app():
    app = Flask(__name__)
    with app.app_context():
        db_instance = Database('app_interactions')
        db_instance.spawnAll()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


@app.route('/', methods=['GET', 'POST'])
def initialize():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def startSession():
    Database.startSession()

    return render_template('home.html')

'''
