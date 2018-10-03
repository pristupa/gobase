from lxml import html
import sqlite3
import requests

conn = sqlite3.connect('tigr_mirror.db')
c = conn.cursor()

# Create schema
c.execute('''
CREATE TABLE IF NOT EXISTS tigr_tournaments (
  tigr_tournament_id INTEGER,
  consecutive_number INTEGER,
  name TEXT,
  location TEXT,
  start_date TEXT,
  end_date TEXT,
  fetched_at TEXT
)
''')

r = requests.get('http://tigr.gofederation.ru/OldSite/Tigr_TurnL.php')
print(r.text)
tree = html.fromstring(r.text)
rows = tree.xpath('/table')

print(rows)

for row in rows:
    print(row)

conn.commit()
conn.close()
