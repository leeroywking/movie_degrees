import json
def build_actor_links():
    print("Loading the movie.json file...")
    with open("./movie.json") as f:
        movie_list = json.load(f)


    movies = {}
    actors = {}
    print("Parsing the movie.json file into an interim data structure...")
    for movie in movie_list:
        if movie["title"] not in movies:
            movies[movie["title"]] = []
        movie_actors = movie["actors"]
        movies[movie["title"]] = movie_actors
        for actor in movie_actors:
            if actor not in actors:
                actors[actor] = []
            if movie["title"] not in actors[actor]:
                actors[actor].append(movie["title"])

    # print(actors["Sean Connery"])
    # print(movies["Thor"])


    actor_links = {}

    print("Generating the Actor links...")
    for actor in actors:
        acted_in = actors[actor]
        # print(actor, "acted in", acted_in)
        if actor not in actor_links:
            actor_links[actor] = {}
        for movie in acted_in:
            linked_actors = movies[movie]
            for link in linked_actors:
                if link != actor:
                    if link not in actor_links[actor]:
                        actor_links[actor][link] = []
                    actor_links[actor][link].append(movie)
    return actor_links


if __name__ == "__main__":
    # print(json.dumps(actor_links))
    actor_links = build_actor_links()
    print("saving the actor_links.json file (~300mb)...")
    with open('actor_links.json', 'w') as outfile:
        json.dump(actor_links, outfile)
    print("Done!")