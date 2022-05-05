import requests
from bs4 import BeautifulSoup
from datetime import datetime 

url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll("p","title")
rank = 1

rank_file = open("PythonHW2/practice1.txt", "a",  encoding="UTF-8") # 한글 깨짐 방지 

rank_file.write(str(datetime.today()) + "의 벅스 실시간 차트 순위입니다\n")

for result in results:
    rank_file.write(str(rank) + "위:" + result.get_text() + "\n")
    rank += 1

