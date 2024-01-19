from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import mysql.connector
import random
import string

app = Flask(__name__)

# Database Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="dilly",
    database="app_interactions"
)


@app.route('/', methods=['GET', 'POST'])
def initialize():
    print('first.......')
    # Dummy Data
    # advertiser
    advertiserName = 'advertiser ' + \
        ''.join(random.choices(string.ascii_letters, k=10))
    industry = 'ind-' + ''.join(random.choices(string.ascii_letters, k=10))
    # advertisement
    adContent = 'adContent ' + \
        ''.join(random.choices(string.ascii_letters, k=50))
    adDuration = 30
    targetDemographic = ''.join(random.choices(string.ascii_letters, k=20))
    hasSkip = False
    # director
    directorName = ''.join(random.choices(string.ascii_letters, k=15))
    # genre
    genre = 'genre ' + ''.join(random.choices(string.ascii_letters, k=15))

    # device
    deviceType = 'device ' + \
        ''.join(random.choices(string.ascii_letters, k=15))
    operatingSystem = 'os ' + \
        ''.join(random.choices(string.ascii_letters, k=15))
    browser = 'browser ' + ''.join(random.choices(string.ascii_letters, k=15))

    # location
    latitude = random.uniform(-90.0, 90.0)
    longitude = random.uniform(-90.0, 90.0)

    cursor = db.cursor()
    try:
        # advertiser
        cursor.execute('''
            INSERT INTO advertisers (AdvertiserName, Industry)
            VALUES (%s, %s)
        ''', (advertiserName, industry))
        print("THIS RAN!")
        try:
            assert cursor.lastrowid != None  # check auto-increment
        except Exception as e:
            print(e)
        db.commit()

        # advertisement
        advertiserID = cursor.lastrowid  # grabbing ID from last commit
        cursor.execute('''
            INSERT INTO advertisements (AdvertiserID, AdContent, AdDuration, TargetDemographic, HasSkip)
            VALUES (%s, %s, %s, %s, %s)
        ''', (advertiserID, adContent, adDuration, targetDemographic, hasSkip))
        try:
            assert cursor.lastrowid != None  # check auto-increment
        except Exception as e:
            print(e)
        db.commit()

        # director
        cursor.execute('''
            INSERT INTO directors (DirectorName)
            VALUES (%s)
        ''', (directorName,))
        try:
            assert cursor.lastrowid != None  # check auto-increment
        except Exception as e:
            print(e)
        db.commit()

        # genre
        cursor.execute('''
            INSERT INTO directors (DirectorName)
            VALUES (%s)
        ''', (directorName,))
        try:
            assert cursor.lastrowid != None  # check auto-increment
        except Exception as e:
            print(e)
        db.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def startSession():
    if request.method == 'POST':
        # Connect to database and insert data
        cursor = db.cursor()
        try:
            cursor.execute('''YOUR INSERT QUERY HERE''')
            db.commit()
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
