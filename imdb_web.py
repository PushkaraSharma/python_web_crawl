
import bs4
import urllib.request as url
printer = []
while True:

    name = input("Enter Movie name:")
    printer.append("Enter Movie name: ")
    printer.append(name)
    if name == 'quit':
        break

    web = url.urlopen("https://www.imdb.com/find?ref_=nv_sr_fn&q="+name)
    page1 = bs4.BeautifulSoup(web,"lxml")
    b = page1.find('td', class_="result_text")
    href = b.a['href']
    new_link = "https://www.imdb.com"+href
    web_2 = url.urlopen(new_link)
    page_2 = bs4.BeautifulSoup(web_2,"lxml")
    c = page_2.find_all('div', class_="titleBar")
    for name in c:
        d = name.text.replace("\n","")
        x = (d.replace(" ",""))
        print(x)
        printer.append(x)

    summary = page_2.find_all('div',class_="summary_text")
    print("SUMMARY-")
    printer.append("\n SUMMARY:-\n")
    for i in summary:
        print(i.text)
        printer.append(i.text)
    cast = page_2.find_all('table',class_="cast_list")
    for j in cast:
        print(j.text.replace("\n",""))
        printer.append(j.text.replace("\n",""))


    story = page_2.find_all('div',class_="inline canwrap")
    print("\n STORY-")
    printer.append("\n STORY:-\n")
    for k in story:
        print(k.text)
        printer.append(k.text)

output = open("IMDBmovies.txt",'a')
for line in printer:
    output.write(line)
    output.write('\n')

output.close()