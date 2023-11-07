'''izveidot 3 sarakstus: lietotājs pats norādīs, cik elementus likt sarakstā.
Pirmā un otrā saraksta vērtības ievada lietotājs.
Trešā saraksta vērtības iegūst apvienojot pirmos 2 sarakstus
Katra saraksta saturu glīti paradīt uz ekrāna'''

saraksts1 = []
saraksts2 = []
saraksts3 = []

print('-----------------Saraksts-----------------')
cipars1 = int(input('Cik elementu Jūs vēlaties likt sarakstsos? '))
for i in range(cipars1):   #pirmais saraksts
    melns = int(input('Ko Jūs vēlaties ievietot 1.sarakstā?'))
    saraksts1.append(melns)
print('Pirmā saraksta elementi:',saraksts1)


for j in range(cipars1):
    melns2 = int(input('Ko Jūs vēlaties ievietot 2.sarakstā?'))
    saraksts2.append(melns2)
print('Otrā saraksta elementi:',saraksts2)

saraksts3 = saraksts1+saraksts2
print(saraksts3)




    
