from flask import Flask

app = Flask(__name__)
from degree_finder import find_path_in_links
from build_actor_links import build_actor_links
actor_links = build_actor_links()


@app.route("/<actor1>/<actor2>")
def hello_world(actor1, actor2):
    return find_path_in_links(actor_links,actor1,actor2)
