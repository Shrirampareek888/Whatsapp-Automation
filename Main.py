# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:51:59 2020

@author: shrir
"""
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def news():
    import urllib.request
    from bs4 import BeautifulSoup as bs
    content = urllib.request.urlopen('https://inshorts.com/en/read/').read()
    soup = bs(content,'html.parser')
    cntr=1;
    headlines = []
    links = []
    for headline in soup.find_all('span',attrs={'itemprop':'headline'}):
        if cntr==8:
            break
        headlines.append(headline.text)
        cntr+=1
    cntr=1
    tp = 'https://inshorts.com'
    for link in soup.find_all('a',attrs={'class':'clickable'}):
        if cntr==8:
            break
        links.append(tp+link.get('href'))
        cntr+=1
    ans = ''
    for i in range(0,len(links)):
        ans+=headlines[i]+'\n'
        #ans+=links[i]+'\n'
        ans+='\n'
    return ans


def tweets():
    import urllib.request
    from bs4 import BeautifulSoup as bs
    content = urllib.request.urlopen('https://trends24.in/india/').read()
    soup = bs(content,'html.parser')
    cntr=1
    f=0
    ans=''
    for trends in soup.find_all('li',attrs={'class':''}):
        for b in trends.find_all('a'):
            ans += b.text+'\n'
            cntr+=1
            if cntr==6:
                f=1
                break
        if f==1:
            break
    return ans
    
def price():
    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen
    site= "https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-mumbai.cms"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('span',attrs={'class':'fuel-price'}):
        ans = 'Petrol Price (Mumbai):\n'
        ans+='₹ '+fp.text+'\n'
    site= "https://economictimes.indiatimes.com/wealth/fuelprices/fuel-diesel,citystate-mumbai.cms"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('span',attrs={'class':'fuel-price'}):
        ans+='Diesel Price (Mumbai):\n'
        ans+='₹ '+fp.text+'\n'
    site= "https://www.goodreturns.in/gold-rates/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('strong',attrs={'id':'el'}):
        ans+='Gold Price per gram (22 ct):\n'
        ans+=fp.text.strip()+'\n'
    site= "https://www.goodreturns.in/silver-rates/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('strong',attrs={'id':'el'}):
        ans+='Silver Price per gram:\n'
        ans+=fp.text.strip()+'\n'
    site= "https://economictimes.indiatimes.com/indices/sensex_30_companies?from=mdr"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('div',attrs={'id':'ltp'}):
        ans+='Sensex:\n'
        ans+=fp.text.strip()+'\n'
    site= "https://economictimes.indiatimes.com/indices/nifty_50_companies"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    for fp in soup.find_all('div',attrs={'id':'ltp'}):
        ans+='Nifty:\n'
        ans+=fp.text.strip()+'\n'
    return ans
    

def quote():
    
    site= "https://www.brainyquote.com/quote_of_the_day"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,features='lxml')
    cntr=1
    for quote in soup.find_all('a',attrs={'title':'view quote'}):
        ans = quote.text.strip()
        if(cntr==2):
            break
        cntr+=1
    return ans

def contests():
    import urllib.request
    from bs4 import BeautifulSoup as bs
    from datetime import datetime, timedelta
    contests = []
    time = []
    website=[]
    content = urllib.request.urlopen('https://clist.by/').read()
    soup = bs(content,'html.parser')
    for taga in soup.find_all('div',attrs={'class':'row contest coming'}):
        for timeb in taga.find_all('div',attrs={'class':'col-md-5 col-sm-12 start-time'}):
            temp = timeb.text.strip()
            time.append(temp)
              
        for tagc in taga.find_all('span',attrs={'class':'contest_title'}):
            s = tagc.text.strip()
            contests.append(s)
            for site in taga.find_all('div',attrs={'class':'resource'}):
                website.append(site.text.strip())
    #converter
    times =[]
    for ti in time:
        utcmoment_naive = datetime.strptime(ti, "%d.%m %a %H:%M")
        utcmoment = utcmoment_naive + timedelta(hours = 5,minutes = 30)
        timestampStr = utcmoment.strftime("%d.%m %a %H:%M")
        times.append(timestampStr)
        
    x=datetime.now().day
    y=datetime.now().month
    x1="{0:0=2d}".format(x)
    x2="{0:0=2d}".format(y)
    tday = str(x1)+"."+str(x2)
    ftime =[]
    for i in times:
        if tday in i:
            ftime.append(i);
    ans = ''
    for i in range(0,len(ftime)):
        ans+=website[i]+' - '+contests[i]+' - '+ftime[i]+'\n\n'
    return ans
def cont():
    res = "\n*😊Good Morning😊*\n\n*😇Today's Quote😇*\n\n"
    res += quote() + '\n\n\n*💰Commodities And Indices💸:*\n'
    res += price()
    res+='\n*🔥Trending #Hashtags🔥:*\n'
    res+=tweets()
    res+='\n\n*📰Newsℹ️:*\n'
    res+=news()
    res+='\n\n*🏆Contests🏆:*\n'
    res+=contests()
    res+='\n\n*Enjoy Your Day!💪😇*'
    return res

