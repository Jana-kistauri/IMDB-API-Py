import requests
import json

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt0816692"

headers = {
    'x-rapidapi-key': "1f77456fcamsh4ff879ab310009bp13f2e9jsna2ba84228f3c",
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

print("Title:", data['title'])
print("Year:", data['year'])
print("Length:", data['length'])
print("IMDB:", data['rating'])
print("Votes:", data['rating_votes'])