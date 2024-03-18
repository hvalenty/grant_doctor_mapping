import sqlite3


query = '''
CREATE TABLE IF NOT EXISTS npi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    npi INTEGER NOT NULL,
    taxonomy_code VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    forename VARCHAR(100),
    address VARCHAR(100),
    cert_date DATE,
    state VARCHAR(100),
    country VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''


conn = sqlite3.connect('data/npi_datatable.db')
cursor = conn.cursor()

# version_query = 'select sqlite_version();'
cursor.execute(query)
record = cursor.fetchall()
print('version is: ', record)

cursor.close()