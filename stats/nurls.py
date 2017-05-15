#
# Detecting URLs with no source, for instance webpack calls
#
import sqlite3

# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/testcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')
print "Created connection with database..."

c =  conn.cursor()

q = """SELECT script_url
       FROM javascript 
       WHERE script_url
       NOT LIKE 'http%' 
       GROUP BY script_url"""

# not urls, nurls, fetched
nurls = c.execute(q).fetchall()
print "Not URLs fetched"

for nurl in nurls:
  print nurl