def carrée():
    x = input("tapez 1 si on doit trouver x² et 2 si on doit trouver x: ")
    a = input("le nombre le plus petit de l'intervalle: ")
    b = input("le nombre le plus grand de l'intervalle: ")
    x = float(x)
    a = float(a)
    b = float(b)
    if x==1:
        a = a**2
        b = b**2
        print("S=[", a,";", b,"]")
    if x==2:
        if a>=0 and b>=0:
            a = a**(0.5)
            b = b**(0.5)
            ma = 0-a
            mb = 0-b
            print("S=[" , mb,";", ma,"]U[", a, ";", b,"]")
        if a<0 and b>=0:
            b = b**(0.5)
            mb = 0-b
            print("S=[", mb,";", b,"]")
        if a<0 and b<0:
            print("l'ensemble est nul")
        if a==0 and b==0:
            print("l'ensemble est nul")
    else:
        print("choisisez un chiffre entre 1 et 2 svp")


