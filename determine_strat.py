import pandas as pd


def set_strat():
    """
    """
    data = pd.read_csv(
        f"./data/means.csv", index_col=False)

    data['rating'] = 1/4*(data['final_third_entries'] +
                          data['attempts_obox'] +
                          data['attempts_ibox'] +
                          data['total_offside']) - 1/3*(data['total_tackle'] +
                                                        data['blocked_pass'] +
                                                        data['interception'])
    average = sum(list(data['rating'].values)) / len(data['rating'])
    strats = [0 if i + 1 < average else 1 for i in data['rating'].values]

    data['strategy'] = strats

    result = data[['team', 'rating', 'strategy']]
    return result


def filter_matches(param):
    """
    """
    data = pd.read_csv(
        f"./data/matches.csv")
    strat_data = set_strat()

    data = pd.merge(data, strat_data, left_on='team1', right_on='team')
    data.rename(columns={"strategy": "strategy1",
                "rating": "rating1"}, inplace=True)
    del data["team"]

    data = pd.merge(data, strat_data, left_on='team2', right_on='team')
    data.rename(columns={"strategy": "strategy2",
                "rating": "rating2"}, inplace=True)
    del data["team"]

    data = filter_data(data, param)
    if param:
        data.to_csv('data/agressive.csv', index=False)
    else:
        data.to_csv('data/defensive.csv', index=False)

    return data


def filter_data(data, param):
    """
    """
    data = data[(data['strategy1'] == param) & (data['strategy2'] == param)]
    data = data[['team1', 'team2', 'score1', 'score2',
                 'first_half_goals1', 'first_half_goals2',
                 'rating1', 'rating2', 'strategy1', 'strategy2']].reset_index()
    del data['index']

    return data


if __name__ == '__main__':
    filter_matches(1)
    filter_matches(0)
