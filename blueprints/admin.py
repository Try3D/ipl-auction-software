from flask import Blueprint, render_template, request
from models import pool_name_map, data

admin = Blueprint("admin_blueprint", __name__)


@admin.route("/")
def index():
    import json

    combined = {
        "cat": pool_name_map,
        "data": data.to_dict(orient="records"),
    }
    return render_template("admin.html", data=json.dumps(combined))


@admin.route("/<int:player_id>", methods=["GET", "PUT"])
def get_player(player_id):
    if request.method == "GET":
        return data[data["id"] == player_id].to_dict(orient="records")[0]
    elif request.method == "PUT":
        return request.get_json()
