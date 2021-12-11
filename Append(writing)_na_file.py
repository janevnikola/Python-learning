

serii_file=open("C:\\Users\\Administrator\\Desktop\\Series.txt", "a") # a znaci append t.e ne go prebrisuvame kako write tuku samo dodavame
print("Dali fajlot e citliv? \n")
print(serii_file.writable())
serii_file.write("\nTest writing") #\n za nov red zapisuvanje vo fajlot
serii_file.close() #sekoj fajl koj ke se otvori mora da se zatvori
