import os
import time
import datetime
import re
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

for page in range(20):
    page += 1
#     base = page + 12
    url = "https://freemusicarchive.org/genre/Classical?sort=track_date_published&d=1&page=" + str(page)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko",
            }

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response,"html.parser")
    response.close()
    
    elems = soup.find_all(href=re.compile("https://files.freemusicarchive.org/storage-freemusicarchive-org/music/"))
    elenum =len(elems)
    for onpage in range(elenum):
        dl_url = elems[onpage].attrs['href']
        print(dl_url)
        # urllib.request.urlopen(dl_url)
    
        r_image = requests.get(dl_url)
        filename_image = os.path.basename(dl_url)
        with open('/home/ryo/Documents/fma/song/classical/' + filename_image, 'wb') as f:
            f.write(r_image.content)

        time.sleep(5)
        dt = datetime.datetime.now()
        print(dt)
    time.sleep(10)
