# Ejemplo de iterable 2 con ciclo For
# Ejemplo de iteración por índice,
# Se hace cuando sabemos cuantos elementos hay en la lista
my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
	'Perplexity',
	'50 cents Disco Inferno',
	'Slim Shady We Made You',
]

for index in range(0, len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')
	