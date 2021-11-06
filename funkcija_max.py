def max_vrednost(new_broj1, new_broj2):
    if new_broj1 > new_broj2:
        return new_broj1
    elif new_broj2>new_broj1:
        return new_broj2

broj1=input("Vnesi go prviot broj: ")
broj2=input("Vnesi go vtoriot broj: ")

print("Pogolem broj e: "+str(max_vrednost(broj1,broj2)))
