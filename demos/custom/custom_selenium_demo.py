from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

FIREFOX_BIN_PATH = os.getcwd() + "/firefox-bin/firefox-bin"

fb = FirefoxBinary(firefox_path=FIREFOX_BIN_PATH)
# fo = Options()
# fo.headless = True
# fo.add_argument('--headless')
# driver = webdriver.Firefox(firefox_binary=fb, options=fo)
driver = webdriver.Firefox(firefox_binary=fb)
driver.get("http://example.com")
print(driver.title)
driver.quit()


# import argparse
# from pathlib import Path

# import tranco

# from custom_command import LinkCountingCommand
# from openwpm.command_sequence import CommandSequence
# from openwpm.commands.browser_commands import GetCommand
# from openwpm.config import BrowserParams, ManagerParams
# from openwpm.storage.sql_provider import SQLiteStorageProvider
# from openwpm.task_manager import TaskManager

# parser = argparse.ArgumentParser()
# parser.add_argument("--tranco", action="store_true", default=False),
# args = parser.parse_args()
# if args.tranco:
#     # Load the latest tranco list. See https://tranco-list.eu/
#     print("Loading tranco top sites list...")
#     t = tranco.Tranco(cache=True, cache_dir=".tranco")
#     latest_list = t.list()
#     sites = ["http://" + x for x in latest_list.top(10)]
# else:
#     sites = [
#         "http://www.example.com",
#         "http://www.princeton.edu",
#         "http://citp.princeton.edu/",
#     ]
# # Loads the default ManagerParams
# # and NUM_BROWSERS copies of the default BrowserParams
# NUM_BROWSERS = 2
# manager_params = ManagerParams(num_browsers=NUM_BROWSERS)
# browser_params = [BrowserParams(display_mode="native") for _ in range(NUM_BROWSERS)]
# # Update browser configuration (use this for per-browser settings)
# for browser_param in browser_params:
#     # Record HTTP Requests and Responses
#     browser_param.http_instrument = True
#     # Record cookie changes
#     browser_param.cookie_instrument = True
#     # Record Navigations
#     browser_param.navigation_instrument = True
#     # Record JS Web API calls
#     browser_param.js_instrument = True
#     # Record the callstack of all WebRequests made
#     browser_param.callstack_instrument = True
#     # Record DNS resolution
#     browser_param.dns_instrument = True

# # Update TaskManager configuration (use this for crawl-wide settings)
# manager_params.data_directory = Path("./datadir/")
# manager_params.log_path = Path("./datadir/openwpm.log")
# # memory_watchdog and process_watchdog are useful for large scale cloud crawls.
# # Please refer to docs/Configuration.md#platform-configuration-options for more information
# # manager_params.memory_watchdog = True
# # manager_params.process_watchdog = True
# # Commands time out by default after 60 seconds
# with TaskManager(
#     manager_params,
#     browser_params,
#     SQLiteStorageProvider(Path("./datadir/crawl-data.sqlite")),
#     None,
# ) as manager:
#     # Visits the sites
#     for index, site in enumerate(sites):

#         def callback(success: bool, val: str = site) -> None:
#             print(
#                 f"CommandSequence for {val} ran {'successfully' if success else 'unsuccessfully'}"
#             )

#         # Parallelize sites over all number of browsers set above.
#         command_sequence = CommandSequence(
#             site,
#             site_rank=index,
#             callback=callback,
#         )
#         # Start by visiting the page
#         command_sequence.append_command(GetCommand(url=site, sleep=3), timeout=60)
#         # Have a look at custom_command.py to see how to implement your own command
#         command_sequence.append_command(LinkCountingCommand())
#         # Run commands across all browsers (simple parallelization)
#         manager.execute_command_sequence(command_sequence)
