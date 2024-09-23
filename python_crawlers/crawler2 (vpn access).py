import requests
from bs4 import BeautifulSoup
import time
import random

# 定義一個函數來進行網頁請求，並包含代理與重試機制
def fetch_page(url, headers=None, proxies=None, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            # 檢查是否成功回應
            if response.status_code == 200:
                return response
            else:
                print(f"Error {response.status_code}, retrying...")
        except requests.RequestException as e:
            print(f"Request failed: {e}, retrying...")
        retries += 1
        time.sleep(random.uniform(1, 3))  # 隨機等待1-3秒
    raise Exception(f"Failed to fetch page after {max_retries} retries")

# 主程序
def main():
    url = 'https://www.wikipedia.org'  # 替換成你要爬的目標網址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    # 設置代理（帶身份驗證）
    proxies = {
        'http': 'http://HN73917750:a1228hsy@202.39.62.153:0.0.0.0',
        'https': 'http://HN73917750:a1228hsy@202.39.62.153:0.0.0.0',
    }
    
    try:
        # 爬取頁面
        response = fetch_page(url, headers=headers, proxies=proxies)
        print("Page fetched successfully!")
        
        # 解析頁面
        soup = BeautifulSoup(response.content, 'lxml')
        print(soup.title.get_text())  # 範例：打印網頁標題
        
    except Exception as e:
        print(f"Failed to scrape the page: {e}")

# 執行主程序
if __name__ == "__main__":
    main()
