nolīgšana= 1,20
dienā = 0,47
naktī= 0,87
gaidīšana = 0,15
izsaukums = 2,40

pasažieri = int(input('Cik pasažieri brauks ar taksi? (1 līdz 4 / vairāk kā 4): '))
if pasažieri >4 : #pasažieru skaits tiek ierobežots līdz 4
    print('Jūms ir pārsniegts pasažieru skaits ')
    exit()
elif pasažieri <= 4: #pasažieru skaits tiek ierobežots no 1 līdz 4
    pulkstenis = int(input ('Cikos plānojat veikt izsaukumu? (veselās stundās) '))
    if pulkstenis >5 or pulkstenis<23:
       print('Par taksi šajā laika periodā būs jāmaksā 0,47 par km ')#tiek veikta norādītā perioda maksa
    elif pulkstenis <6 or pulkstenis>23:
        print('Par taksi šajā laika periodā būs jāmaksā 0,87 par km ')#tiek veikta norādītā perioda maksa
    vieta = (input('Vai Jūs atrodaties pie mūsu firmas stāvvietas? (jā/nē) '))
    if vieta == 'nē':
        print('Tad Jums nāksies maksāt gan par nolīgšanas cenu, kas ir 1,20, gan par izsaukuma izsaukumu, kas ir 2,40 ')
    elif vieta =='jā':
        print('Tad Jums nāksies maksāt tikai par nolīgšanas cenu 1,20 ')
    gaidīšana= (input ('Vai Jums ir vēlme veikt apstāšanos veikalā? (jā/nē)  '))#tiek veikta apstāšanās jautājuma uzdošana
    gaidīšana2= int(input('Cik ilgi?(ievadiet minūšu skaitu)'))
    if gaidīšana == 'jā':
            print('Par katru gaidīšanas mīnūti jāpiemaksā 0,15 ')
    elif gaidīšana =='nē':
            print('Tad nav jāmaksā par gaidīšanu ')
            attālums = int(input('Cik km jābrauc līdz galapunktam (km skaits 1-20) '))
            if attālums <=20:
                print('Tiks veikts norādītais km daudzums')
            elif attālums >20:
                 print('Ir pārsniegts km daudzums')

                
            

   