from fuggvenyek import primszam
import random

# 1. Írd ki, hogy melyik a legnagyobb szám a [100;100000] intervallumból, amelyiknek az utolsó
# számjegye nagyobb, mint az előtte lévő számjegyek összege.
def feladat1():
    def szamol(szam):
        _szam = szam
        utolso = _szam % 10
        _szam //= 10
        osszeg = 0
        while _szam > 0:
            osszeg += _szam % 10
            _szam //= 10

        return utolso > osszeg

    i = 100
    legn = 0
    while i < 100000:
        if szamol(i):
            legn = i
        i += 1
    return legn


print("Az 1. feladat eredménye:", feladat1())

# 2. Írd ki 100-tól kezdve a második 10 darab olyan számot, amelyiknek pontosan 7 osztója van
# (1-et és önmagát figyelmen kívül hagyva).
def feladat2():
    def osztokszama(szam):
        i = 2
        osztok = []
        while i < szam:
            if not szam % i:
                osztok.append(i)
            i += 1
        return len(osztok)

    hetosztosok = []
    i = 100
    while len(hetosztosok) < 2:
        if osztokszama(i) == 7:
            hetosztosok.append(i)
        i += 1
    return hetosztosok[1]


print("A 2. feladat eredménye:", feladat2())

# 3. Írd ki annak a sorozatnak a 15. elemét, amelyet úgy kapsz meg, hogy minden következő elemet
# az előző szám számjegyeinek kétszereséből állítod elő! (1, 2, 4, 8, 16, 212, 424, 848, 16816)
def feladat3():
    def kovetkezo(szam):
        kov = ""
        while szam > 0:
            maradek = szam % 10
            szam //= 10
            kov = str(maradek * 2) + kov
        return int(kov)

    szamok = []
    kov = 1
    szamok.append(kov)
    while len(szamok) < 15:
        kov = kovetkezo(kov)
        szamok.append(kov)

    return szamok[14]


print("A 3. feladat eredménye:", feladat3())
# 4. Sorsolj ki egy 6 számjegyű számot. Add meg, hogy melyik prímszám van ehhez a legközelebb!
# Ha több ilyen van, írd ki mindet!
def feladat4():
    szam = int(random.random() * (900000)) + 100000
    # szam = 149832 # egyenlő
    i = 0
    while not primszam(szam + i):
        i += 1
    ptavolsag = i
    pprim = szam + i

    i = 0
    while not primszam(szam - i):
        i += 1
    ntavolsag = i
    nprim = szam - i

    ret = f"A szám {szam} volt,"

    if ptavolsag > ntavolsag:
        ret += (
            f"a legközelebbi prímszám {nprim}. (A szomszédos prímek: {nprim}, {pprim})"
        )
    elif ptavolsag < ntavolsag:
        prim = pprim
        ret += (
            f"a legközelebbi prímszám {pprim}. (A szomszédos prímek: {nprim}, {pprim})"
        )
    else:
        ret += f"a szomszádos prímszámok egyenlő távolságra vannak: {szam - ntavolsag}, {szam + ptavolsag}"

    return ret


print("A 4. feladat eredménye:", feladat4())
# 5. Sorsolj ki egy 10 számjegyű számot. Írd ki a számon belüli prímszámokat!
# (pl: 1123456789 -> 2, 3, 5, 7, 11, 23, 67, 89, 1123, 4567, 23456789)
# A prímszámokat növekvő sorrendben add meg! Ugyanazt a számot ne írd ki kétszer!
# Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!
def feladat5():
    szam_str = str(int(random.random() * (9000000000)) + 1000000000)
    # szam_str = "1123456789"
    primek = []
    i = 0
    while i < len(szam_str):
        j = i
        while j < len(szam_str):
            j += 1
            vizsg_szam = int(szam_str[i:j])
            if vizsg_szam not in primek and primszam(vizsg_szam):
                primek.append(vizsg_szam)

        i += 1
    primek.sort()
    return ", ".join(map(str, primek))


print("A 5. feladat eredménye:", feladat5())
# 6. Sorsolj ki egy 10 számjegyű számot. Melyik az a legnagyobb legalább kétjegyű szám ezen belül,
# amelyiknek a számjegyei növekvő sorrendben állnak? (pl: 1234345673 -> 34567)
# Ha nincs ilyen, akkor írd ki, hogy nincs ilyen szám!
def feladat6():
    szam_str = str(int(random.random() * (9000000000)) + 1000000000)
    nov = szam_str[0]
    i = 1

    sorozatok = []
    # print(">>", szam_str)
    while i < len(szam_str):
        if szam_str[i] > nov[-1]:
            nov += szam_str[i]
            # print(">> add:  ", nov)
        else:
            if len(nov) >= 2:
                sorozatok.append(nov)
            #     print(">>store: ", nov)
            # else:
            #     print(">>disc: ", nov)
            nov = szam_str[i]
        i += 1

    if len(nov) >= 2:
        sorozatok.append(nov)
        # print(">>fstore: ", nov)

    if not len(sorozatok):
        ret = f"A szám {szam_str} volt, nincs benne növekvő sorozat."
    else:
        ret = f"\n- A szám {szam_str} volt,"

        max = 0
        i = 0
        while i < len(sorozatok):
            if sorozatok[max] < sorozatok[i]:
                max = i
            i += 1
        ret += (
            f"\n- A szövegként összehasonlítva a legnagyobb sorozat {sorozatok[max]}."
        )

        max = 0
        i = 0
        while i < len(sorozatok):
            if int(sorozatok[max]) < int(sorozatok[i]):
                max = i
            i += 1
        ret += f"\n- A számértékét tekintve a legnagyobb sorozat {sorozatok[max]}."

        max = 0
        i = 0
        while i < len(sorozatok):
            if len(sorozatok[max]) < len(sorozatok[i]):
                max = i
            i += 1
        ret += f"\n- A leghosszabb sorozat {sorozatok[max]}."
    return ret


print("A 6. feladat eredménye:", feladat6())
# 7. Sorsolj ki egy 10 számjegyű számot. Írd ki azokat a számjegyeket, amelyek nem fordulnak elő a számban!
# Ha nincs ilyen, írd ki, hogy nincs hiányzó számjegy!
def feladat7():
    szam = int(random.random() * (9000000000)) + 1000000000
    jegyek = [0] * 10
    _szam = szam
    while _szam > 0:
        maradek = _szam % 10
        _szam //= 10
        jegyek[maradek] += 1
    i = 0
    nem_szerepel = []
    while i < len(jegyek):
        if jegyek[i] == 0:
            nem_szerepel.append(i)
        i += 1
    if not nem_szerepel:
        ret = f"A szám {szam} volt, nincs hiányzó számjegy"
    else:
        ret = f"A szám {szam} volt, a következő számok nem szerepelnek benne: {', '.join(map(str, nem_szerepel))}"
    return ret


print("A 7. feladat eredménye:", feladat7())
# 8. Sorsolj ki egy 10 számjegyű számot. Írd ki azokat a 3 számjegyű számokat, amelyek az eredeti
# számjegyekből összerakhatóak úgy, hogy a számjegyeik növekvő sorrenden állnak.
# Ugyanazt a számot ne írd ki kétszer! Ha nincsenek ilyenek, akkor írd ki, hogy nincsenek ilyen számok!
def feladat8():
    szam_str = str(int(random.random() * (9000000000)) + 1000000000)
    i = 0
    csh = 3  # csoportok hossza
    csoportok = []
    while i < len(szam_str) - csh + 1:
        csoport = szam_str[i : (i + csh)]
        j = 1
        while j < len(csoport) and csoport[j - 1] < csoport[j]:
            j += 1
        if j == len(csoport):
            csoportok.append(csoport)
        i += 1
    if len(csoportok):
        ret = f"A szám: {szam_str}, csoportok: {', '.join(csoportok)}"
    else:
        ret = f"A szám: {szam_str}, nincsenek benne csoportok"
    return ret


print("A 8. feladat eredménye:", feladat8())
# 9. Sorsolj ki egy 5 számjegyű számot. Írd ki, hogy van-e olyan számjegye, amelyik nagyobb a többi
# számjegy összegénél! Ha van ilyen, írd ki melyik az! Ha nincs ilyen, írd ki, hogy nincs ilyen számjegy!
def feladat9():
    szam = int(random.random() * (90000)) + 10000
    _szam = szam
    josszeg = 0
    while _szam > 0:
        josszeg += _szam % 10
        _szam //= 10

    _szam = szam
    legn = 0
    while _szam > 0:
        jegy = _szam % 10
        _szam //= 10
        if jegy > josszeg - jegy:
            legn = jegy

    if legn:
        ret = f"A szám: {szam}, a legnagyobb jegy: {legn}"
    else:
        ret = f"A szám: {szam}, nincs ilyen számjegy"

    return ret


print("A 9. feladat eredménye:", feladat9())
