#!/usr/bin/env python

# Script to add Conor Friedersdorf's top 102 non-fiction 
# articles of 2012 to an Instapaper account. 
# Original list: http://www.byliner.com/spotlights/102-spectacular-nonfiction-articles-2012
# Scraped data: https://scraperwiki.com/scrapers/conor_friedersdorfs_top_articles_of_2012_byliner/
import csv
import getpass 
import sys
import urllib 

reader = csv.DictReader(open('conor_friedersdorfs_top_articles_of_2012_byliner.csv', 'rU'))

AUTHENTICATE_URL = 'https://www.instapaper.com/api/authenticate'
ADD_URL = 'https://www.instapaper.com/api/add'
 
# Check username + password is valid. 
username = raw_input("Enter your Instapaper email or username: ")
passwd = getpass.getpass("And password, if you have one: ")
print 'Checking your account details...'
user_data = urllib.urlencode({"username": username,"password": passwd})
validated = urllib.urlopen(AUTHENTICATE_URL, user_data)
status_code = validated.read()
if status_code!='200':
    if status_code=='403':
        print 'Sorry, invalid username or password! Please check your account details at instapaper.com'
    elif status_code=="500":
        print 'Sorry, the Instapaper API is down. Please try again later.'
    else:
        print "Sorry, something went wrong - status code %s" % status_code
    sys.exit()
print "Successfully authenticated!"

# Add articles. 
print 'Adding articles...'
for i, a in enumerate(reader):
    print "Adding article %s of 102: '%s' from %s by %s" % (i+1, a['heading'], a['publication'], a['author'])
    data = urllib.urlencode({ 
        'username': username,
        'password': passwd,
        'title': a['heading'],
        'url': a['url'],
        'selection': "%s - via Conor Friedersdorf's Best of 2012" % a['publication']
    })
    posted = urllib.urlopen(ADD_URL, data)
    status_code = posted.read()
    if status_code!='201':
        if status_code=="400":
            print 'Bad request or exceeded the rate limit'
        elif status_code=='403': 
            print "Invalid username or password"
        elif status_code=='500':  
            print "Sorry, the Instapaper API encountered an error. Please try again later"
        else:
            print "Sorry, something went wrong - status code %s" % status_code
