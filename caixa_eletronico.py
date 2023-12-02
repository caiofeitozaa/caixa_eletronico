from time import sleep

saldo = 0

while True:

	print("Escolha uma das opções:")
	
	sleep(0.5)

	print("[ 1 ] Efetuar saque")
	
	sleep(0.5)

	print("[ 2 ] Efeturar depósito")
	
	sleep(0.5)

	print("[ 3 ] Efetuar uma transferência")
	
	sleep(0.5)

	print("[ 4 ] Verificar saldo")
	
	sleep(0.5)

	print("[ 5 ] Sair")
	
	sleep(0.5)

	print("~" * 30)
	
	sleep(0.5)

	usuario = str(input("Digite aqui: "))

	print("~" * 30)
	
	sleep(0.5)
	
	""" Opção 1 """
	
	if usuario == "1":
	
		valor = float(input("Quanto deseja sacar ?\nDigite aqui: "))
		
		print("PROCESSANDO...")
		
		sleep(3)
		
		print("~" * 30)
	
		if valor > saldo:
		
			print("Você não tem esse valor em sua conta.")
			
			print("~" * 30)
		
		else:
		
			saldo -= valor
		
			print(f"Seu novo saldo é de R$:{saldo:.2f}")
			
			print("~" * 30)
			
	""" Opção 2 """
	
	if usuario == "2":
		
		valor = float(input("Quanto deseja depositar ?\nDigite aqui: "))
		
		print("~" * 30)
		
		saldo += valor
		
		sleep(0.5)
		
		print(f"Seu novo saldo é de R${saldo:.2f}")
		
		print("~" * 30)
		
	""" Opção 3 """
		
	if usuario == "3":
		
		print("Escolha uma das opções")
		
		sleep(0.5)
		
		print("[ 1 ] Pessoa física")
		
		sleep(0.5)
		
		print("[ 2 ] Pessoa Jurídica")
		
		sleep(0.5)
		
		pessoa = str(input("Digite aqui: "))
		
		sleep(0.5)
		
		print("~" * 30)
		
		if pessoa == "1":
			
			cpf = str(input("Indique o CPF (OBS.: Não use pontos): "))
			
			cpf_contador = len(cpf)
			
			print("PROCESSANDO...")
			
			sleep(3)
			
			print("~" * 30)
			
			if cpf_contador == 11:
				
				print("CPF válido.")
				
				print("~" * 30)
			
			else:
				
				while True:				
					cpf = str(input("Digite um CPF válido: "))
				
					cpf_contador = len(cpf)
					
					print("PROCESSANDO...")
					
					sleep(3)
					
					print("~" * 30)
					
					if cpf_contador == 11:
					
						print("CPF válido.")
						
						print("~" * 30)
						
						break
						
		if pessoa == "2":
			
			cnpj = str(input("Indique o CNPJ (OBS.: Não use pontos): "))
			
			cnpj_contador = len(cnpj)
			
			print("PROCESSANDO...")
			
			sleep(3)
			
			print("~" * 30)
			
			if cnpj_contador == 14:
				
				print("CNPJ válido.")
				
				print("~" * 30)
			
			else:
				
				while True:				
					cnpj = str(input("Digite um CNPJ válido: "))
					cnpj_contador = len(cnpj)
					
					print("PROCESSANDO...")
					
					print("~" * 30)
					
					sleep(3)
				
					if cnpj_contador == 14:
					
						print("CNPJ válido.")
						
						print("~" * 30)
						
						break
			
		valor = int(input("Digite o valor a ser transferido: "))
		
		sleep(0.5)
		
		print("~" * 30)
			
		if valor > saldo:
				
			print("Você não tem esse valor em sua conta.")
			
			print("~" * 30)
			
		else:
			
			saldo -= valor 
			
			print(f"Seu novo saldo é de R$:{saldo:.2f}")
			
			print("~" * 30)
						
	""" Opção 4 """
		
	if usuario == "4":
		
		sleep(0.5)
		
		print(f"Seu saldo atual é de R$:{saldo:.2f}")
		
		print("~" * 30)
	
	if usuario == "5":
		
		print("Encerrando...")
		
		sleep(2)
		
		break

print("Programa finalizado.")