import requests
import pandas as pd

def fetch_baseball(date, debug=False):
    # date as YYYY-MM-DD
    endpoint = f'games?date={date}'
    url = f"https://v1.baseball.api-sports.io/{endpoint}"
    headers = {
    'x-apisports-key': 'b3a48765c914f155e0beba11ff4063b0',
    }
    response = requests.request("GET", url, headers=headers)
    games = response.json()['response']
    print(f"MLB Games being fetched for {date}...")
    temp = []

    for _, elem in enumerate(games):
        if elem['league']['name'] == 'MLB':
            temp_dict = {}
            game_id = elem['id']
            temp_dict['game_id'] = game_id
            # NOTE: change format to EST
            temp_dict['date'] = elem['date'].split("T")[0]
            temp_dict['time'] = elem['time']
            temp_dict['timezone'] = elem['timezone']
        ############
            home_team = elem['teams']['home']['name']
            temp_dict['home_team'] = home_team
            away_team = elem['teams']['away']['name']
            temp_dict['away_team'] = away_team
        ############
            home_score = elem['scores']['home']['total']
            temp_dict['home_score'] = home_score
            away_score = elem['scores']['away']['total']
            temp_dict['away_score'] = away_score
            temp_data = pd.DataFrame(temp_dict, index=[game_id])
            data = pd.concat([data, temp_data])

            if(debug):
                print(f"{temp_dict}")
                print(f" {home_team} with {home_score} ----- vs ----- {away_team} with {away_score} \n")
            temp.append(temp_dict)
    print("MLB Games fetched.")
    return temp
        
def fetch_football(date, debug=False):
    # date as YYYY-MM-DD
    endpoint = f'games?date={date}'
    url = f"https://v1.american-football.api-sports.io/{endpoint}"
    headers = {
    'x-apisports-key': 'b3a48765c914f155e0beba11ff4063b0',
    }

    response = requests.request("GET", url, headers=headers)
    games = response.json()['response']
    print(f"NFL Games being fetched for {date}...")
    data = pd.DataFrame()
    temp = []
    for _, elem in enumerate(games):
        if elem['league']['name'] == 'NFL':
            temp_dict = {}
            game_id = elem['game']['id']
            temp_dict['game_id'] = game_id
    #         # NOTE: change format to EST
            temp_dict['date'] = elem['game']['date']['date']
            temp_dict['time'] = elem['game']['date']['time']
            temp_dict['timezone'] = elem['game']['date']['timezone']
    #     ############
            home_team = elem['teams']['home']['name']
            temp_dict['home_team'] = home_team
            away_team = elem['teams']['away']['name']
            temp_dict['away_team'] = away_team
    #     ############
            home_score = elem['scores']['home']['total']
            temp_dict['home_score'] = home_score
            away_score = elem['scores']['away']['total']
            temp_dict['away_score'] = away_score
            temp_data = pd.DataFrame(temp_dict, index=[game_id])
            data = pd.concat([data, temp_data])

            if(debug):
                print(f"{temp_dict}")
                print(f" {home_team} with {home_score} ----- vs ----- {away_team} with {away_score} \n")
            temp.append(temp_dict)

    print("NFL Games fetched.")
    return temp



if __name__='__main__':
    # get data as list of dicts
    baseball_data = fetch_baseball("2023-08-07")

    # get data as list of dicts
    football_data = fetch_football("2022-10-09")

