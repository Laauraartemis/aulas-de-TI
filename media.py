nota1 = float(input("adicione a nota: "))
nota2 =  float(input("adicione a nota: "))
nota3 =  float(input("adicione a nota: "))
nota4 =  float(input("adicione a nota: "))

media = (nota1+nota2+nota3+nota4)/4

print("sua nota é", media)

if media <=3:
    print("reprovado")
elif media <=5:
    print("recuperação")
else:
    print("aprovado")



