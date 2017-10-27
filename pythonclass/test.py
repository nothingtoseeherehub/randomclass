import urllib
from bs4 import BeautifulSoup

url="http://labfiles.linuxacademy.com/python/scraping/courses.html"

html_data = urllib.urlopen(url).read()

soup = BeautifulSoup(html_data,"lxml")

sections = soup.find_all('a',attrs={'class':'col-xs-12 p-x-0 library-content-box-container content-aws'})

for section in sections:
    title = section.find('span', attrs={"class":"library-content-title"})
    length = section.find('span', attrs={"class":"library-content-length"})
    url = section['href']
    html_data = urllib.urlopen(url).read()
    instructor = BeautifulSoup(html_data,"lxml").find_all('span',attrs={"class":"instructor-name"})
    print "%s is taught by %s [%s]" % ( title.text, instructor[0].text, length.text)

