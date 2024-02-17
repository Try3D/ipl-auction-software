import pandas as pd
import numpy as np

data = pd.read_excel("data/PlayersList2024_preprocessed.xlsx")
data = data.replace({np.nan: None})

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
    14: "ALL ROUNDERS 4",
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
    14: "AR4",
}

data.columns = [
    "id",
    "setNo",
    "name",
    "country",
    "basePrice",
    "age",
    "numMatches",
    "numRuns",
    "battingAvg",
    "strikeRate",
    "numWickets",
    "bowlingAvg",
    "bowlingEconomy",
]
