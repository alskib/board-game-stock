import urllib2
import re
from bs4 import BeautifulSoup as bs



def csi(soup):
    title_text = re.match(r"(.*)(?=\s) \|", soup.title.text).group(1)
    tag = soup.find("p", class_="stock")
    print "[CSI] -", tag.text, "|", title_text

def miniature_market(soup):
    title_text = re.match(r"(.*?)(?= NewArrival|$)", soup.title.text).group(1)
    tag = soup.find("p", class_="availability")
    tag_text = re.match(r"(Availability: (.*)[\s]?)", tag.text).group(2)
    print "[MM] -", tag_text, "|", title_text

def boardgamebliss(soup):
    title_text = re.match(r"(.*?)Buy (.*?)(?=\s\W\sBoard)", soup.title.text, re.DOTALL).group(2)
##    title_text = soup.title.text
    tag = soup.find("div", id="sold-out")
    print "[BGB] - Out of Stock" if tag else "[BGB] - In Stock", "|", title_text
        

def main():
    csi_list = []
    csi_list.append('http://www.coolstuffinc.com/p/197671')
    csi_list.append('http://www.coolstuffinc.com/p/183423')
    csi_list.append('http://www.coolstuffinc.com/p/184149')

    mm_list = []
    mm_list.append('http://www.miniaturemarket.com/mfg3501.html')
    mm_list.append('http://www.miniaturemarket.com/bezsubu.html')
    mm_list.append('http://www.miniaturemarket.com/asmkem01.html')

    bgb_list = []
    bgb_list.append('http://www.boardgamebliss.com/products/caverna-the-cave-farmers')

    for u in csi_list:
        csi(bs(urllib2.urlopen(u)))

    for u in mm_list:
        miniature_market(bs(urllib2.urlopen(u)))

    for u in bgb_list:
        boardgamebliss(bs(urllib2.urlopen(u)))

main()
