#1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#a. Debe incluir:
# 1. Nombre
# 2. Género
# 3. Desarrollador
# 4. Clasificación ESRB

import csv

def enter_video_game():
    name = input("Enter the name of the video game: ")
    genre = input("Enter the genre of the video game: ")
    developer = input("Enter the developer of the video game: ")
    esrb = input("Enter the ESRB rating of the video game: ")
    return [name, genre, developer, esrb]

def save_to_csv(video_games):
    with open('video_games.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Genre', 'Developer', 'ESRB Rating'])
        writer.writerows(video_games)
    print("Data has been saved to 'video_games.csv'")

def main():
    n = int(input("Enter the number of video games you want to enter: "))
    video_games = []
    for i in range(n):
        video_games.append(enter_video_game())
    save_to_csv(video_games)

if __name__ == "__main__":
    main()