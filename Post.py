# Post metodu ile her tür veri gönderilebilir
# veriler adres satırında gözükmeyecek şekilde gönderilir

#post metodu ile bir siteye veri göndermek

import urllib.request
import urllib.parse

adress= "http://github.com"

header={
    'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.0 Safari/537.36'
}

veri= {
"kullanici_adi": "alperen",
"sifre": "123",
"email": "alperenmert@gmail.com",
"isim": "Alperen MERT"
}

#özel karakterlerin şifrelenmesi
parametre = urllib.parse.urlencode(veri)
parametre = parametre.encode('utf-8')

#istek
istek= urllib.request.Request(adress, data=parametre, headers= header)

#isteğin gönderilmesi
html = urllib.request.urlopen(istek)

#kaynak kodu yaz
print(html.read())


