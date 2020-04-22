from browser import document, ajax, console
import json

url = 'https://api.chucknorris.io/jokes/random'

def on_complete(res):
  # console.log(json.loads(res.responseText))
  jokes = json.loads(res.responseText)
  document['joke'].text = jokes['value']

def get_joke(e):
  req = ajax.ajax()
  req.open('GET', url, True)
  req.bind('complete', on_complete)
  document['joke'].text = 'Loading..'
  req.send()

document['get_joke'].bind('click', get_joke)

