powitanie = input("Podaj swoje imię")
powitanie2 =input("Cześć " + powitanie + " miło mi Ciebie poznać, jest to program przeliczający waluty.Czy jesteś zainteresowany/zainteresowana")
if powitanie2 == "Tak" or powitanie2 == "tak":
    print("Dobrze w takim razie podaj walutę, którą chcesz przeliczyć (Do wyboru masz dolar, funt, złotówka)")
else:
    print("Dobrze w takim razie dziękuje i życzę miłego dnia")
    import sys
    sys.exit(0)
while True:
    waluta = input("Waluta którą chcesz przeliczyć: ")
    if waluta == "dolar" or waluta == "Dolar":
            print("Wybrałeś/aś pierwszą walutę dolar, na jaką walutę chcesz ją przeliczyć? (funt, złotówka)")
    elif waluta == "funt" or waluta == "Funt":
            print("Wybrałeś/aś pierwszą walutę funt, na jaką walutę chcesz ją przeliczyć? (dolar, złotówka)")
    elif waluta == "złotówka" or waluta == "Złotówka":
            print("Wybrałeś/aś pierwszą walutę złotówka, na jaką walutę chcesz ją przeliczyć? (dolar, funt)")
    else:
            print("Wybrałeś/aś walutę której nie obsługujemy")
    waluta2 = input("Waluta na którą chcesz przeliczyć: ")
    if waluta == waluta2:
        print("Kwota będzie taka sama :)")
    elif waluta2 == "dolar" or waluta2 == "Dolar":
        print("Wybrałeś/aś drugą walutę dolar, jaką kwotę chciałabyś/chciałbyś przeliczyć?")
    elif waluta2 == "funt" or waluta2 == "Funt":
        print("Wybrałeś/aś drugą walutę funt, jaką kwotę chciałabyś/chciałbyś przeliczyć?")
    elif waluta2 == "złotówka" or waluta2 == "Złotówka":
        print("Wybrałeś/aś drugą walutę złotówka, jaką kwotę chciałabyś/chciałbyś przeliczyć?")
    else:
        print("Wybrałeś/aś walutę której nie obsługujemy")
    print("Kwota:")
    suma = float(input())
    if suma <= 0:
        print("Kwota nie może być mniejsza ani równa 0")
    elif suma > 0:
        print("Kwota którą podałeś to " + str(suma))
    else:
        print("Musisz podać kwotę")
    print("Wpisz po jakim kursie chcesz przeliczyć pieniądze: ")
    kurs = float(input())
    podsumowanie = input(
        "Podsumujmy wybrałeś/aś walutę " + waluta + " żeby przeliczyć ją na walutę " + waluta2 + " a wartość którą chcesz przeliczyć to "
        + str(suma) + ". Całość rozliczamy po kursie: " + str(kurs) + " Czy to się zgadza?")
    if podsumowanie == "tak" or podsumowanie == "Tak":
        print()
    elif podsumowanie == "nie" or podsumowanie == "Nie":
        print()
    else:
        print("Musisz odpowiedzieć tak lub nie")
    rozliczenie = suma * kurs
    całość = print("Przeliczenie : " + str(suma) + " " + waluta + " = " + str(kurs) + " " + waluta2)
    reply = input("Czy chcesz powtórzyć przeliczenie? ")
    if reply.strip().lower() not in ('tak', 'Tak'):
        break
