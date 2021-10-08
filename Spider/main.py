import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

findLink = re.compile(r'<a class="title" href="//(.*?)" target="_blank">(.*?)</a>')

def getData(baseurl):
    datalist = []
    html = askURL(baseurl)
    print(html)
    soup = BeautifulSoup(html,"html.parser")
    datalist = soup.find_all('a',class_="title")
    cnt = 0
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    for item in datalist:
        #print(item)
        data = []
        item = str(item)
        link = re.findall(findLink,item)[0]
        cnt+=1;
        print(cnt,end=" ")
        print(link[1])
        print(link[0])
        worksheet.write(cnt-1,0,cnt)
        worksheet.write(cnt-1,1,link[1])
        worksheet.write(cnt-1,2,link[0])
    workbook.save('bilibili.xls')
    return datalist

def askURL(url):
    #伪装头
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "Accept": "application/json"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLerror as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def main():
    baseurl = "https://www.bilibili.com/v/popular/rank/all"
    getData(baseurl)
    #html = askURL(baseurl)
    # t_list = bs.find_all(text = re.compile("bilibili"))
    # for item in t_list:
    #     print(item)

if __name__ == "__main__":
    main()

