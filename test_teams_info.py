import tba_service

teams = [857,
        1596,
        2586,
        3602,
        4391,
        4715,
        4970,
        4988,
        5486,
        5702,
        5706,
        5989,
        6088,
        6113,
        6345,
        6558,
        6569,
        7638,
        7713,
        7782,
        7816]

for team in teams:
    data = tba_service.teamInfo(team)
    nickname = data['nickname']
    city = data['city']
    state = data['state_prov']
    print(f'{team},{nickname},{city}, {state}')