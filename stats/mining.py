import sqlite3
from operator import itemgetter
from pymining import itemmining
import itertools
import time


# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')

c =  conn.cursor()

q = "SELECT script_url, GROUP_CONCAT(DISTINCT symbol) FROM javascript GROUP BY script_url"


script_urls = c.execute(q).fetchall()

in_script = {}
for url in script_urls:
    calls = url[1].split(',')
    for call in calls:
        try:
            in_script[call] += 1
        except KeyError, e:
            in_script[call] = 1
        except:
            print 'No KeyError, something went wrong'

for each in in_script.keys():
    print each, in_script[each]


diff_scripts_q = "SELECT COUNT(DISTINCT script_url) FROM javascript"
num_scripts = c.execute(diff_scripts_q).fetchone()[0]

conn.close()
