import sqlite3


# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
# conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/testcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')
conn = sqlite3.connect('../bresults/crawl-data.sqlite')
# conn = sqlite3.connect('../tresults/crawl-data.sqlite')

print "Created connection with database..."
drop = ['xpath', 'task', 'profile_cookies', 'localstorage', 'http_responses_proxy', 'http_responses', 'http_request_proxy', 'flash_cookies']

c =  conn.cursor()
# Get all urls which are redirected and are in the visited_sites
for table in drop:
    q = 'DROP TABLE IF EXISTS ' + table 
    table_dropped = c.execute(q)
    print 'Deleted table' + table + '...'

conn.commit()
print 'Committed to database...'

