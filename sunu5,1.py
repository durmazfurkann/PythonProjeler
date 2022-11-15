# isim=input("isminizi Giriniz")
# yas=int(input("Yaşınızı Giriniz"))

# if isim =="HALİL" :
#     print("Merhaba Halil")
# elif yas < 12:
#     print("Sen Halit Değilsin")
# elif yas > 80:
#     print("Burda Ne İşin Var amca")    




# sayi=int(input("Lütfen Bir Sayı Giriniz"))
# islem=(sayi%2)

# if islem==0:
#    print("Seçilen Sayı Çift Sayıdır")

# elif islem  !=0 :
#     print("Seçilen Sayı Tek Sayıdır")




# harf=str(input("Lütfen Alfabeden Bir Harf Giriniz"))

# if harf ==("a" or "e" or "i" or "u") :
#     print("Girdiğiniz harf olan", harf, "sesli harfdir")
# elif harf !=("a" or "e" or "i" or "u")  :
#     print("Girdiğiniz harf olan", harf, "sessiz harfdir")    




aylar=input("Bir Ay Giriniz")

if aylar =="Ocak" or aylar == "ocak" or aylar == "Mart" or aylar == "mart" or aylar == "Mayıs" or aylar == "mayıs" or aylar == "Temmuz" or aylar == "temmuz" or aylar == "Ağustos" or aylar == "ağustos" or aylar == "Ekim" or aylar == "ekim" or aylar == "Aralık" or aylar == "aralık":
   print("31 gündür")
elif aylar=="Şubat" or aylar == "şubat":
    print("29 gündür")
else:
    print("30 gündür")