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
def median (zoznam):
    """
    vypoicita strednu hodnotu zo zadaneho listu celych cisiel 
    """
    zoznam.sort()
    num=0
    zCount = len(zoznam)
    
    if (zCount%2):
    
         num=zoznam[zCount//2]

    else:
         
         num=99999    
    return num


numbList=[]

while True:
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
    median=median(numbList)
    print(numbList,"mnozina cisel  ",len(numbList), "Pocet cisel v mnozine ",cnt,"Sucet cisiel v mnozine ",max,"Najvacsie cislo v mnozine ",min,"Najmensie cislo v mnozine ",average,"Priemer cisel v mnozine ",sep='\n')
    print("Median  ", median )
    
else: print("ZIADNE CISLO ZADANE ****** KONIEC ")    