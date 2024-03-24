import sqlite3

#joining on possible set of overlaps
query = '''
SELECT 
    npi.last_name,
    npi.forename
FROM npi, grants
    WHERE forename IS NOT NULL 
        AND city IS NOT NULL;
    OUTER JOIN npi
        ON npi.last_name = grants.last_name;
'''

#CREATE TABLE IF NOT EXISTS prospective_bridge();
#INSERT INTO prospective_bridge (last_name, npi_id, grant_id)

conn = sqlite3.connect('data/bridge_npi_grants.db')
cursor = conn.cursor()
cursor.execute(query)
record = cursor.fetchall()
cursor.close()
