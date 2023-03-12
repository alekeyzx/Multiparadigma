import random as equizde
import csv



#while True:
   # numrad = int(input("cual sera el numero entre 1 y 20",))
    
    #n = equizde.randint(0,20)
    #if(numrad == n):
     #   print("error, el numero es", n)
      #  break
    
with open('test.csv') as file:
    reader= csv.reader(file)
    for row in reader:
        print(','.join(row))
        
    
