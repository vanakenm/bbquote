import requests

def get_quote():
  url = "http://breaking-bad-quotes.herokuapp.com/v1/quotes"
  response = requests.get(url).json()[0]

  return f'{response["quote"]} - {response["author"]}'