def countList (numb):
    """
    funkc na spocitanie listu 
    """
    out=0
    
    for cislo in numb:
        out+=cislo

    return out 

def avg (list):
    """
    funkc na spocitanie priemeru 
    """
    return sum(list)/len(list)


numbList=[]

while True:

    cislo= input ("Zadaj cele platne cislo alebo Enter pre ukoncenie ")
    if cislo : 
        numbList+=[int(cislo)]
    else:
        break    

cnt=countList(numbList)
max = max(numbList)
min = min(numbList)
average= avg(numbList)
print("mnozina cisel je ", numbList)
print("Pocet cisel v mnozine je ", len(numbList))
print("Sucet cisiel v mnozine je ", cnt)
print("Najvacsie cislo v mnozine je ", max)
print("Najmensie cislo v mnozine je ", min)
print("Priemer cisel v mnozine je ", average)

