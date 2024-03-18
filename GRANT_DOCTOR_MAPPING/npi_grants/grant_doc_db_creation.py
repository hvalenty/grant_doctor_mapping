import sqlite3


query = '''
CREATE TABLE IF NOT EXISTS grants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER NOT NULL,
    budget_start DATE,
    grant_type VARCHAR(100),
    total_cost FLOAT,
    pi_names VARCHAR(500),
    pi_ids VARCHAR(500),
    organization VARCHAR(500),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    is_contact BOOLEAN,
    both_names VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    forename VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''


conn = sqlite3.connect('data/grants_datatable.db')
cursor = conn.cursor()

# version_query = 'select sqlite_version();'
cursor.execute(query)
record = cursor.fetchall()
print('version is: ', record)

cursor.close()