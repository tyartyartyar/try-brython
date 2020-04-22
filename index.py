from browser import document, console, alert

def show(e):
  console.log('Hello')
  alert('Hello World')
  document['hello'] <= 'Hello Worlds'

document['alert-btn'].bind('click', show)