import sqlite3
# from operator import itemgetter
# from pymining import itemmining
import itertools
import time
import matplotlib.pyplot as plt
from pylab import *
from urlparse import urlparse


replace_redirect = False
# conn = sqlite3.connect('../testdb/jsapi_crawl.sqlite')
# conn = sqlite3.connect('../../b500/bcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/tcrawl-data.sqlite')
# conn = sqlite3.connect('../../b500/testcrawl-data.sqlite')
# conn = sqlite3.connect('../results/crawl-data.sqlite')
# conn = sqlite3.connect('../bresults/crawl-data.sqlite')
# conn = sqlite3.connect('../tresults/crawl-data.sqlite')
print "Created connection with database..."

c =  conn.cursor()

# Only needs to be run once on the database, altought multiple times doesn't harm
if (replace_redirect):

    # while still redirects starting with http are active we assume
    # these are correct redirects and replace the original value. We
    # break when there are nog more valid redirects present
    while True:
        q = """
            SELECT url, location
            FROM http_responses
            WHERE location != ''
            AND url IN 
                (SELECT site_url FROM site_visits)
            """

        # Get all urls which are redirected and are in the visited_sites
        redirect_urls = c.execute(q).fetchall()
        print "Collected", len(redirect_urls) ,"redirected urls..."
        if len(redirect_urls) == 0:
            break

        # Replace original visit URL domain with redirected domain. But
        # only for the visted domain and redirects starting with http.
        for url, redirect in redirect_urls:
            if redirect.startswith('http'):
                b = c.execute("UPDATE site_visits SET site_url = ? WHERE site_url = ?",(redirect, url))
            # We want to delete redirects we assume are not correct
            # because they don't start with http and we are not 
            # going to write complicated traceback to fix them.
            redirect_urls = c.execute("DELETE FROM http_responses WHERE location = ?", (redirect,))

    urls = c.execute("""SELECT site_url 
                        FROM site_visits""").fetchall()
    for url in urls:
        url = url[0]
        parsed_uri = urlparse(url)
        stripped_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        if stripped_url != url:
            c.execute("UPDATE site_visits SET site_url = ? WHERE site_url = ?",(stripped_url, url))
            print "Stripped:", url, "-TO->", stripped_url

    conn.commit()
    print "Replaced all original URLs with redirected URLs..."

# Query all symbols and group them by script and domain
q = """
    SELECT javascript.script_url AS script_url,
           site_visits.site_url AS site_url
    FROM javascript
    INNER JOIN site_visits
    ON javascript.visit_id = site_visits.visit_id
    GROUP BY script_url;
    """

script_urls = c.execute(q).fetchall()
# print script_urls
a = [script[1] in script[0] for script in script_urls]
print "1st party: ", sum(a)
print "3rd party: ", len(a) - sum(a)
print "All: ", len(script_urls)

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