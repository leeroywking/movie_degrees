import json

with open("./actor_links.json") as f:
    raw = json.load(f)

print(json.dumps(raw, sort_keys=True, indent=4))