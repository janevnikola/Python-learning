ime="Nikola"
godini=45
daliEvisok= True

if ime=="Nikola" and str(godini)==str(45): #and e && t.e i, a or e || t.e ili
    print("Ti se vikas: "+ime+" i imas "+str(godini))
elif ime=="Tosko" and str(godini)==str(67):
    print("Ti ne se vikas "+ime+" i nemas "+str(godini))
elif not(daliEvisok): #!=
    print("Vnesi drugo ime")
