from degree_finder import find_path_in_links
from build_actor_links import build_actor_links

actor_links = build_actor_links()

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