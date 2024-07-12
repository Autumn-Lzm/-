import requests
from bs4 import BeautifulSoup
for i in range(1, 101):
    if i == 1:
        url = "https://pic.netbian.com/4kmeinv/"
    else:
        url = "https://pic.netbian.com/4kmeinv/index_{}.html".format(i)
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    li = soup.find_all("li")
    for value in li:
        img = value.a.img
        if img != None:
            img_url = "https://pic.netbian.com{}".format(img["src"])
            content = requests.get(img_url).content
            filename = img_url.split("/")[-1]
            # print(filename)
            with open("../img/"+filename, "wb") as file:
                file.write(content)
                print("{}下载成功".format(filename))
