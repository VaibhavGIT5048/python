player_stats = {
    "player_name" : "virat khole",
    "player_age":32,
    "teams" :[ "India" , "RCB"] ,
    "format" : ["TEST" , "ODI" , "T20"],
    "Matches_played":{"TEST":585 , "ODI":585 , "T20":524},
    "Total_Runs":{"TEST":1025 , "ODI":2145 , "T20":2547},
    "Batting_average":{"TEST":54 , "ODI":54 , "T20":57},
    
    
    
}

for key,value in player_stats.items():
    print(f" {key} , {value}")
