s = input ('Zadaj cele cislo ')
try:
       
    
    i=int(s)
    print ('Zadane platne cele cislo ', i )

except ValueError as err:
    print(err)

