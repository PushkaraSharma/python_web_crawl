import urllib.request as url
import bs4
import csv
import pandas as pd
web = url.urlopen("http://stats.espncricinfo.com/ci/content/records/283279.html")
page1 = bs4.BeautifulSoup(web,"lxml")
b = page1.find("table",class_="engineTable")
rows = b.find_all('tr')
csvfile = open("data.csv",'w',newline='')
writer = csv.writer(csvfile)

for row in rows:
    csvrow =[]
    for cell in row.findAll(['td','th']):
        csvrow.append(cell.get_text())
    writer.writerow(csvrow)

csvfile.close()