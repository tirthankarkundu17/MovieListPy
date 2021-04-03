import bs4 as bs
import urllib2
url = "http://in.bookmyshow.com/hyderabad/movies"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
soup = bs.BeautifulSoup(response, 'lxml')
data = {}
for name in soup.find_all("div", class_="card-container"):
    for buytick in name.find_all("div", class_="content"):
        for tick in buytick.find_all("a"):
            if tick['href'] != "":
                loc = "http://in.bookmyshow.com/" + tick['href']
                requestven = urllib2.Request(loc)
                responseven = urllib2.urlopen(requestven)
                soupvenue = bs.BeautifulSoup(responseven, 'lxml')
                for m in name.find_all("a", class_="__movie-name"):
                    m_name = m.text
                for venue in soupvenue.find_all("a", class_="__venue-name"):
                    data.setdefault(m_name, []).append(venue.text)
for movie in data:
    print movie + " playing at locations :",
    for loc in data[movie]:
        print loc,
    print "\n"
