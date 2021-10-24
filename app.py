import requests
import smtplib
import time
from bs4 import BeautifulSoup



url = 'https://www.hepsiburada.com/msi-modern-14-b10mw-271xtr-intel-core-i5-10210u-8gb-256gb-ssd-freedos-14-fhd-tasinabilir-bilgisayar-p-HBV0000147C06'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'} # you can find your user agent by searching "my user agent" on Google



def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='product_name').get_text().strip()
    title = title[0:13]
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print(price,'₺') # you can chenge the currency
    if(price < 12500): # we said, remind me when the price is under 12500₺
        send_mail(title)

        
def send_mail(title):
    sender = 'justanexample@gmail.com'
    receiver = 'justanotherexample@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo() # starting the server
        server.starttls() # we need that line to provide security of the server connection
        server.login(sender,'lmrgqztjhyezblsk') # we are signing up to mail system here. so, we should enter the password here
        # you can get that password from the net by searching "gmail app passowrd" and clicking on the googlemyaccount link.
        subject = title + ' is at discount'
        body = 'You can reach there from the link => ' + url
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,receiver,mailContent)
        print('Mail sent!')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

        
        
while(1):
    check_price()
    time.sleep(60*60) # check the price once per hour
