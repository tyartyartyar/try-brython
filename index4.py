from browser import document, window

def file_read(e):
  def onload(e):
    document['file-read'].value = e.target.result

  file = document['file-upload'].files[0]
  reader = window.FileReader.new()
  reader.readAsText(file)
  reader.bind('load', onload)

document['file-upload'].bind('input', file_read)

