import pandas as pd


def set_team_position():
    """
    """
    position = {'Arsenal': 8,
                'Aston Villa': 11,
                'Fulham': 18,
                'Leeds United': 9,
                'Leicester City': 5,
                'Liverpool': 3,
                'Manchester City': 1,
                'Sheffield United': 20,
                'West Ham United': 6,
                'Wolverhampton Wanderers': 13,
                'Burnley': 17,
                'West Bromwich Albion': 19,
                'Crystal Palace': 14,
                'Everton': 10,
                'Newcastle United': 12,
                'Tottenham Hotspur': 7,
                'Chelsea': 4,
                'Brighton and Hove Albion': 16,
                'Manchester United': 2,
                'Southampton': 15}

    data = pd.read_csv(
        f"data/means.csv")

    data['finale position'] = [position[i] for i in position]
    data.to_csv('data/means.csv', index=False)
    data.to_csv('data/regr_means.csv', index=False)


def scale_by_parmeter(param):
    """
    """
    data = pd.read_csv(f"data/scaled_means.csv")

    values = list(data[param])
    teams = list(data['team'])

    position = [None]*len(teams)

    v_t = [(values[i], teams[i]) for i in range(len(teams))]
    v_t.sort()

    for j, team in enumerate(teams):
        for i, v in enumerate(v_t):
            if team == v[1]:
                position[j] = i + 1

    data[f'scale_by_{param}'] = position
    data.to_csv('data/scaled_means.csv', index=False)


if __name__ == '__main__':

    set_team_position()
    parameters = ['touches',  'total_pass', 'pen_area_entries',
                  'final_third_entries', 'attempts_obox', 'attempts_ibox', 'blocked_pass', 'interception']
    for p in parameters:
        scale_by_parmeter(p)
