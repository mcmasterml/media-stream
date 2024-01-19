class DummyData:
    def spawnData(table_name):
        ''' Initializes some dummy data for
        MySQL Database "app_interactions"
        Table: advertisers, advertisements, directors, genres, devices, and locations
        '''

        # SQL Inserts
        cursor = db.cursor()  # needs `db`, found in `app.py`
        try:
            # advertisers
            advertiserName = 'advertiser ' + \
                ''.join(random.choices(string.ascii_letters, k=10))
            industry = 'ind-' + \
                ''.join(random.choices(string.ascii_letters, k=10))

            cursor.execute('''
                INSERT INTO advertisers (AdvertiserName, Industry)
                VALUES (%s, %s)
            ''', (advertiserName, industry))
            try:
                assert cursor.lastrowid != None  # check auto-increment
            except Exception as e:
                print(e)
            db.commit()

            # advertisements
            adContent = 'adContent ' + \
                ''.join(random.choices(string.ascii_letters, k=50))
            adDuration = 30
            targetDemographic = ''.join(
                random.choices(string.ascii_letters, k=20))
            hasSkip = False

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

            # directors
            directorName = ''.join(random.choices(string.ascii_letters, k=15))

            cursor.execute('''
                INSERT INTO directors (DirectorName)
                VALUES (%s)
            ''', (directorName,))
            try:
                assert cursor.lastrowid != None  # check auto-increment
            except Exception as e:
                print(e)
            db.commit()

            # genres
            genreName = 'genre ' + \
                ''.join(random.choices(string.ascii_letters, k=15))

            cursor.execute('''
                INSERT INTO genres (GenreName)
                VALUES (%s)
            ''', (genreName,))
            try:
                assert cursor.lastrowid != None  # check auto-increment
            except Exception as e:
                print(e)
            db.commit()

            # devices
            deviceType = 'device ' + \
                ''.join(random.choices(string.ascii_letters, k=15))
            operatingSystem = 'os ' + \
                ''.join(random.choices(string.ascii_letters, k=15))
            browser = 'browser ' + \
                ''.join(random.choices(string.ascii_letters, k=15))

            cursor.execute('''
                INSERT INTO devices (DeviceType, OperatingSystem, Browser)
                VALUES (%s)
            ''', (deviceType, operatingSystem, browser))
            try:
                assert cursor.lastrowid != None  # check auto-increment
            except Exception as e:
                print(e)
            db.commit()

            # locations
            latitude = random.uniform(-90.0, 90.0)
            longitude = random.uniform(-90.0, 90.0)

            cursor.execute('''
                INSERT INTO locations (Latitude, Longitude)
                VALUES (%s)
            ''', (latitude, longitude))
            try:
                assert cursor.lastrowid != None  # check auto-increment
            except Exception as e:
                print(e)
            db.commit()

        except Exception as e:
            print(e)
        finally:
            cursor.close()

        return

    def spawnAdvertisements():
        ''' Initializes some dummy data for
        MySQL Database "app_interactions"
        Table: advertisers, advertisements, directors, genres, devices, and locations
        '''

        # SQL Inserts
        cursor = db.cursor()  # needs `db`, found in `app.py`

    def spawnDirectors():
        ''' Initializes some dummy data for
        MySQL Database "app_interactions"
        Table: advertisers, advertisements, directors, genres, devices, and locations
        '''

        # SQL Inserts
        cursor = db.cursor()  # needs `db`, found in `app.py`
