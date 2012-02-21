import sqlite3 as lite
import string
import re

con = lite.connect('comedians.db')
cur = con.cursor()

whand = open('comedians.gdf', 'wb')

header = "nodedef> name, style, color" + "\n"
whand.write(header)

i = 1
cur.execute('SELECT name FROM Nodes')

for row in cur:
    name = re.sub('\W', '', row[0])
    if i == 1: 
        color = "white"
    if i == 2: 
        color = "blue"
    if i == 3: 
        color = "red"
    if i == 4: 
        color = "black"
    if i == 5: 
        color = "yellow"
    line = name + "," + "1" + "," + color + "\n"
    whand.write(line.encode('utf-8'))
    i = i + 1
    if i > 5: 
        i = 1

header = "edgedef> node1, node2, directed" + "\n"
whand.write(header)

cur.execute('SELECT source, target FROM Edges')

for row in cur:
    source = re.sub('\W', '', row[0])
    target = re.sub('\W', '', row[1])
    line = source + "," + target + ",true\n"
    whand.write(line.encode('utf-8'))