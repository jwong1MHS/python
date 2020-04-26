def strip_commas( s ):
    quote_end = -1
    while s.find('"', quote_end+1) != -1:
        quote_start = s.find('"', quote_end+1)
        quote_end = s.find('"', quote_start + 1)
        comma = s.find(',', quote_start, quote_end)
        while comma != -1:
            s = s[:comma] + ' ' + s[comma + 1:]
            comma = s.find(',', comma + 1, quote_end)
    return s


def make_list(s):
    lines = s.split('\n')
    data = []
    for line in lines:
        row = line.split(',')
        i = 0
        while i < len(row):
            cell = row[i]
            if cell.isdigit():
                row[i] = int(cell)
            i+= 1
        data.append(row)
    return data

#f = open('2012_SAT_Results.csv')
#text = f.read().strip()
#f.close()

text = """DBN,SCHOOL NAME,Num of SAT Test Takers,SAT Critical Reading Avg. Score,SAT Math Avg. Score,SAT Writing Avg. Score
01M292,HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES,29,355,404,363
01M539,"NEW EXPLORATIONS INTO SCIENCE, TECHNOLOGY AND MATH HIGH SCHOOL",159,522,574,525
02M392,MANHATTAN BUSINESS ACADEMY,s,s,s,s"""

text = strip_commas(text)
print( text )

data = make_list(text)
for row in data:
    print(row)