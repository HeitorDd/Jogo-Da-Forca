import os 

sub = []
sub2 =[]
pal_sub = []
pal_sub2 = []
cont = 0
cont3 = 0
cont4 = 0
estagio = 0
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç"]

while(cont4 == 0):
    print(" ")
    palavra = input("Digite a palavra desejada(Caso tenha espaço a palavra não será aceita):\n ")
    palavra = palavra.lower()
    if(" " in palavra or "1" in palavra or "2" in palavra or "3" in palavra or "4" in palavra or "5" in palavra
       or "6" in palavra or "7" in palavra or "8" in palavra or "9" in palavra or "0" in palavra or palavra == ""):
        #""
        print("Palavra inválida!!")
    else:
        cont4 = cont4 + 1
        
for i in range(len(palavra)):
    sub.append("_")
    sub2.append("_")
    pal_sub.append(palavra[cont])
    pal_sub2.append(palavra[cont])
    cont = cont + 1

while(cont3 == 0):
    limpar = input("Digite 'a' para limpar o terminal: ")
    if(limpar == "a"):
        os.system('cls')
        cont3 = 1
    
var1 = " ".join(map(str,sub))
var2 = " ".join(map(str,pal_sub))

def forca(estagio):
    if estagio == 0:
        print("\n  __ \n"
            " /    | \n"
            "|     o \n"
            "| \n"
            "| \n")
    elif estagio == 1:
        print("\n  __ \n"
            " /    | \n"
            "|     o \n"
            "|     | \n"
            "| \n")
    elif estagio == 2:
        print("\n  __ \n"
            " /    | \n"
            "|     o \n"
            "|    /| \n"
            "| \n")
    elif estagio == 3:
        print("\n  __ \n"
            " /    | \n"
            "|     o \n"
            "|    /|\ \n"
            "| \n")
    elif estagio == 4:
        print("\n  __ \n"
            " /    | \n"
            "|     o \n"
            "|    /|\ \n"
            "|    / \n")
    elif estagio == 5:
        print("\n  __ \n"
            " /    | \n"
            "|     o \n"
            "|    /|\ \n"
            "|    / \ \n")
    if estagio == -1:
        print("\n  __ \n"
            " /    | \n"
            "| \n"
            "| \n"
            "| \n")
  
while(estagio < 7):
    cont1 = 0
    print(" ")
    var5 = " ".join(map(str,sub))
    tent = input(f"Digite uma letra para tentar adivinhar a palavra:\n\n{var5}        ")
    if(len(tent) > 1 or tent not in alfabeto):
        print(" ")
        print("valor invalido!!")
    else:
        if(tent in pal_sub):
            ind2 = alfabeto.index(tent)
            alfabeto.pop(ind2)
            for i in range(len(palavra)):
                var3 = "".join(map(str,palavra))
                if(tent == var3[cont1]):
                    ind = pal_sub.index(tent)
                    sub[ind] = tent
                    pal_sub[cont1:cont1 + 1] = "*"
                    cont1 = cont1 + 1
                    var4 = " ".join(map(str,sub))
                    forca(estagio - 1)
                    print(var4)
                    print(" ")
                else:
                    cont1 = cont1 + 1
        else:
            forca(estagio)
            estagio += 1
            print("Voce gastou ",estagio ,"de 6 tentativas!!")
            
    if(sub == pal_sub2):
        print("Voce ganhou!!")    
        break
    if(estagio == 6):
        print("Voce perdeu!!")
        print(f"a palavra era: {var2} ")
        print(" ")
        break