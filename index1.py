from browser import document

def show_text(e):
  document['output'].textContent = e.target.value

document['text'].bind('input', show_text)