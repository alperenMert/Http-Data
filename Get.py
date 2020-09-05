#verilerin get metodu ile gönderilmesi
#get metodu ile site adresi ve verilerimiz birleştirilerek okunur
# sadece yazı(Text) gönderilebilir (resim,dosya ses vb. gönderilemez)
#adres ile verileri birleştirmek iin (?) karakteri kullanılır

#üye kayıt bilgilerinin siteye get ile gönderilmesi

import urllib.request
import urllib.parse

#veri gönderilecek site adresi
adress="http://google.com"

header={
    'User_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.0 Safari/537.36'
}

#siteye gönderilecek veriler
veri={
    "kullanici_adi": "alperen",
    "sifre": "123",
    "email": "alperenmert@gmail.com",
    "isim": "Alperen MERT"
}

#siteye gönderilecek verilerin özel karakterlerini şifreliyoruz
parametre = urllib.parse.urlencode(veri)

#sitenin tam adının oluşturulması
site_adress=adress + "?" + parametre

#istek
istek= urllib.request.Request(site_adress, headers= header)

#isteğin gönderilmesi
html= urllib.request.urlopen(istek)

#kaynak kodun ekrana yazılması
print(html.read())
