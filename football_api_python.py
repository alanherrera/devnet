import requests
from requests.exceptions import HTTPError

try:
    response = requests.get("https://v3.football.api-sports.io/standijngs",
    headers = {'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "bb2e5c996cc071a43b0a4b16c84aea56"},
    params = {'season':'2020', 'league':'39'})

    response.raise_for_status()
except HTTPError as http_err:
    print("Http error ocurred {}".format(http_err))
except Exception as err:
    print("Other error occurred {}".format(err))
else:
    print("Success!")
    standings = response.json()
    #print(standings['response'][0]['league']['standings'][0][0]['team']['name'])
    index = 0
    print("---- PREMIER LEAGUE STANDINGS ----\n")
    for items in standings['response'][0]['league']['standings'][0]:
        print("{} {} --> {} points".format(standings['response'][0]['league']['standings'][0][index]['rank'],standings['response'][0]['league']['standings'][0][index]['team']['name'], standings['response'][0]['league']['standings'][0][index]['points']))
        index+=1
    #for key in standings['response'][]:
        #print(key)
            
    #Response Headers returns a dictionary, can be accessed using ['header'].
    print(response.headers['Content-Type'])