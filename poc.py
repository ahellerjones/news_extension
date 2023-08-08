import requests

def fetch_baseball(date, debug=False):
    # date as YYYY-MM-DD
    endpoint = f'games?date={date}'
    url = f"https://v1.baseball.api-sports.io/{endpoint}"
    headers = {
    'x-apisports-key': 'b3a48765c914f155e0beba11ff4063b0',
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


if __name__=='__main__':
    data = fetch_baseball("2023-08-07", True)
    print(data)