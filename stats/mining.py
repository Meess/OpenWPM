import sqlite3
from operator import itemgetter
from pymining import itemmining
import itertools
import time
import matplotlib.pyplot as plt

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

diff_scripts_q = "SELECT COUNT(DISTINCT script_url) FROM javascript"
num_scripts = float(c.execute(diff_scripts_q).fetchone()[0])

occurence_q = "SELECT symbol, COUNT(*) AS `num` FROM javascript GROUP BY symbol ORDER BY COUNT(*) ASC"
occurences = c.execute(occurence_q)

data = [[in_script[each[0]]/num_scripts, each[0]] for each in occurences]


perc, names = zip(*data)
ax = plt.subplot(111)
bins = range(0, len(perc))
ax.bar(bins, perc)
# ax.set_xticks(bins)
# ax.set_xticklabels(names,rotation=45)

# ax.xlabel('Occurence low to high')
# ax.ylabel('%% of script found')
plt.show()

conn.close()
