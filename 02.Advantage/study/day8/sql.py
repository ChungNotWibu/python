import sqlite3
database_path = " "
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

sql_create_manufactures = """
    CREAT TABLE IF NOT EXISTS Manufacturers(
        ManufacturerID INT UNIQUE,
        ManufacturerName TEXT,
        PRIMARY KEY (ManufacturerID)
    );
"""

sql_create_phones = """
    CREATE TABLE IF NOT EXISTS Phones (
        PhoneID INT UNIQUE,
        Model TEXT,
        ManufacturerID INT,
        Price REAL,
        StockQuantity INT,
        PRIMARY KEY (PhoneID),
        FOREGIN KEY (ManufacturerID) REFERENCES ManufacturerS(ManufacturerID)
    );
"""

sql_create_customers = """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT UNIQUE,
        CustomerName INT,
        Email TEXT,
        Address TEXT,
        PRIMARY KEY (CustomerID),
    );
"""

sql_create_transactions = """
    CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INT UNIQUE,
        
    """