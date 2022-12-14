lista = []
sw = True
cad = 'aver'
sum = 0
max_sum = -1
while sw:
    cad = input()
    
    if cad == "":
        print(lista, sum)
        if sum > max_sum and sum!=64929 and sum!=64690:
            max_sum = sum
        sum = 0
        lista = []
        print('Suma max: ', max_sum)
    else:
        lista.append(cad)
        sum = sum + int(cad)
    
    

#64929
#64690
#64078