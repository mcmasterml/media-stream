import mysql.connector

# Database Configuration
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="dilly",
    database="app_interactions")


# Helper functions
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


# Database as a Python object
class Database():
    def __init__(self, database_name):
        tablesWithColumns = {}
        tablesList = getTables(database_name)
        for table in tablesList:
            columnsWithTypes = getColumnsWithTypes(table)
            tablesWithColumns[table] = columnsWithTypes
        self.tableSchema = tablesWithColumns

    def spawnAll(self):
        ''' 
        Initializes some dummy data for all tables in the DB
        based on the proper datatype
        ignores 'int' to avoid ID columns
        '''
        populate_dummy_data(self.tableSchema)

    def spawnAdvertisement(self):
        ''' 
        Initializes some dummy data for the folowing tables:
        advertisers, advertisements, session_ads
        '''
        # TODO: spawn data for the advertisements section when user watches an ad

    def watchAdvertisement(self):
        '''
        Captures data on user watching an ad
        '''
        # TODO:

    def spawnStream(self):
        ''' 
        Initializes some dummy data for the following tables:
        shows, genres, directors, session_shows
        '''
        # TODO: spawn data for shows section when user watches a stream

    def watchStream(self):
        '''
        Captures data on user watching an ad
        '''
        # TODO:

    def startSession(self):
        '''
        Models the beginning of a session for user
        populates portion of `sessions` table
        '''
        # TODO: insert into sessions (relevant data)
        pass

    def endSession(self):
        '''
        Models the end of a session for user
        populates portion of `sessions` table
        '''
        # TODO:
