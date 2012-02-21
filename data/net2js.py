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
		name = line.split('"')[1].strip()
		output['nodes'].append({'name': name})
	
	if arcs is True:
		(src,target) = line.split()
		src = int(src.strip()) - 1
		target = int(target.strip()) - 1

		output['links'].append({'source': src, 
								'target': target})

netfile.close()

links = []
for link in output['links']:
	links.append({'source': output['nodes'][link['source']]['name'],
				 'target': output['nodes'][link['target']]['name']})

outfile = open('links.js', 'w')
outfile.write('var links = ' + json.dumps(links) + ';')
outfile.close()
