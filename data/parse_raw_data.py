import simplejson as json

influenced_file = open('source-data-influenced.txt', 'r')
#influenced_by_file = open('source-data-influencedby.txt', 'r')

results1 = json.loads(influenced_file.read())['result']
#results2 = json.loads(influenced_by_file.read())['result']

comedians = {}
for comedian in results1:
	
	name = comedian['name']
	comedians[name] = {}
	comedians[name]['influenced'] = []

	for c2 in comedian['/influence/influence_node/influenced']:
		comedians[name]['influenced'].append(c2['name'])


#for comedian in results2:
	# name = comedian['name']

	# if name not in comedians:
	# 	comedians[name] = {}
	# 	comedians[name]['influenced'] = []
	# 	comedians[name]['influenced_by'] = []

	# for c2 in comedian['/influence/influence_node/influenced_by']:
	# 	comedians[name]['influenced_by'].append(c2['name'])

#print comedians['Bill Hicks']



output = {}

output['nodes'] = []
output['links'] = []

for name in comedians:
	try:
		src_ind = output['nodes'].index(name)
	except:
		output['nodes'].append(unicode(name))
		src_ind = len(output['nodes']) - 1

	for com in comedians[name]['influenced']:
		try:
			dest_ind = output['nodes'].indexc(unicode(com))
		except:
			output['nodes'].append(unicode(com))
			dest_ind = len(output['nodes']) - 1
	
		link = {'source':src_ind,'target':dest_ind,'value':1}
		output['links'].append(link)

out_file = open('comedian_data.js', 'w')

out_file.write(json.dumps(output))

out_file.close()