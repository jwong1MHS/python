#!/usr/bin/python
print ("Content-type: text/html\n")

import random
import cgi

#useful functions
def fill_tag(html, tag, content):
    opentag = html.find('<'+tag+'>')
    closetag = html.find('</'+tag+'>')
    opentag+= len('<'+tag+'>')
    return html[:opentag] + content + html[closetag:]

def get_headers(s):
    g = s.split('\n')
    return g[0].split(',')

def row_total(row):
    total = 0
    for d in row:
        total+= int(d)
    return total

def get_data(s):
    lines = s.split('\n')
    lines.pop(0)
    data = {}
    for line in lines:
        line = line.split(',')
        data[line[0]] = line[1:]
        data[line[0]].append( str(row_total(line[1:])))
    return data


#collect the data from the csv file
pop_file = open('nyc_pop.csv')
text = pop_file.read().strip()
pop_file.close()
pop_headers = get_headers(text) + ['Total']
pop_data = get_data(text)

#set up the HTML from template
template_file = open('template.html')
html = template_file.read()
template_file.close()
page = fill_tag(html, 'title', 'Boro Population')

#get the query string data
form = cgi.FieldStorage()
if 'year' in form:
    YEAR = form.getvalue('year')

    if YEAR in pop_data:
        #Create the webpage
        page_body = '<body><h2>NYC Population Data for ' + YEAR + '</h2>'

        if 'name' in form:
            page_body+= 'Hello ' + form.getvalue('name') + ' here is the data you requested:<br><br>'

        table = '<table><tr>'
        for header in pop_headers:
            table+= '<th>'
            table+= header
            table+= '</th>'
        table+= '</tr><tr>'
        row_data = pop_data[YEAR]
        table+= '<td>' + YEAR + '</td>'
        for data in row_data:
            table+= '<td>'
            table+= data
            table+= '</td>'
        table+= '</tr></table>'
        page_body+= table + '</body></html>'
    else:
        page_body = '<h2>No Census Data for ' + YEAR + '</h2>'
else:
    page_body = '<h2>Please provide a year in the query string</h2>'

page = fill_tag(page, 'body', page_body)

print(page)
