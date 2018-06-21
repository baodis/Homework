import requests 
from bs4 import BeautifulSoup
import time

session = requests.Session()
session.verify = False
requests.packages.urllib3.disable_warnings() 

url = 'https://store.steampowered.com/search/?filter=globaltopsellers&os=win'
while True:
	try:
		resp = session.get(url)
		data = resp.content
		
		soup = BeautifulSoup(data, 'html.parser')
		count = 0
		rank = []		

		for itemText in soup.find_all('span', attrs={'class':'title'}):
			count = count + 1
			print("%d %s" % (count, itemText.string))
			rank.append(itemText.string)
			
		if "Dead by Daylight" and "PLAYERUNKNOWN'S BATTLEGROUNDS" in rank:
			print("데바데가 갓겜들 사이에 껴있군\n")
			
			dbdrank = rank.index("Dead by Daylight")+1			
			raftrank = rank.index("Raft")+1

			print("역시 데바데(%d등)가 최고!!" % dbdrank) if dbdrank < raftrank else print("하지만 래프트(%d등)보단 못하군" % raftrank)
			
		else:
			print("데바데 망함 - %s 등함ㅋ" % str(rank.index("Dead by Daylight")+1))
		
		time.sleep(10)
	except Exception as e:
		print(e)