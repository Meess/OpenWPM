import sqlite3
# from operator import itemgetter
# from pymining import itemmining
import itertools
import time
import matplotlib.pyplot as plt
from pylab import *
from urlparse import urlparse
from itertools import compress

replace_redirect = False
# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
# conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/testcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')
conn = sqlite3.connect('../bresults/crawl-data.sqlite')
# conn = sqlite3.connect('../tresults/crawl-data.sqlite')
print "Created connection with database..."

c =  conn.cursor()

q = """
    SELECT http_requests.is_third_party_window AS third,
           javascript.script_url AS script_url,
           GROUP_CONCAT(symbol) AS symbol 
    FROM javascript
    INNER JOIN http_requests
    WHERE http_requests.url = script_url
    AND http_requests.visit_id = javascript.visit_id
    GROUP BY script_url, javascript.visit_id;
    """

script_urls = c.execute(q).fetchall()
third_urls = [script for script in script_urls if script[0]]
first_urls = [script for script in script_urls if not script[0]]

print "num 1st party scripts:", len(first_urls)
print "num 3rd party scripts:", len(third_urls)


q = """
    SELECT script_url
    FROM javascript
    GROUP BY script_url, visit_id;
    """

num_script = c.execute(q).fetchall()
print 'Total scripts:', len(num_script)
print 'Scripts lost:', len(num_script) - len(first_urls) - len(third_urls)


in_fp_script = {}
in_tp_script = {}
for url in script_urls:
    calls = url[2].split(',')
    for call in calls:
        try:
            if url[0]:
                in_tp_script[call] += 1
            elif url[0] == 0:
                in_fp_script[call] += 1
        except KeyError, e:
            if url[0]:
                in_tp_script[call] = 1
            elif url[0] == 0:
                in_fp_script[call] = 1
        except:
            print 'No KeyError, something went wrong'

q = """
    SELECT script_url
    FROM javascript
    GROUP BY script_url, visit_id;
    """

num_script = c.execute(q).fetchall()

occurence_q = """
              SELECT symbol, COUNT(*) AS `num` 
              FROM javascript 
              GROUP BY symbol 
              ORDER BY COUNT(*) ASC
              """

occurences = c.execute(occurence_q)

# first party stats
# num_urls = float(len(first_urls))
# data_fp = [[in_fp_script[each[0]]/num_urls, each[0]] if each[0] in in_fp_script else [0.0, each[0]] for each in occurences]

# perc, names = zip(*data_fp)
# bins = range(0, len(perc))

# figure(1)
# barh(bins, perc, align='center')
# yticks(bins, names)
# show()


# third party stats
num_urls = float(len(third_urls))
data_tp = [[in_tp_script[each[0]]/num_urls, each[0]] if each[0] in in_tp_script else [0.0, each[0]] for each in occurences]

perc, names = zip(*data_tp)
bins = range(0, len(perc))

figure(1)
barh(bins, perc, align='center')
yticks(bins, names)
show()
