import os

txtyaz= []


# görev istediğin kadar belirle
adet = int(input("KAÇ GÖREV EKLEMEK İSTERSİNİZ "))
g = input("Gün Nedir: ")
t = input("Tarih Nedir: ")
i = 0
while(i<adet):
     gör = input("Görevler Nedir: ")
     txtyaz.append({
           "gün" : g,
           "tarih" : t,
           "görev" : gör

     })
     i += 1



print(txtyaz)
with open('Years All Görev List.txt', 'w') as f:
    for item in txtyaz:
        f.write(f"%s\n" % item+ "\n")


# .txt dosyasına yaz

