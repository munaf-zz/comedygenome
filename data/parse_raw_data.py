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



print json.dumps(comedians)