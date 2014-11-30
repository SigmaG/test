carte=[]

def bordure_h(col):
	return [1]*col

def ligne(col):
	return [1] + [0]*(col-2) + [1]
	
def carre (col, lig):
	return [bordure_h(col)] + [ligne(col)]*(lig-2) + [bordure_h(col)]
	
def imprime_forme (tab):
	for y in range (len (tab)):
		for x in range (len( tab[0])):
			if tab[y][x] == 1:
				if y==0 or y==len(tab)-1:
					if x==0 or x == len(tab[0])-1:
						print("+",end =="")
					else :
						print("-",end=="")
				else :
					if x==0 or x== len(tab[0])-1:
						print("|" , end == "")
					else : 
						print("X", end == "" )
				print("#", end = "")
			else :
				print(" ", end = "")
		print("")