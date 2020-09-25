import random
count  = 0 

zamena=["moj","tvoj","jeho","jej","nas",'vas']
podstM=["muz",'Zena','pes',"macka",'Kon',"dom",'vlak']
pridM=['tazky',"lahky","opacny",'Kratky',"Dlhy"]
slovesa=['skace',"prdi","grga","otravuje"]

while count < 5 :
    flag=random.randint(0,1)
    line = random.choice(zamena) + " "
    line += random.choice(podstM) + " "
    if flag:
        line += random.choice(pridM) + " "
    line += random.choice(slovesa) + " "
    print(line)
    count += 1       