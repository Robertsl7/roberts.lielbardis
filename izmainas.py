saraksts = [2,5,9,4,6,3,2,8]
saraksts.append('Cepumns')#pievieno saraksts beigās
print(saraksts)

saraksts.pop()#izmet no beigām
print(saraksts)

saraksts.insert(3, 'Hello!')#ievieto 3. no kreisās, tas ir atkarīgs no skaitļa
print(saraksts)

saraksts.remove(5)#izdzēš norādīto vērtību
print(saraksts)

#funkcijas del pielietojums
tests = [1,2,3,4,5,6,7,8,]
del saraksts[2]
print(saraksts)

del tests[3:6]
print(tests) #izdzēš intervālu

cipari = [1,2,3,4,5,6,7,8]
del cipari[2:7:2]# no 2-7 elementa dzēš ārā katru otro
print(cipari)
