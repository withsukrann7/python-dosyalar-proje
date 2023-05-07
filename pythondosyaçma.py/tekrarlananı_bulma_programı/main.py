"""
Soru: Bir metin dosyasında, bir kelimenin kaç kez geçtiğini sayan bir Python programı yazın.
Programın kullanıcıdan kelimeyi girmesini isteyin ve dosyadaki kelimenin kaç kez geçtiğini gösterin.

çıktısı böyle olsun: 

Dosya adı: programming.txt
Aranacak kelime: Python
Dosyada 'Python' kelimesi 2 kez geçiyor.

"""
"""
with open("metin.txt","r",encoding="UTF-8") as f:
   

    liste = []

    name = input(str("aranacak kelimeyi yazınız:"))

    for i in f:
        if name in liste:
            liste[name] += 1
        else:
            liste[name] = 1

    print("toplam geçen sayı:",len(liste[name]))

print("aranan kelime:",name)
print("dosyada {} kelimesi {} kez geçiyor".format(name),(len(liste[name])))
"""


with open("metin.txt","r",encoding="UTF-8") as f:

    liste = {}

    name = input("aranacak kelimeyi yazınız: ")

    for i in f:
        if name in i:
            if name in liste:
                liste[name] += 1
            else:
                liste[name] = 1

    print("aranan kelime:", name)
    if name in liste:
        print("dosyada {} kelimesi {} kez geçiyor".format(name, liste[name]))
    else:
        print("dosyada {} kelimesi geçmiyor".format(name))

