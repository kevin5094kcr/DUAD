#1.Cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.

import csv

def enter_video_game():
    name = input("Enter the name of the video game: ")
    genre = input("Enter the genre of the video game: ")
    developer = input("Enter the developer of the video game: ")
    esrb = input("Enter the ESRB rating of the video game: ")
    return "t/".join([name, genre, developer, esrb]) # Concatena los valores con tabulaciones 

def save_to_csv(video_games_two):
    with open('video_games_two.csv', mode='w', newline='') as file:
        file.write("Name\tGenre\tDeveloper\tESRB Rating\n")  # Write the header with tabulation
        for game in video_games_two:
            file.write(game + "\n")  # Write each game data with tabulation
    print("Data has been saved to 'video_games.csv'")

def main():
    n = int(input("Enter the number of video games you want to enter: "))
    video_games = []
    for i in range(n):
        video_games.append(enter_video_game())
    save_to_csv(video_games)

if __name__ == "__main__":
    main()