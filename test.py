from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import mysql.connector
import random
import string

# Database Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="dilly",
    database="app_interactions"
)


def get_table_info(table_name):
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
        return {'columns': columns}
    except Exception as e:
        print(e)
        return str(e)
    finally:
        cursor.close()


print(get_table_info('directors'))
# {'columns': [('DirectorID', 'int'), ('DirectorName', 'varchar')]}

'''
I CAN LITERALLY JUST RECURSIVELY DUMP THE DUMMY DATA
'''
