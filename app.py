from flask import Flask, redirect

from blueprints.admin import admin
from blueprints.get_player import get_player

# Data ingestion
"""

--- FYI ---

id: Player Unique ID
setNo: Player Pool (e.g. BATSMEN 1, ALL ROUNDERS 2, & more)

"""

app = Flask(__name__)

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(get_player, url_prefix="/player")


@app.route("/")
def home():
    return redirect("/player/1")


if __name__ == "__main__":
    app.run(debug=True)
