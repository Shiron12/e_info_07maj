#!/usr/bin/python

kodtabla = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

def kodolas(szoveg):
    kodolt_szoveg = ""
    for betu in szoveg:
        if not(ord(betu) >= 97 and ord(betu) <= 122):
            print("Hiba: Nem megfelelo karakter (elfogadott karakterek [a-z]).")
            return ""
        kodolt_szoveg += str(kodtabla[ord(betu) - 97])
    return kodolt_szoveg

def main():

    #1. feladat
    print("1. feladat:")
    bekeres = str(input("Kerek egy betut: "))
    if len(bekeres) > 1:
        print("Csak egy betut kertem!\n")
    else:
        print("A betunek a szamkodja: " + kodolas(bekeres) + "\n")

    #2. feladat
    print("2. feladat:")
    bekeres = str(input("Kerek egy szot: "))
    print("A szonak a szamkodja: " + kodolas(bekeres) + "\n")

    #3,4,5 feladat
    print("3. feladat:\nA szoveg.txt file beolvasasa.\n")
    szavak_file = open("szavak.txt", "r")
    eltarolt_sorok = szavak_file.readlines()
    szavak_file.close()

    print("4. feladat:")
    legnagyobb_meret = 0
    legnagyobb_szoveg = ""
    rovid_szavak = 0
    index = 0
    for sor in eltarolt_sorok:
        eltarolt_sorok[index] = sor.replace("\n", "")
        if len(sor) > legnagyobb_meret:
            legnagyobb_meret = len(sor)
            legnagyobb_szoveg = sor
        if len(sor) <= 5:
            rovid_szavak += 1
        index += 1
    print("A leghosszabb szo: " + legnagyobb_szoveg + "Hossza: " + str(legnagyobb_meret - 1) + " karakter\n")

    print("5. feladat:\nRovid szavak szama: " + str(rovid_szavak) + "\n")

    #6. feladat
    kodok = open("kodok.txt", "w")
    for sor in eltarolt_sorok:
        kodok.write(kodolas(sor)+"\n")
    kodok.close()
    print("6. feladat:\nSikeresen letrejott a kodok.txt\n")

    #7. feladat
    print("7. feladat:")
    bekeres = str(input("Kerek egy szamsort: "))
    volt_e_talalat = False
    for sor in eltarolt_sorok:
        if bekeres == kodolas(sor):
            if not volt_e_talalat:
                print("Egyezo szavak: ", end="")
            print(sor + " ", end="")
            volt_e_talalat = True

    if not volt_e_talalat:
        print("Nem volt egyezes.")
    else:
        print()

    #8.feladat
    print("\n8. feladat:")
    talalatok = dict()
    seged_lista = []
    max_elofordulas = 0
    max_elofordulas_kulcs = ""
    for sor in eltarolt_sorok:
        for sor2 in eltarolt_sorok:
            if kodolas(sor) == kodolas(sor2):
                seged_lista.append(sor2)
        if len(seged_lista) > 1 and not (kodolas(sor) in talalatok):
            if max_elofordulas < len(seged_lista):
                max_elofordulas = len(seged_lista)
                max_elofordulas_kulcs = kodolas(sor)
            talalatok[kodolas(sor)] = list()
            for lista_elem in seged_lista:
                talalatok[kodolas(sor)].append(lista_elem)
        seged_lista.clear()
    for kodolt_szam in talalatok.keys():
        for lista_elem in talalatok[kodolt_szam]:
            print(kodolt_szam + " : " + lista_elem + "; ", end="")

    print("\n\n9. feladat:")
    print("Legtobb kod: " + max_elofordulas_kulcs)
    print("hozza: ", end="")
    for lista_elem in talalatok[max_elofordulas_kulcs]:
        print(lista_elem + "; ", end="")
    print()


if __name__ == "__main__":
    main()
