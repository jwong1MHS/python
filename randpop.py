#!/usr/bin/python
print ("Content-type: text/html\n")

import random

def random_year():
    f = open('nyc_pop.csv')
    s = f.read().strip()
    f.close()
    lines = s.split('\n')[1:]
    return random.choice(lines)

def total_pop(line):
    data = line.split(',')[1:]
    total = 0
    for boro in data:
        total+= int(boro)
    return line + ',' + str(total)

#get the pertinent data
year = random_year()
new_line = total_pop(year)
headers = 'Year,Manhattan,Brooklyn,Queens,Bronx,Staten Island,Total'

#make the HTML
page_top = """
<!DOCTYPE html>
<html>
<head>
<title>Random NYC Population</title>
<style>                                                                                                                                                                 
table, th, td {                                                                                                                                                         
border: 1px solid black;                                                                                                                                                
}                                                                                                                                                                       
table {                                                                                                                                                                 
border-collapse: collapse;                                                                                                                                              
}                                                                                                                                                                       
</style>
</head>
"""

page_body = """
<body>
<h2>Random NYC Population Data</h2>
"""

table = '<table><tr>'
for header in headers.split(','):
    table+= '<th>'
    table+= header
    table+= '</th>'
table+= '</tr><tr>'

for data in new_line.split(','):
    table+= '<td>'
    table+= data
    table+= '</td>'

table+= '</tr></table>'



page_body+= table + '</body></html>'

print(page_top)
print(page_body)

