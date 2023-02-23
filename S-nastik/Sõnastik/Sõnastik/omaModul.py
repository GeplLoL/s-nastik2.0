from random import *
def loe_failist(f):
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
def tõlk(f:str,s:str):
    x=input("Sise sõnu: ")
    if x in f:
        asv=f.index(x)
        asd=s[asv]
    else:
        asd="Vale sõnu"
    return(asd)
def lisa_sõnu(f:str,s:str):
    x=input("Esti sõna: ")
    y=input("Vene sõna: ")
    asv=f.append(x)
    asd=s.append(y)
    return(asv,asd)
def muutaSõnu(f:list,s:list)->list:
    xy=input("millist sõnastikku soovite parandada? Est või Vene")
    if xy=="Est":
        x=int(input("Nimetage sõna asukoht: "))
        xyz=input("Sisse: ")
        f.pop(x)
        fa=f.insert(x,xyz)
        f=open("est.txt", "a")
        f.writelines(fa)
        f.close()
    elif xy=="Vene":
        y=int(input("Nimetage sõna asukoht: "))
        xyz=input("Sisse: ")
        sa=f.insert(y,xyz)
        s=open("vene.txt", "a")
        s.writelines(sa)
        s.сlose()
    return f,s
def test(f:str, s:str):
    x=input("millist sõnastikku soovite test? Est või Vene")
    vastusVale=0
    vastusÕige=0
    zxz=int(input("mitu katset soovite teha: "))
    for i in range(zxz):
        if x=="Est":
            randomSõnu=randint(0,4)
            print(f[randomSõnu])
            zx=f.index(f[randomSõnu])
            xy=input("Sisse: ")
            if xy==s[zx]:
                vastusÕige+=1
            else:
                vastusVale+=1
        elif x=="Vene":
            randomSõnu=randint(0,4)
            print(s[randomSõnu])
            zx=s.index(s[randomSõnu])
            xy=input("Sisse: ")
            if xy==f[zx]:
                vastusÕige+=1
            else:
                vastusVale+=1
    print("Õige",round(vastusÕige/zxz*100,1),"%")
    print("Vale",round(vastusVale/zxz*100,1),"%")
    f.write
    return f, s
