#!/usr/bin/python
print ("Content-type: text/html\n")

import random

f = open('template.html')
html = f.read()
f.close()

def set_title(html, title):
    opentag = html.find('<title>')
    closetag = html.find('</title>')
    opentag+= len('<title>')
    return html[:opentag] + title + html[closetag:]

def fill_tag(html, tag, content):
    opentag = html.find('<'+tag+'>')
    closetag = html.find('</'+tag+'>')
    opentag+= len('<'+tag+'>')
    return html[:opentag] + content + html[closetag:]

f = open('filler.txt')
filler = f.read().strip().split('\n')
f.close()


page = fill_tag(html, 'title', 'Silliness')
body = ''
i = 0
while i < 5:
    body+= random.choice(filler)
    body+= '<hr>'
    i+= 1
page = fill_tag(page, 'body', body)
print(page)
