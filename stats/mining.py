import sqlite3
from operator import itemgetter
from pymining import itemmining
import itertools
import time


# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
# conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
conn = sqlite3.connect('../results/crawl-data.sqlite')

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



# Redundant, can just be done with quer (500x faster)
# q = "SELECT DISTINCT script_url FROM javascript"
# script_urls = c.execute(q).fetchall()
# a = time.time()
# groups1 = [list(itertools.chain.from_iterable(c.execute("SELECT symbol FROM javascript WHERE script_url=(?)",url).fetchall())) for url in script_urls]
# print time.time() - a

q = "SELECT script_url, GROUP_CONCAT(DISTINCT symbol) FROM javascript GROUP BY script_url"


script_urls = c.execute(q).fetchall()

for each in script_urls:
    print each
conn.close()
