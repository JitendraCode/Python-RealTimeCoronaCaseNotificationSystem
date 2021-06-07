from plyer import notification
import icon
import IPython
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon = ("C://Users//lenovo//Desktop//realtimecorona//icon.ico"),
        timeout= 10
    )
def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    notifyMe("Hey Jitu"," Let's stop the spread of this virus together" )
    myHtmlData=getData('https://www.mohfw.gov.in/')

    soup=BeautifulSoup(myHtmlData, 'html.parser')
    #  print(soup.prettify().encode("utf-8"))
    myDataStr=""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr=myDataStr[1: ]
    itemlist=myDataStr.split("\n\n")

    states=['Chandigarh','Telangana', 'Maharashtra']
    for item in itemlist[0:22]:
        datalist=item.split('\n')
        if datalist[1] in states:
            print(datalist)
            nTitle='Cases of Covid-19'
            nText=f"{datalist[1]}\n Indian:{datalist[2]}\n Foreign: {datalist[3]}\n Cured: {datalist[4]}\n Deaths: {datalist[5]}"
            notifyMe(nTitle, nText) 
            time.sleep(2)



    