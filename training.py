# araba1=int(input("Hızı Giriniz"))
# araba2=int(input("Hızı Giriniz"))

# cıkart=(araba1-araba2) 

# if cıkart > 0  :
#   print("Araba1 Önde")
# else:
#   print("Araba1 Geride")

g=float(9.8)
Ks=float(2.3)
top=int(input("Hızı Giriniz"))
h=int(input("yükseklik Giriniz"))
saniye=int(input("Süreyi Giriniz"))
maxhız1=(top - (g + Ks)*saniye)
maxhız2=(top + (g+Ks)*h)

if h > 1:
  print(maxhız2)
else:
  print(maxhız1)  



