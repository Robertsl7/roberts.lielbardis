pirmais = int(input('Ievadiet pirmo locekli!'))
dif = int(input('Ievadiet diferenci!'))
sk = int(input("Ievadiet elementu skaitu!"))
formula = pirmais + dif*sk
x=1 

for i in range(pirmais, sk, x):
    print( i, " loceklis ", formula)
    x=x+1



