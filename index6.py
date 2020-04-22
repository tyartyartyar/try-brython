from browser import document, html, window, console

storage = window.localStorage

def add_item(e):
  key = document['key-input'].value
  value = document['value-input'].value
  storage.setItem(key, value)

def remove_item(e):
  key = document['key-input'].value
  storage.removeItem(key)

document['add-btn'].bind('click', add_item)
document['remove-btn'].bind('click', remove_item)