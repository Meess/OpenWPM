import sqlite3
from operator import itemgetter
from pymining import itemmining
import itertools
import time
import matplotlib.pyplot as plt
from pylab import *

# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
# conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/testcrawl-data.sqlite')
conn = sqlite3.connect('../results/crawl-data.sqlite')
print "Created connection with database..."

c =  conn.cursor()

q = """
    SELECT url, location
    FROM http_responses
    WHERE location != ''

    """

# Get all urls which are redirected
redirect_urls = c.execute(q).fetchall()
print "Collected redirected urls..."


# Replace original visit URL domain with redirected domain. But
# only for the visted domain.
for url, redirect in redirect_urls:
    b = c.execute("UPDATE site_visits SET site_url = ? WHERE site_url = ?",(redirect, url))
    print redirect

conn.commit()
print "Replaced all original URLs with redirected URLs..."

# exit()
# Query all symbols and group them by script and domain
q = """
    SELECT javascript.script_url AS script_url, 
           site_visits.site_url AS site_url,
           GROUP_CONCAT(DISTINCT javascript.symbol) AS symbol
    FROM javascript 
    INNER JOIN site_visits 
    ON javascript.visit_id = site_visits.visit_id
    GROUP BY script_url;
    """
        # WHERE symbol LIKE '%Canvas%'f

script_urls = c.execute(q).fetchall()
print script_urls
a = [script[1] in script[0] for script in script_urls]
print sum(a)

# for each in script_urls:
#     print each

exit()
q = """SELECT script_url, 
              GROUP_CONCAT(DISTINCT symbol) 
       FROM javascript 
       WHERE symbol 
       LIKE '%Canvas%' 
       GROUP BY script_url"""


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

occurence_q = "SELECT symbol, COUNT(*) AS `num` FROM javascript WHERE symbol LIKE '%Canvas%' GROUP BY symbol ORDER BY COUNT(*) ASC"
occurences = c.execute(occurence_q)

data = [[in_script[each[0]]/num_scripts, each[0]] for each in occurences]

perc, names = zip(*data)
bins = range(0, len(perc))

figure(1)
barh(bins, perc, align='center')
yticks(bins, names)
show()





# perc, names = zip(*data)
# ax = plt.subplot(111)
# bins = range(0, len(perc))
# ax.bar(bins, perc)
# # ax.set_xticks(bins)
# # ax.set_xticklabels(names,rotation=45)

# # ax.xlabel('Occurence low to high')
# # ax.ylabel('%% of script found')
# plt.show()

conn.close()

# q = "SELECT javascript.script_url, site_visits.site_url ,GROUP_CONCAT(DISTINCT javascript.symbol) FROM javascript INNER JOIN site_visits on javascript.visit_id = site_visits.visit_id WHERE javascript.symbol LIKE '%Canvas%' GROUP BY javascript.script_url;"

# q = """
#     SELECT CASE http_responses.location 
#                 WHEN ''
#                 THEN site_visits.site_url
#                 ELSE http_responses.location
#                 END AS url
#     FROM site_visits
#     LEFT JOIN http_responses 
#     ON http_responses.visit_id = site_visits.visit_id 

#     """