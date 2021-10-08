

import urllib.request

# response = urllib.request.urlopen("https://www.baidu.com/")
# print(response.read().decode('utf-8'))   #utf-8 decode

#get post response
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response =  urllib.request.urlopen("https://www.bilibili.com/",data=data)
# print(response.read().decode('utf-8'))


# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out")


#response = urllib.request.urlopen("https://www.bilibili.com/")
#print(response.status)
#print(response.getheaders())
#url = "https://www.douban.com"

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
#     "Accept":"application/json"
# }
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name':'jim'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept":"application/json"
}
url = "https://www.bilibili.com/v/popular/rank/all"
#data = bytes(urllib.parse.urlencode({'name':'jim'}),encoding="utf-8")
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))