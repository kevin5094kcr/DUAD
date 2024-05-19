# Ejemplo de iterable con ciclo For
# Ejemplo de iteración directa incluyendo índice


my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index, record in enumerate(my_favorite_records): 
	print(f'Record {index}: {record}')
	
# Se usa enumerate en lugar de range con diferencias en el código