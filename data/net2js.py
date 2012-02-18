import simplejson as json

netfile = open('comedians.net', 'r')

output = {}
output['nodes'] = []
output['links'] = []

vert = False
arcs = False
for line in netfile.readlines():
	if '*Vertices' in line:
		vert = True
		arcs = False
		continue
	if '*Arcs' in line:
		vert = False
		arcs = True
		continue
	
	if vert is True:
		#print line.split('"')
		name = line.split('"')[1].strip()

		#name = name.strip()
		#name.replace('"', '')

		output['nodes'].append(name)
	
	if arcs is True:
		(src,target) = line.split()
		src = int(src.strip()) - 1
		target = int(target.strip()) - 1

		output['links'].append({'source': src, 
								'target': target})

netfile.close()

outfile = open('comedians.js', 'w')
outfile.write('var comedians = ' + json.dumps(output) + ';')
outfile.close()
