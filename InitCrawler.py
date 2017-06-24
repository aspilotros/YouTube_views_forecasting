
"""
Created on Tue May 16 14:09:48 2017

@author: ale
"""

import sys
sys.path.append('/home/ale/Desktop/Portfolio/YTCrawl-master')
from crawler import Crawler
c=Crawler()
c._crawl_delay_time = 1 # set crawling delay to 1
c._cookie_update_delay_time = 1 # set cookie updating delay to 1
c.batch_crawl("/home/ale/Desktop/Portfolio/firstbatch.txt", "/home/ale/Desktop/Portfolio/Firstbatch")