menu = """
------MENU-----
[D]depositar
[S]sacar
[E]exibir extrato
[s]sair
--->"""

saldo=1000.00
limite=500
extrato=""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  
    N =  input (menu)

    if N == "D":

        depósito = float(input("informe o valor do seu depósito:"))

        if depósito > 0:
            saldo += depósito
            extrato += f" depósito : R${depósito}\n "
            print("depósito realizado com successo!")
            print(f"Seu saldo atual é de R${saldo}")

        else:
            print("falha ao realizar depósito! tente novamente mais tarde")
        

    elif N =="S":
        
        S=float(input("informe o valor que queira sacar:"))

        if saldo < S :
            print ("Não podemos realizar o saque porque o valor é maior que o seu saldo!!!!")
            
        elif S > limite:
            print("Não é possível realizar o saque !!!! Porque o seu limite de saque é de R$500.00")  
        
        elif numero_saques >= LIMITE_SAQUES :
            print("voçê atingiu o limite de saque díário!!!")  


        elif S > 0 :
            print(f"seu saldo é {saldo}")
            saldo -= S
            extrato+=f"Saque:R$ {S:.2f}"
            numero_saques+=1
            print (f"seu saldo atual é de {saldo}") 
        else:
            print ("Não é possível realizar o saque porque o valor dosaque é inválido!!!!")

    elif N=="E":
        print("\n----------EXTRATO----------")
        print("Não ouve movimentações na sua conta." if not extrato else extrato)
        print(f"\nSaldo : R${saldo:.2f}")
        print("-----------Esse é o seu extrato----------")

    elif N=="s":
        break


    else:
        print("não reconhecemos a ação ! Por favor , tente outra operação")