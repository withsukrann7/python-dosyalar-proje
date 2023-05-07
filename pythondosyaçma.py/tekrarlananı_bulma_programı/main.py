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
