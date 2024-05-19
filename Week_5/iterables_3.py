# Ejemplo de iterable con ciclo While
# Ejemplo de iteración por índice

my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

index = 0
while (index < len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')
	index += 1
	
# Con el ciclo While se hace como si fuera un contador, 
# Se hace cuando no se sabe cuantos elementos hay en la lista 