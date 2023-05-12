import random
import time

print("""*******************************
SAYI TAHMİN OYUNU


1 ile 40 arasındaki sayıları tahmin edin..

*******************************""")

rastgele_sayı = random.randint(1,40)

tahmin_hakkı = 7
while True:
    tahmin = int(input("Tahmininiz:"))

    if(tahmin < rastgele_sayı):
        print("Bilgiler sorgulanıyor....")
        time.sleep(2)
        print("Daha yüksek bir sayı söyleyin..")

        tahmin_hakkı -= 1

    elif(tahmin > rastgele_sayı ):
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Daha düşük bir sayı söyleyin")

        tahmin_hakkı -= 1

    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(2)
        print("Tebrikler! Sayınız:",rastgele_sayı)
        break
    if(tahmin_hakkı == 0):
        print("Tahmin hakkınız ne yazık ki kalmadı...")
        time.sleep(3)
        print("Tahmin etmeniz gereken sayı",rastgele_sayı)

        break