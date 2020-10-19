import requests

response = requests.get("https://anapioficeandfire.com/api/characters/550")

if response.status_code is not 200:
    raise ApiError("Error al intentar traer la API")

else:
    print(response.json())
    #for key, value in response.json().items():
    #    if type(value) == list:
    #        for items in value:
    #            content_of_list = ''
    #            content_of_list = content_of_list + items
    #        print("The {} is {}".format(key, content_of_list))
    #    else:
    #        print("The {} is {}".format(key, value))