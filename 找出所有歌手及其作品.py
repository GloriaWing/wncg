import xlwt
import requests
from bs4 import BeautifulSoup
import re

url = 'http://music.163.com/discover/artist/cat?id=1001'  # 华语男歌手页面
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate,br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Connection': 'keep-alive',
           'Cookie': '_ntes_nnid=afa94cedb054bd0b4f6d875475dc099c,1552445250414; _ntes_nuid=afa94cedb054bd0b4f6d875475dc099c; _iuqxldmzr_=32; WM_NI=wdFjYORay8vlcGDQwj%2BpRRJFhpOHbDEtFU13zEovwE0IfIp6whmFw0EDqRl93m3AEkDvz1%2F71qPQEgqnloRvZ90mo7Uw5A9faRV%2FY0OSYzQwHt3nnjXLVE8tGTjlf%2BLxYjM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb2e734f2ed82d9fc6aaa868ea6d45f928e9baff23caee8feb5e921a7b0acb4b12af0fea7c3b92ab5bc8a8bdc4592bfb7d9f568a1998cb2f662e9b09eb3c94eacb081a9e15087ac8ab6b439ba9ba197f64ff497aaaaf33eb5b8a3a7f63c879cbfb3ef33f1b3fda2c86188aab6d2ae3df3afa0b2c86db3b2a490d17e9ae7008eee3d97a9fba2bc6ea38e9ad0dc3c8d8d979bd47d8cacfd8fed629c949aa6bb80858ca68de52190a8978bd037e2a3; WM_TID=gETjjhqFBqZEAFEVRFI4gitnTnqL4ZSn; JSESSIONID-WYYY=6fHVNFEbQrvIo6ADtMfCfkUQWKTQAknF5lcR7EodsQXtuodbWglAxH%5CWJ%5CPd2obaJ8i8EYkbU4x5DbFrtECpUMthUAX2HogFc98V4felv27I0r8nvSQ9wUHCk3aUN4aekDrUDbUVhXm27se%5CF%2FmZ29b7JErQCBFzd8gRB%2BNkRrdjVspk%3A1552460447693',
           'Host': 'music.163.com',
           'Referer': 'http://music.163.com/',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/66.0.3359.181 Safari/537.36'}
r = requests.get(url, headers=headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
html = r.text  # 获取整个网页


soup = BeautifulSoup(html, 'lxml')  #
top_10 = soup.find_all('div', attrs={'class': 'u-cover u-cover-5'})
print(top_10)


singers = []
for i in top_10:
    singers.append(re.findall(r'.*?<a class="msk" href="(/artist\?id=\d+)" title="(.*?)的音乐"></a>.*?', str(i))[0])


url = 'http://music.163.com'
for singer in singers:
    try:
        new_url = url + str(singer[0])
        # print(new_url)
        songs = requests.get(new_url, headers=headers).text
        soup = BeautifulSoup(songs, 'html.parser')
        Info = soup.find_all('textarea', attrs={'style': 'display:none;'})[0]
        songs_url_and_name = soup.find_all('ul', attrs={'class': 'f-hide'})[0]
        # print(songs_url_and_name)
        datas = []
        data1 = re.findall(r'"album".*?"name":"(.*?)".*?', str(Info.text))
        data2 = re.findall(r'.*?<li><a href="(/song\?id=\d+)">(.*?)</a></li>.*?', str(songs_url_and_name))

        for i in range(len(data2)):
            datas.append([data2[i][1], data1[i], 'http://music.163.com/#' + str(data2[i][0])])
        # print(datas)
        book = xlwt.Workbook()
        sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
        sheet1.col(0).width = (25 * 256)
        sheet1.col(1).width = (30 * 256)
        sheet1.col(2).width = (40 * 256)
        heads = ['歌曲名称', '专辑', '歌曲链接']
        count = 0

        for head in heads:
            sheet1.write(0, count, head)
            count += 1

        i = 1
        for data in datas:
            j = 0
            for k in data:
                sheet1.write(i, j, k)
                j += 1
            i += 1
        book.save(str(singer[1]) + '.xls')  # 括号里写存入的地址

    except:
        continue


