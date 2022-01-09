from bs4 import BeautifulSoup
import requests
html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')

post_listings = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
final_postings = []
for post in post_listings:
    status=post.find(class_='sim-posted').text
    status=" ".join(status.split())
    dict={}    
    if status=='Posted few days ago':
        job_skils=post.find(class_="srp-skills").text
        job_skils=" ".join(job_skils.split())
        dict['job skills']=job_skils
        final_postings.append(dict)
print(final_postings)   

