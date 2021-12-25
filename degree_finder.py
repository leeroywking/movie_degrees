import json


def find_path_in_links(actor_links, actor1 = "Helena Bonham Carter", actor2 = "Chris Hemsworth"):
    if actor1 not in actor_links:
        return(f"Error: {actor1} not in our database")
    if actor2 not in actor_links:
        return(f"Error: {actor2} not in our database")
    print("Actors found in DB")
    print("looking for path...")
    queue = [[actor1,""]]
    checked_actors = []
    loop_count = 0
    while len(queue) > 0:
        loop_count +=1
        if loop_count % 1000 == 0:
            print("still looking...")
        current = queue.pop(0)
        current_actor = current[0]
        current_str = current[1]
        checked_actors.append(current_actor)
        if actor2 in actor_links[current_actor]:
            return(f"{current_str} and {current_actor} was in {actor_links[current_actor][actor2][0]} with {actor2}")
        else:
            for actor in actor_links[current_actor]:
                if actor not in checked_actors:
                    queue.append([actor,f"{current_str} {current_actor} was in {actor_links[current_actor][actor][0]} with {actor};"])
    return("Oops no match sorry")


if __name__ == "__main__":
    try:
        with open("./actor_links.json") as f:
            print("Loading Database...")
            actor_links = json.load(f)
            print("Database Loaded!")
    except:
        print("Error actor_links.json does not exist. Did you follow the setup instructions in the read me?")
        exit()




    while True:
        try:
            print("Ready for user input...(hit ctrl+c to exit)")
            actor1 = ""
            actor2 = ""
            while actor1 not in actor_links:
                actor1 = input("Enter first actors name: ")
                if actor1 not in actor_links:
                    print(f"{actor1} not found please check your spelling and try again")
            while actor2 not in actor_links:
                actor2 = input("Enter second actors name: ")
                if actor2 not in actor_links:
                    print(f"{actor2} not found please check your spelling and try again")
            print(find_path_in_links(actor_links, actor1, actor2))
            print("----------------------------------")
        except KeyboardInterrupt:
            print()
            print("Cleaning up memory...")
            exit()
            # print()
