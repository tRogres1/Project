number=int(input("Listelenecek = "))

for i in range(0,number,1):

    if i%2==0:
        print(f"Çift = {i}")

    if i%2 !=0:
        print(f"Tek = {i}")