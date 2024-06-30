#nested dictionary
def player(dict):
    for player_name in dict:
        print("Player Name:",player_name)
        print("payer detail:",dict[player_name])
dict={"Virat":{"ODI":7548,"Test":7485},"Rohit":{"ODI":8548,"Test":5485},"Sachin":{"ODI":19048,"Test":17485}}
player(dict)

print("\n-------------------------------------------------------------------------------\n")
def player(dict):
    for player_name in dict:
        print("Player Name:",player_name)
        print("payer detail:",dict[player_name]["ODI"])
dict={"Virat":{"ODI":7548,"Test":7485},"Rohit":{"ODI":8548,"Test":5485},"Sachin":{"ODI":19048,"Test":17485}}
player(dict)

print("\n----------------------------------------------------------------------------\n")
def player(dict):
    for name,detail in dict:
        print("Player Name:",name)
        print("payer detail:",detail)
dict=[(1,"Amit"),(2,"Gopal")]
player(dict)