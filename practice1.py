import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://music.bugs.co.kr/chart"
rp = requests.get(url)
bs = BeautifulSoup(rp.text, "html.parser")
rs = bs.findAll("p","title")
rank = 1
rs_file = open("./practice1.txt", "w",  encoding="UTF-8")
rs_file.write(str(datetime.today()) + "의 벅스 실시간 차트 순위입니다\n")
for i in rs:
    rs_file.write(str(rank) + "위:" + i.get_text() + "\n")
    rank =rank+1