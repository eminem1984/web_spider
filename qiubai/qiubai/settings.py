# Scrapy settings for qiubai project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'qiubai'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['qiubai.spiders']
NEWSPIDER_MODULE = 'qiubai.spiders'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'

