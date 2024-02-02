import pandas as pd
from flask import Flask, jsonify, request, render_template, redirect
import numpy as np

#%%

pool_name_map = {
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

pool_code_map = {
    1: "MS",
    2: "BA1",
    3: "AR1",
    4: "WK1",
    5: "FB1",
    6: "SB1",
    7: "BA2",
    8: "WK2",
    9: "AR2",
    10: "FB2",
    11: "SB2",
    12: "AR3",
    13: "BA3",
    14: "AR4"
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

@app.route('/getPlayer/<int:playerId>', methods=['GET'])
def get_player_by_serial(playerId):
    player_data = data[data['id'] == playerId]
    
    if not player_data.empty:
        # Check if player pool is different from previous player
        if playerId == 1:
            newPool = True
            currPlayerSet = 1
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
            'pool': {
                    'poolName': pool_name_map[currPlayerSet],
                    'poolCode': pool_code_map[currPlayerSet],
                    'isNewPool': newPool
                }
            }
        
        print(output)
        
        return render_template('index.html', data=output)
    else:
        return jsonify({"error": "Player not found"}), 404
    
@app.route("/")
def home():
    return redirect("/getPlayer/1")

if __name__ == '__main__':
    app.run(debug=True)
