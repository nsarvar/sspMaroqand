#!/usr/bin/python3
import sys
import collections

i=1;
trans = collections.defaultdict(list)
query = []

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

data = []
j = 0
for (clientId, accountNo), vals in sorted(trans.items()):
	if(j != clientId):
		data.append([clientId, accountNo, len(vals)]);	
		j = clientId

print(data)
	#if(clientId in query):
	#	print '%s\t%s\t%d' % (clientId, accountNo, len(vals))



