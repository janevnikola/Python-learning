#Dictionary (recnik):
#imame PAR (kluc, vrednost)
#klucevite mora da bidat razlicni za sekoj par
#Primer: Jan e klucot, Januari e vrednosta


#Hash tabela vo Java
#definicija: 
Konverzija_meseci={
    "Jan":"Januari",
    "Fev":"Fevruari",
    "Mar":"Mart",
    255:"Dveste pedeset i pet" #moze da sodrzi i broevi
}

print(Konverzija_meseci.get("Jan")) # ke ispecati Januari
print(Konverzija_meseci.get("NO element")) #ke ispecati none
print(Konverzija_meseci.pop("No element","Elementot ne postoi")) # sega nema da ispecati none,
                                                                # tuku Elementot ne postoi
print(Konverzija_meseci) # ke gi ispecati site klucevi
print(Konverzija_meseci.get(255))

Konverzija_meseci.pop("Fev")
print("Pravime pop na fev\n")
print(Konverzija_meseci.get("Fev")) # ke ispecati none
Konverzija_meseci.clear() # go brisime recnikot
print(Konverzija_meseci)


