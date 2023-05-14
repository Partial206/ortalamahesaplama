print("Eokula uygun şekilde Üretildi")
notsayisi = int(input("Kaç Tane Not Seçmek istersin(max 3 min 2):"))
print(notsayisi,"Not Sayisi Olarak Algılandı")

if notsayisi > 3:
    print("3'ten fazla sözlü notu seçemezsin")
    
    

if notsayisi ==2:
    print("(3.ncü Sözlü notu yoksa 0 yazın yerine) Projeye 100 yazabilirsiniz birşey farketmiyor")

    Not1 = int(input(("Not 1'i Seç:")))
    Not2 = int(input(("Not 2'yi Seç:")))

    Proje1 = int(input(("Proje 1'i Seç:")))
    Proje2 = int(input(("Proje 2'yi Seç:")))

    Sözlü1 = int(input(("Sözlü 1'i Seç:")))
    Sözlü2 = int(input(("Sözlü 2'yi Seç:")))
    Sözlü3 = int(input(("Sözlü 3'ü Seç:")))

    if Not1 and Not2 and Sözlü1 and Sözlü2 and Sözlü3 and Proje2 and Proje1 > 100:
        print("Mantık Hatası Not 100'den fazla olamaz")

    if Sözlü3 == 0:
        Sözlü = (int(float(Sözlü1)+float(Sözlü2))/2)
        Proje = (int(float(Proje1)+float(Proje2))/2)
        Dersetk = (int(float(Sözlü+Proje))/2)
        print((int(float(Not1)+float(Not2)+float(Dersetk))/3))
  
    else:
        Sözlü = (int(float(Sözlü1)+float(Sözlü2)+float(Sözlü3))/3)
        Proje = (int(float(Proje1)+float(Proje2))/2)
        Dersetk = (int(float(Sözlü+Proje))/2)
        print((int(float(Not1)+float(Not2)+float(Dersetk))/3))
    
if notsayisi ==3:
    print("(3.ncü Sözlü notu yoksa 0 yazın yerine) Projeye 100 yazabilirsiniz birşey farketmiyor")
    Not1 = int(input(("Not 1'i Seç:")))
    Not2 = int(input(("Not 2'yi Seç:")))
    Not3 = int(input(("Not 3'ü Seç:")))

    Proje1 = int(input(("Proje 1'i Seç:")))
    Proje2 = int(input(("Proje 2'yi Seç:")))

    Sözlü1 = int(input(("Sözlü 1'i Seç:")))
    Sözlü2 = int(input(("Sözlü 2'yi Seç:")))
    Sözlü3 = int(input(("Sözlü 3'ü Seç:")))
    
    if Not1 and Not2 and Not3 and Sözlü1 and Sözlü2 and Sözlü3 > 100:
        print("Mantık Hatası Not 100'den fazla olamaz")
    
    if Sözlü3 == 0:
        Sözlü = (int(float(Sözlü1)+float(Sözlü2))/2)
        Proje = (int(float(Proje1)+float(Proje2))/2)
        Dersetk = (int(float(Sözlü+Proje))/2)
        print((int(float(Not1)+float(Not2)+float(Not3)+float(Dersetk))/4))

    else:
        Sözlü = (int(float(Sözlü1)+float(Sözlü2)+float(Sözlü3))/3)
        Proje = (int(float(Proje1)+float(Proje2))/2)
        Dersetk = (int(float(Sözlü+Proje))/2)
        Ort = ((int(float(Not1)+float(Not2)+float(Not3)+float(Dersetk))/4))
        print(Ort,"Ortalaman Budur")

