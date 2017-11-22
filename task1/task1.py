#!/usr/bin/python3
import sys
import collections
import os

transactions = collections.defaultdict(list)
query = []
filename=sys.argv[-1]

prefix = {
	'Uzmobile':['99','95'],
	'Ucell':['93','94'],
	'Beeline':['90', '91'],
	'UMS': ['97'],
	'Perfectum': ['98']
}
i=1 # line counter


## function to identify the company name according to the prefix
def getCompanyName(prfx):
	for val in prefix:
		if prfx in prefix[val]: return val

## check if data file exists
if not os.path.exists(filename):
	print("file not found")
	sys.exit(0)

## parsing the text from file and storing into the list - transactions
with open(filename) as file:
	for line in file:
		if (i == 1) : n = int(line.strip())	# number of transactions
		if (i == 2) : k = int(line.strip())	# number of queries
		if (i>2 and i <= n+2): 
	 		transId, clientId, accountNo, amount, transDate, transTime = line.split('\t')
			transactions[clientId, accountNo].append(accountNo)

		if (i > n+2 and i<=n+k+2):
			query.append(line.strip())

		i +=1

data = {}
j = 0

## sorting and grouping the transactions list by clientID and accountNumber
for (clientId, accountNo), vals in sorted(transactions.items()):
	if(j != clientId):
		data[clientId]=[clientId, accountNo, len(vals)];
		j = clientId

for val in query:
	if val in data:
		prfx = data[val][1][:2]
		print "%s %s" % (data[val][1],getCompanyName(prfx))
	else:
		print "--"


