import sqlite3
import csv

# 連接到 SQLite 資料庫
conn = sqlite3.connect("SeniorProject.db")
print("Database is connected successfully!")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS venue
    (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Facility_Name TEXT,
        ODRSF_facility_type TEXT,
        Prov_Terr TEXT,
        Latitude REAL,
        Longitude REAL,
        Price INTEGER,
        Max_audience INTEGER,
        Address TEXT
        

    )
    """
)
print("venue table is created successfully!")
conn.commit()

def insert_csv_data(csv_file_name):
    with open(csv_file_name, 'r',encoding='utf-8') as csvFile:
        venue = csv.reader(csvFile)
        next(venue) 
        for row in venue:
            _, Facility_Name, ODRSF_facility_type, Prov_Terr, Latitude, Longitude, Price, Max_audience, Address = row
            cursor.execute(
                """
                INSERT INTO venue (Facility_Name, ODRSF_facility_type, Prov_Terr, Latitude, Longitude, Price, Max_audience, Address) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (Facility_Name, ODRSF_facility_type, Prov_Terr, Latitude, Longitude, Price, Max_audience, Address)
            )



insert_csv_data("venue.csv")
conn.commit()
print("Data are inserted into DB table successfully!")
conn.close()