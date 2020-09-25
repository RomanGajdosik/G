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

    try:
        cislo= input ("Zadaj cele platne cislo alebo Enter pre ukoncenie ")
        if cislo: 
            numbList+=[int(cislo)]
        else:
            break    
   
if numbList:
    cnt=countList(numbList)
    max = max(numbList)
    min = min(numbList)
    average= avg(numbList)
    print(numbList,"mnozina cisel  ",len(numbList), " = Pocet cisel v mnozine ",cnt," = Sucet cisiel v mnozine ",max," = Najvacsie cislo v mnozine ",min,"= Najmensie cislo v mnozine ",average,"= Priemer cisel v mnozine ")
    #print("Pocet cisel v mnozine je ", len(numbList))
    
else: print("ZIADNE CISLO ZADANE ****** KONIEC ")    