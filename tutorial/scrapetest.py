from urllib.request import urlopen
from bs4 import BeautifulSoup

//페이지를 찾을 수 없거나, 404
//서버를 찾을 수 없거나, 503
html = urlopen("http://pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)