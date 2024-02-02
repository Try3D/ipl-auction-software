import pandas as pd
from flask import Flask, jsonify, request
import numpy as np

#%%

pool_title_map = {
    1: "MARQUEE SET",
    2: "BATSMEN 1",
    3: "ALL ROUNDERS 1",
    4: "WICKET KEEPERS 1",
    5: "FAST BOWLERS 1",
    6: "SPIN BOWLERS 1",
    7: "BATSMEN 2",
    8: "WICKET KEEPERS 2",
    9: "ALL ROUNDERS 2",
    10: "FAST BOWLERS 2",
    11: "SPIN BOWLERS 2",
    12: "ALL ROUNDERS 3",
    13: "BATSMEN 3",
    14: "ALL ROUNDERS 4"
}

#%%

# Data ingestion
data = pd.read_excel("data/PlayersList2024_preprocessed.xlsx")
data = data.replace({np.nan: None})

data.columns= ['id', 'setNo', 'name', 'country', 'basePrice', 'age', 'numMatches', 'numRuns', 'battingAvg', 'strikeRate', 'numWickets', 'bowlingAvg', 'bowlingEconomy']

'''

--- FYI ---

id: Player Unique ID
setNo: Player Pool (e.g. BATSMEN 1, ALL ROUNDERS 2, & more)

'''

#%%

app = Flask(__name__)

@app.route('/api/getPlayer/<int:playerId>', methods=['GET'])
def get_player_by_serial(playerId):
    player_data = data[data['id'] == playerId]
    
    if not player_data.empty:
        # Check if player pool is different from previous player
        if playerId == 1:
            newPool = True
        else:
            currPlayerSet = int(data[data['id'] == playerId].iloc[:, 1])
            prevPlayerSet = int(data[data['id'] == (playerId - 1)].iloc[:, 1])
            if currPlayerSet != prevPlayerSet:
                newPool = True
            else:
                newPool = False
            
        # Convert the filtered DataFrame to a dictionary for JSON response
        player_dict = player_data.to_dict(orient='records')[0]
        
        output = {
            'player': player_dict,
            'newPool': newPool}
        
        return jsonify(output)
    else:
        return jsonify({"error": "Player not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

    

    








