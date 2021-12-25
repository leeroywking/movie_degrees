import json

with open("./movie.json") as f:
    movies = json.load(f)

movies_clean = {}

for movie in movies:
    movies_clean[movie["title"]] = movie["actors"]

while True:
    try:
        print("Ready for user input...(hit ctrl+c to exit)")
        title = ""
        while title not in movies_clean:
            title = input("Enter movie title: ")
            if title not in movies_clean:
                print(f"{title} not found please check your spelling and try again")
            print("----------------------------------")
            print(f"Actors in {title}:")
            print("-----")
            for movie in movies_clean[title]:
                print(movie)
        print("----------------------------------")
    except KeyboardInterrupt:
        print()
        print("Cleaning up memory...")
        exit()
        # print()
