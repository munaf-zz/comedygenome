from xml.dom.minidom import Document
import sqlite3 as lite

# Creating the document...

doc = Document()

# Specifying where the output should be written...

whand = open('comedians.gexf', 'wb')

# Opening the database with the information to be written...

con = lite.connect('comedians.db')
cur = con.cursor()

# # Creating the top GEFX element within the XML...

gexfObject = doc.createElement("gexf")
gexfObject.setAttribute("xmlns", "http://www.gexf.net/1.2draft")
gexfObject.setAttribute("version", "1.2")
doc.appendChild(gexfObject)

# Creating metadata tags for the GEXF file...

metaObject = doc.createElement("meta")
metaObject.setAttribute("lastmodifieddate", "2012-02-16")
gexfObject.appendChild(metaObject)

creator = doc.createElement("project")
metaObject.appendChild(creator)
myName = doc.createTextNode("Stand-Up Comedian Genome Project")
creator.appendChild(myName)

description = doc.createElement("description")
metaObject.appendChild(description)
title = doc.createTextNode("A network visualization of influential American stand-up comedians.")
description.appendChild(title)

# Creating a graph element, which will be used to store the node and edge data...

graphObject = doc.createElement("graph")
graphObject.setAttribute("mode", "static")
graphObject.setAttribute("defaultedgetype", "directed")
gexfObject.appendChild(graphObject)

# Creating an element for the nodes in the graph...

nodes = doc.createElement("nodes")
graphObject.appendChild(nodes)

# Pulling data from the database and populating the nodes element...

cur.execute("SELECT uniqueID, name FROM Nodes")

for row in cur:
    uniqueID = str(row[0])
    name = row[1]
    
    node = doc.createElement("node")
    node.setAttribute("id", uniqueID)
    node.setAttribute("label", name)
    nodes.appendChild(node)

# Nodes are complete; creating an element for the edges in the graph...
    
edges = doc.createElement("edges")
graphObject.appendChild(edges)

cur.execute("SELECT Edges.uniqueID, Nodes.uniqueID FROM Edges, Nodes WHERE Edges.source = Nodes.name ORDER BY Edges.uniqueID ASC")

edgelist = []

for row in cur:
    
    uniqueID = row[0]
    source = row[1]
    
    entry = [uniqueID, source]
    
    edgelist.append(entry)
    
cur.execute("SELECT Edges.uniqueID, Nodes.uniqueID FROM Edges, Nodes WHERE Edges.target = Nodes.name ORDER BY Edges.uniqueID ASC")    

i = 0
targetlist = []

for row in cur:
    
    targetID = row[1]
    targetlist.append(targetID)
    
for entry in edgelist:
    
    edgelist[i].append(targetlist[i])
    i = i + 1

for entry in edgelist:
    
    edgeID = str(entry[0])
    sourceID = str(entry[1])
    targetID = str(entry[2])
    
    edge = doc.createElement("edge")
    edge.setAttribute("id", edgeID)
    edge.setAttribute("source", sourceID)
    edge.setAttribute("target", targetID)
    edges.appendChild(edge)

# And writing everything to the previously specified output document so that it can be imported into Gephi...
    
whand.write(doc.toprettyxml(encoding="UTF-8"))