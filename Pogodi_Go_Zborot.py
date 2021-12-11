taen_zbor="Jagotki"
obidi=3
input_zbor=""

print("Igrata zapocnuva\nImate 3 obidi")
while input_zbor != taen_zbor:
    if obidi>0:
        input_zbor=input("Vnesi zbor: ")
    obidi-=1
    print("Imate uste: "+str(obidi)+" obidi")
    if obidi==0:
        break;

if input_zbor==taen_zbor:
    print("Go pogodivte zborot")
elif input_zbor!=taen_zbor:
    print("Ne go pogodivte zborot, obidete se pak")

print("\nIgrata zavrsi")
