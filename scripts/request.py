import requests
import pandas as pd

df = pd.read_excel("PlayerListPreprocessed.xlsx")

url = "http://localhost:8000/addplayer"

for index, row in df.iterrows():
    player_data = {
        "setNo": row["SET NO:"],
        "name": row["NAME"],
        "country": row["COUNTRY"],
        "prevTeam": row["PREV TEAM"] if not pd.isna(row["PREV TEAM"]) else "",
        "basePrice": row["BASE PRICE"],
        "age": row["AGE"],
        "numMatches": (
            int(row["NO.OF MATCHES PLAYED"])
            if not pd.isna(row["NO.OF MATCHES PLAYED"])
            else None
        ),
        "numRuns": int(row["NO.OF RUNS"]) if not pd.isna(row["NO.OF RUNS"]) else None,
        "battingAvg": row["BATTING AVG."] if not pd.isna(row["BATTING AVG."]) else None,
        "strikeRate": row["STRIKE RATE"] if not pd.isna(row["STRIKE RATE"]) else None,
        "numWickets": (
            int(row["NO.OF WICKETS"]) if not pd.isna(row["NO.OF WICKETS"]) else None
        ),
        "bowlingAvg": row["BOWLING AVG."] if not pd.isna(row["BOWLING AVG."]) else None,
        "bowlingEconomy": (
            row["BOWLING ECONOMY"] if not pd.isna(row["BOWLING ECONOMY"]) else None
        ),
    }

    image_file_path = f"player_photos/{str(row['S. NO']).zfill(3)}.png"

    files = {"img": (image_file_path, open(image_file_path, "rb"))}
    response = requests.post(url, data=player_data, files=files)

    if response.status_code == 200:
        print(f"Player {row['S. NO']} - {row['NAME']} added successfully.")
    else:
        print(
            f"\033[93mError for Player {row['S. NO']} - {row['NAME']}: {response.status_code} - {response}\033[0m"
        )
