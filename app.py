import requests
import smtplib
from bs4 import BeautifulSoup

url = 'https://www.hepsiburada.com/msi-modern-14-b10mw-271xtr-intel-core-i5-10210u-8gb-256gb-ssd-freedos-14-fhd-tasinabilir-bilgisayar-p-HBV0000147C06'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    title = title[0:13]
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print(price,'₺')
    if(price < 3500):
        send_mail()



def send_mail():
    sender = 'leoanderson633@gmail.com'
    receiver = 'lasln393@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,'')