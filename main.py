import statsapi
from pprint import pprint

royalsTeamId = 118
merrifieldPlayerId = '593160'
homeOrAway = ''

"""# getStatus
Reference object: https://statsapi.mlb.com/api/v1/gameStatus
Given a unique game id, return whether the game is live or finished
Preview is considered live
Ignoring edge cases of postponed vs delayed

Parameters:

-g (--gameId): unique id for the game
-h (--help): display this help
"""
def getStatus(gameId):
    #boxData = statsapi.boxscore_data(mostRecentGameId)
    params = {}
    params.update(
        {
            "gamePk": gameId,
        })
    
    gumbo = statsapi.get("game", params)
    gameData = gumbo.get('gameData')
    status = gameData.get('status')

    return status['abstractGameState']

"""# getMerrifieldHitsByGameId
Given a unique game id, returns the number of hits by Merrifield

Parameters:

-g (--gameId): unique id for the game
-h (--help): display this help
"""
def getMerrifieldHitsByGameId(gameId):
    boxData = statsapi.boxscore_data(gameId)

    sides = ["away", "home"]
    batters = []
    for i in range(0, len(sides)):
        side = sides[i]
        for batterId_int in [
            x
            for x in boxData[side]["batters"]
            if boxData[side]["players"].get("ID" + str(x), {}).get("battingOrder")
        ]:

            batterId = str(batterId_int)

            batter = {
                "h": str(
                    boxData[side]["players"]["ID" + batterId]["stats"]["batting"][
                        "hits"
                    ]
                ),
                'batterId': batterId
            }

            batters.append(batter)
    
    return batters['batterId' == merrifieldPlayerId]['h']


mostRecentGameId = statsapi.last_game(royalsTeamId)

print(getMerrifieldHitsByGameId(mostRecentGameId))

#print(dates)

#print (boxData['status'])
# Determine if Royals are away or home
# Must be a better way to get this data
# if (boxData['away']['team']['id'] == royalsTeamId):
#     homeOrAway = 'away'
# else:
#     homeOrAway = 'home'

# merriFieldHits = boxData[homeOrAway]["players"]["ID" + merrifieldPlayerId]["stats"]["batting"]["hits"]

# print (statsapi.boxscore(mostRecentGameId))