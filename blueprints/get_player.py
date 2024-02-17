from flask import Blueprint, render_template, jsonify
from models import data, pool_name_map, pool_code_map

get_player = Blueprint("get_player", __name__)


@get_player.route("/<int:playerId>", methods=["GET"])
def get_player_by_serial(playerId):
    player_data = data[data["id"] == playerId]

    if not player_data.empty:
        # Check if player pool is different from previous player
        if playerId == 1:
            newPool = True
            currPlayerSet = 1
        else:
            currPlayerSet = int(data[data["id"] == playerId].iloc[:, 1])
            prevPlayerSet = int(data[data["id"] == (playerId - 1)].iloc[:, 1])
            if currPlayerSet != prevPlayerSet:
                newPool = True
            else:
                newPool = False

        # Convert the filtered DataFrame to a dictionary for JSON response
        player_dict = player_data.to_dict(orient="records")[0]

        output = {
            "player": player_dict,
            "player_img": f"/static/player_photos/{str(playerId).zfill(3)}.png",
            "pool": {
                "poolName": pool_name_map[currPlayerSet],
                "poolCode": pool_code_map[currPlayerSet],
                "isNewPool": newPool,
            },
        }

        print(output)

        return render_template("index.html", data=output)
    else:
        return jsonify({"error": "Player not found"}), 404
