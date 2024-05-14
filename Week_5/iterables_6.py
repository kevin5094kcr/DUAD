# Ejemplo de iterables con la instrucción Break para romper un ciclo

colors = [
	'black',
	'yellow',
	'red',
	'blue',
	'green',
]

for color in colors:
	print(color)
	if color == 'blue':
		break
	
