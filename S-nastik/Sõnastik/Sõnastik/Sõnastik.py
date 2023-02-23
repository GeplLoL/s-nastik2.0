from omaModul import *
MasVene=loe_failist("vene.txt")
MasEst=loe_failist("est.txt")
while True:
    v=int(input("1-tõlk:vene-eesti\n2-tõlk:eesti-vene\n3-lisa_sõnu\n4-Muuta\n5-TEST"))
    if v==1:
        laused=tõlk(MasVene,MasEst)
        print(laused)
    elif v==2:
        laused=tõlk(MasEst,MasVene)
        print(laused)
    elif v==3:
        laused=lisa_sõnu(MasEst,MasVene)
        print(MasEst)
        print(MasVene)
    elif v==4:
        laused=muutaSõnu(MasEst,MasVene)
        print(MasEst)
        print(MasVene)
    elif v==5:
        laused=test(MasEst,MasVene)
        print(MasEst)
        print(MasVene)