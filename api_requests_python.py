import requests
from requests.exceptions import HTTPError

try:
    response = requests.get("https://anapioficeandfire.com/api/characters/583")

    response.raise_for_status()
except HTTPError as http_err:
    print("Http error ocurred {}".format(http_err))
except Exception as err:
    print("Other error occurred {}".format(err))
else:
    print("Success!")
    print(response.text)

    #Response Headers returns a dictionary, can be accessed using ['header'].
    print(response.headers['Content-Type'])