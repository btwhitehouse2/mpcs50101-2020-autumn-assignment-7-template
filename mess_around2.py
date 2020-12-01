import requests
import json
import pandas
import re
from colorama import Fore, Back, Style 

# The headers remain the same for all the requests
headers = {'Authorization': '5178921f092446eca048d486e234e05c'} 
 
# All the endpoints in this section
 
# To fetch the top headlines
top_headlines_url = 'https://newsapi.org/v2/top-headlines'
# To fetch news articles
everything_news_url = 'https://newsapi.org/v2/everything'
# To retrieve the sources
sources_url = 'https://newsapi.org/v2/sources'
q = 'corona'
search_api = {'q':'corona', 'language': 'en', 'country': 'us'}

response = requests.get(url=top_headlines_url, headers=headers , params=search_api)
pretty_json_output = json.dumps(response.json(), indent=0)
print(pretty_json_output)