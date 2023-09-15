print('Divciparu skaitļa ciparu summas aprēķins')
cipars = int(input("ievadiet divciparu skaitli!"))
print("divciparu skaitlis =", cipars)
#iegūst divciparu skaitļa 1. ciparu
first_nummber=cipars//10
print("pirmais cipars:", first_nummber)
#iegūst divciparu skaitļa 2. ciparu
second_number=cipars%10
print("otrais cipars:", second_number)
#iegūst ciparu summu
print(first_nummber+second_number)
