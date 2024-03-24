import sqlite3


query_grants = '''
CREATE TABLE IF NOT EXISTS grants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER NOT NULL,
    pi_names VARCHAR(500),
    pi_ids VARCHAR(500),
    organization VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    forename VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

query_npi = '''
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


conn = sqlite3.connect('data/double_grants_npi.db')
cursor = conn.cursor()

# version_query = 'select sqlite_version();'
cursor.execute(query_grants)
cursor.execute(query_npi)
record = cursor.fetchall()
print('version is: ', record)

cursor.close()