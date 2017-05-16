import sqlite3

# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
# conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/testcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')
# conn = sqlite3.connect('../bresults/crawl-data.sqlite')
conn = sqlite3.connect('../tresults/crawl-data.sqlite')
print "Created connection with database..."

c =  conn.cursor()

q = """
    SELECT site_url
    FROM site_visits
    """

# Get all urls which are redirected
visit_urls = c.execute(q).fetchall()
print "Collected visited urls..."


# Replace original visit URL domain with redirected domain. But
# only for the visted domain.
for url in visit_urls:
    # If url doesn't end on / append a /
    if url[-1] != '/':
        b = c.execute("UPDATE site_visits SET site_url = ? WHERE site_url = ?",(url[0] + '/', url[0]))

conn.commit()
print "Appended '/' to URL if needed"

#