import random # na linkot: https://docs.python.org/3/py-modindex.html 
#moze da gi vidime site moduli koi moze da se koristat
#NO MOZE I DA INSTALIRAME NOVI MODULI SO pip install modul_name
from random import randint #od random modulot .te klasata importirame funkcija randint
def printanje(value):
    print(randint(1,value))


printanje(100)
