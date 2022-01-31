
# This data can be stored in a DB
    # It can be coded to just store new jobs

# This can have email alerts
    # Emails filtering for my skills (which could be stored in a User db)
    # It can filter already emailed jobs to the user and just report new ones

# This PWA can have an account and a interface to see
    #  the jobs 
    #  the skills 
    #  the emailing/bot time for a chron job

# This PWA could have an analytics page to show
    #  the most requested skills, that I don't have
    #  the priciest set of 3 skills

from bs4 import BeautifulSoup
from collections import Counter
import requests
import time

def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

    html = requests.get(url).text

    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

    listSkills = []
    for job in jobs:    
        publishDate = job.find('span', class_ = 'sim-posted').span.text
        if any(element not in publishDate for element in ('few', 'days', 'day')):
            continue

        company = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        # This code makes sure we don't loose spaces between elements composed of two or more words while cleaning whitespaces.
        skills = list(set([ skill.strip().replace('  ', ' ').lower() for skill in job.find('span', class_ = 'srp-skills').text.split(',')]))
        listSkills += skills

        more_info =  job.header.h2.a['href']

        print(f'''
            Company: {company}
            Skills: {', '.join(skills)}
            info+: {more_info}
        ''')

    print(Counter(listSkills))
    sets = set(listSkills)
    sorted = list(sets)
    sorted.sort()
    print('\nSkills asked ', sorted)

if __name__ == '__main__':
        print("hello")
        while True:
            find_jobs()
            print("waiting")
            time.sleep(10 * 60)