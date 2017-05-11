from automation import TaskManager, CommandSequence
from seeds import alexa500, bottom500

# The list of sites that we wish to crawl
NUM_BROWSERS = 4
sites = alexa500.domains
# sites = ['https://www.facebook.com/']
# sites = ['http://279cd9d8.ngrok.io']
# sites = bottom500.domains

# Loads the manager preference and 3 copies of the default browser dictionaries
manager_params, browser_params = TaskManager.load_default_params(NUM_BROWSERS)

# # Update browser configuration (use this for per-browser settings)
for i in xrange(NUM_BROWSERS):
	browser_params[i]['headless'] = True #Launch only browser 0 not headless
	browser_params[i]['js_instrument'] = True
	browser_params[i]['save_javascript'] = False
	browser_params[i]['cookie_instrument'] = False
	browser_params[i]['cp_instrument'] = False


# Update TaskManager configuration (use this for crawl-wide settings)
manager_params['data_directory'] = '~/study/thesis/OpenWPM/results'
manager_params['log_directory'] = '~/study/thesis/OpenWPM/results'

# Instantiates the measurement platform
# Commands time out by default after 60 seconds
manager = TaskManager.TaskManager(manager_params, browser_params)

# Visits the sites with all browsers simultaneously
for site in sites:
    command_sequence = CommandSequence.CommandSequence(site)
    # manager.execute_command_sequence(command_sequence, index=None)
    # Start by visiting the page
    command_sequence.get(sleep=2, timeout=600)

    # dump_profile_cookies/dump_flash_cookies closes the current tab.
    command_sequence.dump_profile_cookies(120)

    manager.execute_command_sequence(command_sequence, index=None) # ** = synchronized browsers

# Shuts down the browsers and waits for the data to finish logging
manager.close()
