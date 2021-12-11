#try catch blokot vo python e:
#try: i except:
#except e sto i kako catch, no namesto da fakjame promenlivi kako java i c++, imame
#except pa error-ot koj go fakjame
#except: (e default catch, koj sto fakja se)
#primer: except Value error e error koj dokolku vneseme ne tocna promenliva t.e rezultat ke frli error
#kako vo primerot
try:
    test = 5 / 10
    broj = int(input("Vnesi broj: "))
    print(broj)
except ZeroDivisionError:
    print("test")
except ValueError:
    print("Brojot ne e cel")
except: #fati se sto ne e specificirano
    print("Default catch")
