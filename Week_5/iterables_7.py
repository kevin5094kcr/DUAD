# Tambien funciona para romper ciclos infinitos
	
colors = [
	'black',
	'yellow',
	'red',
	'blue',
]

for color in colors:
	if color == 'yellow':
		continue

	print(color)