#!/usr/bin/python3
import sys
import collections

i=1;
trans = collections.defaultdict(list)
query = []
prefix = {
	'Uzmobile':['99','95'],
	'Ucell':['93','94'],
	'Beeline':['90', '91'],
	'UMS': ['97'],
	'Perfectum': ['98']
}

def getCompanyName(prfx):
	for val in prefix:
		if prfx in prefix[val]: return val

## parsing the text from file
with open("data.txt") as file:
	for line in file:
		if (i == 1) : n = int(line.strip())
		if (i == 2) : k = int(line.strip())
		if (i>2 and i <= n+2): 
	 		transId, clientId, accountNo, amount, transDate, transTime = line.split('\t')
			trans[clientId, accountNo].append(accountNo)

		if (i > n+2):
			query.append(line.strip())

		i +=1

data = {}
j = 0
for (clientId, accountNo), vals in sorted(trans.items()):
	if(j != clientId):
		data[clientId]=[clientId, accountNo, len(vals)];
		j = clientId

for val in query:
	if val in data:
		prfx = data[val][1][:2]
		print "%s %s" % (data[val][1],getCompanyName(prfx))
	else:
		print "--"


