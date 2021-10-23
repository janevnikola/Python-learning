#rabota so listi
listaIminja=["Nikola", "Elena", "Ana"]
listaBroevi=[1,2,3,4,5,6,7]
listaIminja.append(listaBroevi) #ke ispecati iminjata pa posle broevite
print(listaIminja)

listaNewIminja=["Nikola", "Elena", "Ana"]
listaNewIminja.append("Mia") #ke go dodadi elementot na krajot
print(listaNewIminja)

listaNewIminja.insert(0,"Lea")#dodavanje na element na bilo koja pozicija
print(listaNewIminja)

listaNewIminja.remove("Ana")#brisenje na element od listata
print(listaNewIminja)

listaNewIminja.pop() #go vadi posledniot element (kako stack)
print(listaNewIminja)

listaNewIminja.clear() #ke ja izbrise celata lista
print(listaNewIminja)

listaBroevi.sort() # ke ja sortira listata broevi vo rastecki redosled
print(listaBroevi)

listaBroevi.reverse() #ke ja prevrti listata naopaku
print(listaBroevi)
