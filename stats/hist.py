import sqlite3
from operator import itemgetter

# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')

c =  conn.cursor()
script_info = {}
site_info = {}
calls_info = {}
# for row in c.execute('SELECT visit_id, script_url, symbol FROM javascript'):
#     print(row)

diff_scripts_q = "SELECT COUNT(DISTINCT script_url) FROM javascript"
num_scripts = c.execute(diff_scripts_q).fetchone()[0]
script_info['num'] = num_scripts


diff_sites_q = "SELECT COUNT(visit_id) FROM site_visits"
num_sites = c.execute(diff_sites_q).fetchone()[0]
site_info['num'] = num_sites

diff_calls_q = "SELECT COUNT(symbol) FROM javascript"
num_calls = c.execute(diff_calls_q).fetchone()[0]
calls_info['num'] = num_calls


occurence = "SELECT symbol, COUNT(*) AS `num` FROM javascript GROUP BY symbol ORDER BY COUNT(*) ASC"
occurences = c.execute(occurence)
occ_list = occurences.fetchall()

print occ_list
print "Sites visited: ", site_info['num']
print "Scripts encouterd: ", script_info['num']
print "API calls: ", calls_info['num']
print len(occ_list)
# for row in c.execute(query):
#     print(row)



# conn.commit()
conn.close()