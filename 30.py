for a in range(2, 11):        
    contador = 0                
    for i in range(1, a + 1): 
        if a % i == 0:
            contador += 1      
    if contador == 2:        
        print(a)