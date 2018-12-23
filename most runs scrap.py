import urllib.request as url
import bs4
import csv

web =url.urlopen("http://stats.espncricinfo.com/ci/content/records/83548.html")
page = bs4.BeautifulSoup(web,'lxml')
b = page.find('table',class_="engineTable")
rows = b.find_all('tr')

scvfile = open("score.csv",'w',newline='')
writer = csv.writer(scvfile)

for row in rows:
    csvrow = []
    for cell in row.findAll(['td','th']):
        csvrow.append(cell.get_text())
    writer.writerow(csvrow)

scvfile.close()
