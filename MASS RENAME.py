import os
import random

def renomear():
	# pedindo pasta de caminho
	path = input("Digite o caminho da pasta: ")
	path = path.replace("\\", "/") + '/'
	i = random.randint(0,15)
	ii=0
	
	#path="C:/Users/Juninho/Desktop/MKT MOMENTS/WEBSITE MOMENTS/00 TRABALHOS/13-MD-FIJ/"
	
	for filename in os.listdir(path):
		while(i == ii):
			i = random.randint(0,15)

		ii = i
		my_dest = str(i) + " - " + filename
		my_source =path + filename
		my_dest =path + my_dest
		
		# função rename() vai renomear todos os arquivos
		os.rename(my_source, my_dest)
		
		#print(i)
		#print("-")

		#i += 1	
		#if(i > 5): 
		#	i = 0
			
	print("Arquivos Renomeados com sucesso!")
		

renomear()