from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import mysql.connector
import random
import string

# Database Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="-------",
    database="app_interactions"
)


def getColumnsWithTypes(table_name):
    '''
    Input: string e.g. 'table_name'
    Output: list of tuples e.g. [('column1', 'int'), ('column2', 'varchar'), ... ]
    '''
    cursor = db.cursor()
    try:
        query = """
            SELECT COLUMN_NAME, DATA_TYPE 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = %s 
            AND TABLE_NAME = %s
        """
        cursor.execute(query, ('app_interactions', table_name))
        columns = cursor.fetchall()
        return columns
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()


print(getColumnsWithTypes('directors'))
# [('DirectorID', 'int'), ('DirectorName', 'varchar')]

'''
I CAN LITERALLY JUST RECURSIVELY DUMP THE DUMMY DATA
'''


def getTables(db_name):
    '''
    input: str e.g. 'db_name'
    output: list of str e.g. ['table1', 'table2', ... ]
    '''
    cursor = db.cursor()
    try:
        query = """
            SELECT TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES 
            WHERE TABLE_SCHEMA = %s 
        """
        cursor.execute(query, (db_name,))
        tables = cursor.fetchall()
        tablesList = [table[0]
                      for table in tables]  # check yo'self (could be faster?)
        return tablesList
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()


print(getTables('app_interactions'))
# ['advertisements', 'advertisers', 'customers', 'devices', 'directors', 'genres', ... ]


tablesWithColumns = {}
tablesList = getTables('app_interactions')
for table in tablesList:
    columnsWithTypes = getColumnsWithTypes(table)
    tablesWithColumns[table] = columnsWithTypes

print(tablesWithColumns)

#
#
#
#
#
# Trying Something


def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def random_int(min_value=0, max_value=1000):
    return random.randint(min_value, max_value)


def random_float(min_value=0.0, max_value=1000.0):
    return round(random.uniform(min_value, max_value), 2)


def generate_dummy_data(data_type):
    '''
    input: str of SQL DataType e.g. 'int', 'varchar', or 'enum'
    output: dummy data suitable to that type, as defined by helper functions e.g. 'int' --> 884
    '''
    if data_type == 'int':
        return None
    elif 'varchar' in data_type or 'text' in data_type:
        return random_string()
    elif 'float' in data_type or 'double' in data_type:
        return random_float()
    elif 'datetime' in data_type:
        return None
    elif 'tinyint' in data_type:
        return random_int(0, 1)
    elif 'enum' in data_type:
        return None
    else:
        return 'UnknownType'


def populate_dummy_data(tables_with_columns):
    for table, columns in tables_with_columns.items():
        for tup in columns:
            for _ in range(1):  # Number of dummy records per table
                column_names = ", ".join([col[0] for col in columns])
                placeholders = ", ".join(["%s"] * len(columns))
                data = [generate_dummy_data(col[1]) for col in columns]
                cursor = db.cursor()
                try:
                    query = f"""
                        INSERT INTO {table} ({column_names})
                        VALUES ({placeholders})
                    """
                    cursor.execute(query, tuple(data))
                    db.commit()
                except Exception as e:
                    print(e)
                    return str(e)
                finally:
                    cursor.close()


# usage
populate_dummy_data(tablesWithColumns)


#
#
#
#
#
# Garbage pull from original pass at dummy-data populating

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
