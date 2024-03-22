import pyodbc
import logging

def write_to_mssql(data):
    try:
        connection_string = 'DRIVER={SQL Server};SERVER=localhost,1433;DATABASE=kafkaconsume;UID=sa;PWD=yourStrong(!)Password'
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        
        cursor.execute('''
            IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'WeatherData')
            BEGIN
                CREATE TABLE WeatherData (
                    ID INT PRIMARY KEY IDENTITY(1,1),
                    Temperature FLOAT,
                    WeatherCondition NVARCHAR(255),
                    RelativeHumidity FLOAT,
                    WindSpeed FLOAT,
                    WindDirection NVARCHAR(255),
                    RetrievedDateTime DATETIME
                )
            END
        ''')
        connection.commit()

       
        query = "INSERT INTO WeatherData (Temperature, WeatherCondition, RelativeHumidity, WindSpeed, WindDirection, RetrievedDateTime) VALUES (?, ?, ?, ?, ?, GETDATE())"
        cursor.execute(query, tuple(data.values()))
        connection.commit()

        logging.info("Successfully inserted data into MSSQL table")
    except Exception as e:
        logging.error("Error occurred while writing to MSSQL: %s", e)
    finally:
      
        if connection:
            connection.close()

