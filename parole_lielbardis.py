parole = 'ziema'
username = 'roberts'
print('Jūsu lietotājvārds ir roberts un parole ir ziema')#tiek dota informācija, kas ir jāievada

username_parbaude = input('Ievadiet, lietotājvārdu: ')
if username == 'roberts':
    print
else : print('Mēģiniet velreiz')
    

paroles_parbaude = input('Ievadiet paroli: ')#tiek veikta paroles pārbaude
if parole == 'ziema': 
    print('Pieslēgšanās veiksmīga ')
else : print('Mēģiniet velreiz')



skaitlis1 = int(input("Ievaidiet 1. veselo skaitli: "))
skaitlis2 = int(input('Ievadiet 2. veselo skaitli: '))
if skaitlis1 >0:#skaitlis nevar būt negatīvs
    exit()
if skaitlis2 >0:#skaitlis nevar būt negatīvs
    exit()
while skaitlis2<skaitlis1 == '0':
    summa=skaitlis1+skaitlis2
    if skaitlis1 == 'stop':
        exit()
    if skaitlis2 == 'stop':
        exit()

if skaitlis1<skaitlis2:#skaitlis nevar būt mazāks par 0
    print('0')












