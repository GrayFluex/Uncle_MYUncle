from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def getData(baseurl):
    datalist = []
    return datalist

def saveData(savepath):
    print("save")
def main():
    baseurl = "https://www.bilibili.com/v/popular/all"
    datalist = getData(baseurl)
    savepath = ".\\Data.xls"
    saveData(savepath)

if __name__ == "__main__":
    main()