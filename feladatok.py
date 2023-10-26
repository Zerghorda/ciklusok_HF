def fel1(szam):
    print("1.fel")
    i: int = 0
    while i <= szam:
        if i % 3 == 0:
            if i == szam or i == szam-2 or i == szam-1:
                print(i, end="")
            else:
                print(i, end=",")
        i += 1


def fel2():
    print("2.fel")
    szam: int = int(input("Adjon meg egy pozitiv számot!"))
    while szam > 0:
        if szam == 1:
            print(szam, end="")
        else:
            print(szam, end=";")
        szam -= 1


def fel3():
    print("3.fel")
    szam: int = int(input("Adjon meg egy öttel osztható számot!"))
    if szam % 5 == 0:
        print("Öttel osztható!")
    while szam % 5 != 0:
        szam: int = int(input("Öttel oszthatónak kell ,hogy legyen!"))
        if szam % 5 == 0:
            print("Öttel osztható!")


def fel4(szam):
    print("4.fel")
    i: int = 0
    if szam < 0:
        print("Hiba:pozitivnek kell ,hogy legyen !")
    while i <= szam:
        if i % 6 == 0 and i == szam:
            print("BUMMBAM", end="")
        elif i % 6 == 0:
            print("BUMMBAM", end=",")
        elif i == szam and i % 3 == 0:
            print("BOOM", end="")
        elif i % 3 == 0:
            print("BOOM", end=",")
        elif i == szam and i % 2 == 0:
            print("BAM", end="")
        else:
            print(i, end=",")
        i += 1
