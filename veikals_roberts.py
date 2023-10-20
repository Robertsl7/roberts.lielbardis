'''veikals1 = 
veiaksl2 = 
veikals3 = 
veiaksl4 = 
veikals5 = '''
'''piens = 1('litrs')
maize = 1('500g')
krējums = 2 ('500g')
cukurs = 2('kg')
'''
veikals = input('Sveicināti! Lūdzu izvēlieties veikalu uz kuru vēlaties doties!:')
print('Preču klāsts:','\npiens','\nmaize', '\nkrējums','\ncukurs',)
daudzums = int(input('Cik preces Jūs vēlaties iegādāties? '))
if daudzums<=0 : 
    print('Nav iespējams iegādāties norādīto skaitu preču.')
    exit()
prece = input('Ko jūs pirksiet?:')
cena = input('Cik prece maksā?:')
maksasana = int(input('Vai ir nopirksts viss, kas sarakstā?(jā/nē)'))
if maksasana == 'jā':
    print('Uz drīzu tikšanos atkal:)')