import urllib.request
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0', 'referer' : 'http://www.naver.com'}

url = "https://www.pixiv.net/artworks/86825034"

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req).read().decode("utf-8")
print(str(response)[0:30]+"...")
soup = BeautifulSoup(response, 'html.parser')

meta = soup.find("meta")["name"]
print(meta)

imgurl = "https://i.pximg.net/img-master/img/2021/01/04/23/41/43/86825034_p2_master1200.jpg"

imgreq = urllib.request.Request(url, headers=headers)
imgres = urllib.request.urlopen(imgreq).read()

print(imgres)

urllib.request.urlretrieve(imgreq, "123.jpg")

i = 0

"""for img in soup.find_all("div", role_ = "presentation"):
    imgurl = img.find("img")["src"]
    print("{0}번째 이미지 로딩 성공, url:{1}".format(i,imgurl))

    with urllib.request.urlopen(imgurl) as file:
        with open("./img/"+ str(i) +".jpg",'wb') as savedimg:
            savedimg.write(file.read())
            print("{0}번째 이미지 저장 성공".format(i))

            i += 1
            """