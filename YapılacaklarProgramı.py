yapilacaklar = []

def gorevekle(yapilacaklar):
    Gorev = input("Yapılacak görevi girin: ")
    yapilacaklar.append(Gorev)
    print("Görev başarıyla eklendi.")

def gorevlerigoster(yapilacaklar):
    print("Yapılacak Görevler: ")
    for Gorev in yapilacaklar:
        print("- " + Gorev)

def gorevsil(yapilacaklar):
    Gorev = input("Silmek istediğiniz görevi girin: ")
    if Gorev in yapilacaklar:
        yapilacaklar.remove(Gorev)
        print("Görev başarıyla silindi.")
    else:
        print("Görev bulunamadı.")


while True:
    print("\nYapılacaklar Listesi Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çıkış")
    choice = input("Seçiminiz (1/2/3/4): ")

    if choice == "1":
        gorevekle(yapilacaklar)
    elif choice == "2":
        gorevlerigoster(yapilacaklar)
    elif choice == "3":
        gorevsil(yapilacaklar)
    elif choice == "4":
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
