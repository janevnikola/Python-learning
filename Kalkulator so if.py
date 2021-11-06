broj1=int(input("Vnesi go prviot broj: "))
operator=input("Vnesi +, -, /, %, *: ")
broj2=int(input("Vnesi go vtoriot broj: "))

if operator=="+":
    rezultat=broj1+broj2
    print("Sobiranje, a rezultatot e: "+str(rezultat))
elif operator=="-":
    rezultat=broj1-broj2
    print("Odzemanje, a rezultatot e: "+str(rezultat))
elif operator=="*":
    rezultat=broj1*broj2
    print("Mnozenje, a rezultatot e: "+str(rezultat))
elif operator=="/":
    rezultat=float(broj1)/broj2
    print("Delenje, a rezultatot e: "+str(rezultat))
elif operator=="%":
    rezultat=float(broj1)%broj2
    print("Ostatok, a rezultatot e: "+str(rezultat))
