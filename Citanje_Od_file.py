

serii_file=open("C:\\Users\\Administrator\\Desktop\\Series.txt", "r") #r za citanje (read)
print("Dali fajlot e citliv? \n")
print(serii_file.readable())

#print("\nIscitaj go celiot fajl\n")
#print(serii_file.read())

#print("Citaj ja prvata linija: ")
#print(serii_file.readlines()[0])

#print("Poinakov nacin na citanje na linija: "+serii_file.readline())

#citanje na linija po linija so for ciklus
for i in serii_file.readlines():
    print(i)

serii_file.close() #sekoj fajl koj ke se otvori mora da se zatvori
