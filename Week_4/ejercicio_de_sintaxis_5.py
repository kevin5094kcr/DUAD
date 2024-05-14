n = int(input("Ingrese la cantidad de notas del estudiante: "))

notas = []

for i in range(n):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

aprobadas = 0
desaprobadas = 0

for nota in notas:
    if nota >= 70:
        aprobadas += 1
    else:
        desaprobadas += 1

promedio_total = sum(notas) / n

notas_aprobadas = [nota for nota in notas if nota >= 70]
notas_desaprobadas = [nota for nota in notas if nota < 70]

if notas_aprobadas:
    promedio_aprobadas = sum(notas_aprobadas) / len(notas_aprobadas)
else:
    promedio_aprobadas = 0

if notas_desaprobadas:
    promedio_desaprobadas = sum(notas_desaprobadas) / len(notas_desaprobadas)
else:
    promedio_desaprobadas = 0

print(f"Total de notas aprobadas: {aprobadas}")
print(f"Total de notas desaprobadas: {desaprobadas}")
print(f"Promedio de todas las notas: {promedio_total}")
print(f"Promedio de las notas aprobadas: {promedio_aprobadas}")
print(f"Promedio de las notas desaprobadas: {promedio_desaprobadas}")