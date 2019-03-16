import os
import re
import requests

default_event = '2019miket'
default_match_prefix = 'qm'
tba_api_url = 'https://www.thebluealliance.com/api/v3/'

# Hidden in vscode settings. Use this code for testing
# "terminal.integrated.env.windows": {
#     "TBA_API_TOKEN": "GO TO TBA AND GET YOUR OWN TOKEN"
# }
tba_token = os.environ["TBA_API_TOKEN"]
headers = {
    'X-TBA-Auth-Key': tba_token
}

def teamsInMatch(match_number):
    r = requests.get(url = f'{getMatchUrl(match_number)}', headers=headers) 
  
    data = r.json()
    blue = data['alliances']['blue']['team_keys']
    red = data['alliances']['red']['team_keys']

    blue[:] = [s.replace('frc', '') for s in blue]
    red[:] = [s.replace('frc', '') for s in red]
    return {
        "blue": blue,
        "red": red
    }

def getMatchUrl(match_number):
    return f'{tba_api_url}match/{default_event}_{getMatchKey(match_number)}'

def getMatchKey(match_number):
    return f'{default_match_prefix}{match_number}'

def teamInfo(team_number):
    r = requests.get(url = f'{tba_api_url}team/frc{team_number}', headers=headers)

    data = r.json()
    return data