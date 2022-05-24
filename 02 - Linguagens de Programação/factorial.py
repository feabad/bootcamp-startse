num = int(input('Digite n:'))
rep = 1
fact = num
while rep < num:
    fact = fact * (num - rep)
    rep = rep + 1
print ('O fatorial de ', num, 'é: ', fact)
