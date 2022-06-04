# -*- coding = utf-8 -*-
# @Author: Black-ice-TangKeKe
# @time: 2022/5/30 19:17
# @File: main.py
# @Software: PyCharm
import datetime

import requests                 #请求模块
import re                       #正则表达式
import os                       #目录操作


findlink = re.compile(r'"originalPath":"(.*?)"')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'cookie': 'u_third_platform_source=baidu; _ga=GA1.1.1049456175.1654242704; auth_tk=YTIzN2U1ZmM3MzU1NDE4YmJjZjY1NDhlODUxNGEyMDdqbnNQaA==; hstud=mruqekuo22060315; Hm_lvt_a3e2ff554f3229fd90bcfe77f75b9806=1654242704; Hm_lpvt_a3e2ff554f3229fd90bcfe77f75b9806=1654244730; _ga_Q14GVGCL77=GS1.1.1654242704.1.1.1654244743.0',
    'referer': 'https://www.huashi6.com/'
}#模拟浏览器headers


def main():
    url = "https://rt.huashi6.com/front/works/rank_page"
    datalist = getimg(url)
    saveimg(datalist,headers)


def saveimg(datalist,headers):
    try:
        os.chdir('images')

    except:
        os.mkdir('images')  #新建文件夹
        os.chdir('images')
        pass    #已存在就pass
    try:
        os.chdir(str(datetime.date.today()))
    except:
        os.mkdir(str(datetime.date.today()))
        os.chdir(str(datetime.date.today()))


    for i in range(len(datalist)):
        #构造链接
        baseurl = 'https://img2.huashi6.com/' + datalist[i]
        #保存图片
        result = requests.get(url=baseurl, headers=headers)
        with open( str(i+1) + '.jpg', mode='wb') as f:
            f.write(result.content)
        print("第%d张图片保存完毕"%(i+1))


def getimg(url): #爬取网页
    datalist = []
    for page in range(1,6): #翻页
        data = {'index': page}
        data = askurl(url,data)
        for one in findlink.findall(data):
            #正则表达式匹配
            datalist.append(one)
    return datalist


def askurl(url,data):#获取指定网页内容
    request = requests.post(url=url,headers=headers,data=data)
    datas = ""
    datas = request.text
    return datas


if __name__ == "__main__":
    main()
    print('爬完了')
