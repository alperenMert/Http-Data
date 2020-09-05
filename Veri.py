# Üye kayıt için siteye veri gönderilmek isteniyor

import urllib.parse

# Gönderilmek istenen veriler sözlüğe eklendi
veri= {
    "kullanici_adi":"alperen",
    "sifre":"123",
    "email":"alperenmert@gmail.com",
    "isim":"Alperen MERT"
}

satir =urllib.parse.urlencode(veri) #sözlük url yapısı haline getirildi

print(satir)
print()

# bu şekilde veri gönderiminde boşluklar ve özel karakterler (@) yanlış anlaşılmayacak ve karşı taraf kolaylıkla okuyabilecek

