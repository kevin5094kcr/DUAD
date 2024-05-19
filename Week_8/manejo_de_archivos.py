# 1.Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def sort_songs(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8" ) as file: # Lee nombres de canciones de input_file
        songs = file.readlines()

    sorted_songs = sorted(songs) # Ordena las canciones alfabéticamente


    with open(output_file, 'w') as file: # Escribe los nombres de las canciones ordenadas en el output_file
        for song in sorted_songs:
            file.write(song)

input_file = "songs.txt"
output_file = "sorted_songs.txt"
sort_songs(input_file, output_file)
