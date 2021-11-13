import urllib3
import io, time, sys, re
import argparse
import itertools
from bs4 import BeautifulSoup
from urllib.parse import urlparse

appName = sys.argv[0]

parser = argparse.ArgumentParser(usage="python {} --author 'dedy affandy' or --abstract 'digital forensik' or --title 'digital forensik'". format(appName), epilog="HAPPY SCRAPING !")
parser.add_argument("--author", "--keyword", help="Search By keyword author. Ex --author 'Dedy Affandy'", type=str, nargs="?")
parser.add_argument("--abstract", help="Search By keyword abstract Ex : --abstract 'digital forensik' ", nargs="?")
parser.add_argument("--title", help="search By keyword title. Ex : --title 'digital forensik' ", nargs="?")

args = parser.parse_args()


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()

def Title():

    url = http.request("GET", "https://garuda.kemdikbud.go.id/documents?select=title&q={}".format(args.title.replace(" ", "+")))
    data = url.data
    bs = BeautifulSoup(data, 'lxml')
    divPage = bs.find('div', {"class": "page-column"})
    pageNum = divPage.find('a', {"class": "ui mini icon button page-button"})
    regexNum = re.findall(r'page=([^&]*)', pageNum['href'])
    # print(regexNum[0])
    regexNum = int(regexNum[0])
    for i in range(1, regexNum+1):
        url = http.request("GET", "https://garuda.kemdikbud.go.id/documents?page={}&q={}&select=title".format(i, args.title.replace(" ", "+")))
        data = url.data

        bs = BeautifulSoup(data, 'lxml')
        search_body = bs.find('body')
        div_search = bs.find_all('div', {"class": "article-item"})
        div_search_ab = bs.find_all('div', {"class": "abstract-article"})


        for divS, divAb in zip(div_search, div_search_ab):
            divSearchAll_ta = divS.find('a', {"class": "title-article"})
            divSearchAll_auA = divS.findAll('a')
            # print(divSearchAll_auA[4])
            Judul = divSearchAll_auA[0].text.replace("\n", "")
            author1= divSearchAll_auA[1].text.replace("\n", "")
            author2 = divSearchAll_auA[2].text.replace("\n", "")
            if "Show Abstract" in author2:
                author2 = ""
            author3 = divSearchAll_auA[3].text.replace("\n", "").replace("Download Original","")
            if "Show Abstract" in author3 :
                author3 = ""
            author4 = divSearchAll_auA[4].text.replace("\n", "")
            if "Show Abstract" in author4:
                author4 = ""
            
            with io.open("data/title/{}.ris".format(args.title.replace(" ", "+")), 'a', encoding='utf-8') as nulis:
                nulis.write("TI  - CONF\nTI  - {}\nAU  - {}\nAU  - {}\nAU  - {}\nER  - \n".format(Judul, author1, author2, author3, author4))
                nulis.close()
                time.sleep(0.5)

def Abst():
    url = http.request("GET", "https://garuda.kemdikbud.go.id/documents?select=abstract&q={}".format(args.abstract.replace(" ", "+")))
    data = url.data
    bs = BeautifulSoup(data, 'lxml')
    divPage = bs.find('div', {"class": "page-column"})
    pageNum = divPage.find('a', {"class": "ui mini icon button page-button"})
    regexNum = re.findall(r'page=([^&]*)', pageNum['href'])
    # print(regexNum[0])
    regexNum = int(regexNum[0])
    for i in range(1, regexNum+1):
        url = http.request("GET", "https://garuda.kemdikbud.go.id/documents?page={}&q={}&select=abstract".format(i, args.abstract.replace(" ", "+")))
        data = url.data

        bs = BeautifulSoup(data, 'lxml')
        search_body = bs.find('body')
        div_search = bs.find_all('div', {"class": "article-item"})
        div_search_ab = bs.find_all('div', {"class": "abstract-article"})


        for divS, divAb in zip(div_search, div_search_ab):
            divSearchAll_ta = divS.find('a', {"class": "title-article"})
            divSearchAll_auA = divS.findAll('a')
            # print(divSearchAll_auA[4])
            Judul = divSearchAll_auA[0].text.replace("\n", "")
            author1= divSearchAll_auA[1].text.replace("\n", "")
            author2 = divSearchAll_auA[2].text.replace("\n", "")
            if "Show Abstract" in author2:
                author2 = ""
            author3 = divSearchAll_auA[3].text.replace("\n", "").replace("Download Original","")
            if "Show Abstract" in author3 :
                author3 = ""
            author4 = divSearchAll_auA[4].text.replace("\n", "")
            if "Show Abstract" in author4:
                author4 = ""
            
            with io.open("data/abstract/{}.ris".format(args.abstract.replace(" ", "+")), 'a', encoding='utf-8') as nulis:
                nulis.write("TI  - CONF\nTI  - {}\nAU  - {}\nAU  - {}\nAU  - {}\nER  - \n".format(Judul, author1, author2, author3, author4))
                nulis.close()
                time.sleep(0.5)
def Auth():
    url = http.request("GET", "https://garuda.kemdikbud.go.id/documents?select=author&q={}".format(args.author.replace(" ", "+")))
    data = url.data
    bs = BeautifulSoup(data, 'lxml')
    divPage = bs.find('div', {"class": "page-column"})
    pageNum = divPage.find('a', {"class": "ui mini icon button page-button"})
    regexNum = re.findall(r'page=([^&]*)', pageNum['href'])
    # print(regexNum[0])
    regexNum = int(regexNum[0])
    for i in range(1, regexNum+1):
        url = http.request("GET", "https://garuda.kemdikbud.go.id/documents?page={}&q={}&select=author".format(i, args.author.replace(" ", "+")))
        data = url.data

        bs = BeautifulSoup(data, 'lxml')
        search_body = bs.find('body')
        div_search = bs.find_all('div', {"class": "article-item"})
        div_search_ab = bs.find_all('div', {"class": "abstract-article"})


        for divS, divAb in zip(div_search, div_search_ab):
            divSearchAll_ta = divS.find('a', {"class": "title-article"})
            divSearchAll_auA = divS.findAll('a')
            # print(divSearchAll_auA[4])
            Judul = divSearchAll_auA[0].text.replace("\n", "")
            author1= divSearchAll_auA[1].text.replace("\n", "")
            author2 = divSearchAll_auA[2].text.replace("\n", "").replace("Download Original","").replace("Original Source","")
            if "Show Abstract" in author2:
                author2 = ""
            author3 = divSearchAll_auA[3].text.replace("\n", "").replace("Download Original","").replace("Original Source","")
            if "Show Abstract" in author3 :
                author3 = ""
            author4 = divSearchAll_auA[4].text.replace("\n", "").replace("Download Original","").replace("Original Source","")
            if "Show Abstract" in author4:
                author4 = ""
            
            with io.open("data/author/{}.ris".format(args.author.replace(" ", "+")), 'a', encoding='utf-8') as nulis:
                nulis.write("TI  - CONF\nTI  - {}\nAU  - {}\nAU  - {}\nAU  - {}\nER  - \n".format(Judul, author1, author2, author3, author4))
                nulis.close()
                time.sleep(0.5)

def main():
    if args.abstract :
        Abst()
    if args.author :
        Auth()
    if args.title :
        Title()

if __name__ == "__main__":
    main()
