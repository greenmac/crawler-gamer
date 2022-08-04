from bs4 import BeautifulSoup
import requests
import os

from utils import timer

@timer
def crawlerGamerInfo():
    url = 'https://gnn.gamer.com.tw/' # 巴哈姆特 GNN
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    resp = requests.get(url, headers=headers)
    resp_results = resp.text
    soup = BeautifulSoup(resp_results, 'lxml')
    soup_img = soup.select('.GN-lbox2E')
    
    if not os.path.exists("images"):
        os.mkdir("images")  # 建立資料夾
        
    for i in soup_img:
        img_url = i.select('img')[0].get('src')
        resp_img_title = img_url.replace('https://p2.bahamut.com.tw/S/2KU/', '').split('/')
        resp_img_title = resp_img_title[0]+'_'+resp_img_title[1]
        resp_img = requests.get(img_url)  # 下載圖片
        
        print(img_url)
        print('-'*20)
        
        with open(f'./images/{resp_img_title}.jpg', 'wb') as file:  # 開啟資料夾及命名圖片檔
            file.write(resp_img.content)

if __name__ == '__main__':
    crawlerGamerInfo()