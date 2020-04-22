from browser import document
from browser.template import Template

namasaya = 'Tyar'
Template(document['greet']).render(name=namasaya)