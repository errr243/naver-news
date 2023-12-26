import requests
import json
from bs4 import BeautifulSoup
import datetime
import time

# 텔레그램 봇 설정
bot_token = "6413288318:AAF5zNXhGqJLFDJbPn63ux0Yj6Bq6qIBGjQ"
chat_id = "6536235574"

def send_message(message):
    data = {"chat_id": chat_id, "text": message}
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, data=data)

def send_news():
    keyword = "AI"  # 뉴스 검색 키워드
    url = f"https://search.naver.com/search.naver?where=news&query={keyword}"
    res = requests.get(url)

    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        news_title = soup.select(".news_tit")

        title_list = []
        for title in news_title:
            title_list.append(f"{title.text}\n{title['href']}")

        message = "\n\n".join(title_list)
        send_message(message)

def main():
    last_sent = None
    while True:
        try:
            now = datetime.datetime.now()
            start_time = datetime.time(8, 0, 0)

            if now.time() >= start_time and (last_sent is None or last_sent != now.date()):
                send_news()
                last_sent = now.date()

            time.sleep(3600)  # 1시간 동안 대기

        except Exception as e:
            print(e)
            time.sleep(3600)

if __name__ == "__main__":
    main()
