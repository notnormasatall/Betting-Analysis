from typing import Collection
import pandas as pd
from constants import TEAMS_NAMES, COL_NAMES

<<<<<<< HEAD

def get_team_data(df, team_name):
    df_team1 = df[df["team1"] == team_name]
    stats = [x + "1" for x in COL_NAMES]
    df_team1 = df_team1[["team1"] + stats]
    df_team1 = df_team1.set_axis([["team"] + COL_NAMES], axis=1)
=======
def get_team_data(df, team_name, data = COL_NAMES):
    df_team1 = df[df["team1"] == team_name]
    stats = [x + "1" for x in data]
    df_team1 = df_team1[stats]
    df_team1 = df_team1.set_axis([data], axis = 1)
>>>>>>> 9ab69d5d719d1c00040c11c64e422a8880be14a7

    df_team2 = df[df["team2"] == team_name]
<<<<<<< HEAD
    stats = [x + "2" for x in COL_NAMES]
    df_team2 = df_team2[["team2"] + stats]
    df_team2 = df_team2.set_axis([["team"] + COL_NAMES], axis=1)
=======
    stats = [x + "2" for x in data]
    df_team2 = df_team2[stats]
    df_team2 = df_team2.set_axis([data], axis = 1)
>>>>>>> 9ab69d5d719d1c00040c11c64e422a8880be14a7

    # print(df_team1, df_team2)
    df_team = pd.concat([df_team1, df_team2])
    return df_team

<<<<<<< HEAD

def get_data(df):
    for team_name in TEAMS_NAMES:
        df_team = get_team_data(df, team_name)
        create_team_csv(df_team, team_name)


def create_team_csv(df_team, filename):
    df_team.to_csv(f"data/teams/{filename}_stats.csv")
=======
def get_data(df, season_name = "", teams = TEAMS_NAMES, data = COL_NAMES):
    for team_name in teams:
        df_team = get_team_data(df, team_name, data)
        create_team_csv(df_team, team_name, season_name)

def create_team_csv(df_team, filename, season_name):
    df_team.to_csv(f"data/teams/{season_name}/{filename}_score_posession.csv", index = False)
>>>>>>> 9ab69d5d719d1c00040c11c64e422a8880be14a7


def read_csv(filename):
    df = pd.read_csv(filename, index_col=False)
    return df

<<<<<<< HEAD

if __name__ == "__main__":
    get_data(read_csv("data/matchesSEASON_20_21.csv"))
=======
# def create_team_csv(df_team, filename):
#     df_team.to_csv(f"data/teams/{filename}_stats.csv")

if __name__ == "__main__":
    dat = COL_NAMES
    get_data(read_csv("data/matchesSEASON_20_21.csv"), "SEASON_20_21", data=dat)
    get_data(read_csv("data/matchesSEASON_19_20.csv"), "SEASON_19_20", data=dat)
    get_data(read_csv("data/matchesSEASON_18_19.csv"), "SEASON_18_19", data=dat)
    get_data(read_csv("data/matchesSEASON_17_18.csv"), "SEASON_17_18", data=dat)
    get_data(read_csv("data/matchesSEASON_16_17.csv"), "SEASON_16_17", data=dat)
>>>>>>> 9ab69d5d719d1c00040c11c64e422a8880be14a7
